$folder              = "C:\Users\hisham\Desktop\Job_Market_paper\Literature"
$reader              = "C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe"
$logFile             = Join-Path $folder "print_log_reader.csv"
$checklistFile       = Join-Path $folder "print_checklist.csv"
$preferredPrinter    = "PCL6 Driver for Universal Print"
$maxRetries          = 3
$sendDelay           = 20   # seconds to allow Reader to hand off the job
$retryDelay          = 20   # seconds before retrying a failed launch
$betweenFiles        = 5    # seconds between files
$jobAppearTimeout    = 10   # seconds to briefly observe the queue after sending
$queuePollInterval   = 2    # seconds between queue checks
$resumeAfterFile     = ""   # optional: set to the last PDF that physically printed

function Write-Log {
    param(
        [string]$FileName,
        [string]$FullPath,
        [string]$Status,
        [int]$Attempt,
        [string]$Message
    )

    $row = [PSCustomObject]@{
        Timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
        FileName  = $FileName
        FullPath  = $FullPath
        Status    = $Status
        Attempt   = $Attempt
        Message   = $Message
    }

    $row | Export-Csv -Path $logFile -NoTypeInformation -Append -Encoding UTF8
    return $row
}

function Test-ChecklistYes {
    param(
        [AllowNull()]
        [string]$Value
    )

    if ([string]::IsNullOrWhiteSpace($Value)) {
        return $false
    }

    $normalized = $Value.Trim().ToUpperInvariant()
    $normalized -in @("YES", "Y", "TRUE", "1", "X")
}

function Sync-Checklist {
    param(
        [array]$PdfFiles,
        [string]$ChecklistPath,
        [array]$LegacySentRows,
        [hashtable]$CompletedInfo
    )

    $existingRows = @()
    if (Test-Path $ChecklistPath) {
        try {
            $existingRows = @(Import-Csv -Path $ChecklistPath -ErrorAction Stop)
        }
        catch {
            $existingRows = @()
        }
    }

    $existingByPath = @{}
    foreach ($row in $existingRows) {
        if (-not [string]::IsNullOrWhiteSpace($row.FullPath)) {
            $existingByPath[$row.FullPath] = $row
        }
    }

    $legacyByPath = @{}
    $legacyOrder = 0
    foreach ($row in $LegacySentRows) {
        $legacyOrder++
        if (-not $legacyByPath.ContainsKey($row.FullPath)) {
            $legacyByPath[$row.FullPath] = [PSCustomObject]@{
                Order     = [string]$legacyOrder
                Timestamp = [string]$row.Timestamp
            }
        }
    }

    $rows = foreach ($file in $PdfFiles) {
        $existing = $null
        if ($existingByPath.ContainsKey($file.FullName)) {
            $existing = $existingByPath[$file.FullName]
        }

        $legacy = $null
        if ($legacyByPath.ContainsKey($file.FullName)) {
            $legacy = $legacyByPath[$file.FullName]
        }

        $confirmedPrinted = ""
        $confirmedAt = ""
        $lastStatus = ""
        $lastStatusAt = ""
        $notes = ""

        if ($null -ne $existing) {
            $confirmedPrinted = [string]$existing.ConfirmedPrinted
            $confirmedAt = [string]$existing.ConfirmedAt
            $lastStatus = [string]$existing.LastStatus
            $lastStatusAt = [string]$existing.LastStatusAt
            $notes = [string]$existing.Notes
        }

        if ($CompletedInfo.ContainsKey($file.FullName)) {
            $lastStatus = [string]$CompletedInfo[$file.FullName].Status
            $lastStatusAt = [string]$CompletedInfo[$file.FullName].Timestamp
        }

        [PSCustomObject]@{
            FileName           = $file.Name
            FullPath           = $file.FullName
            ConfirmedPrinted   = $confirmedPrinted
            ConfirmedAt        = $confirmedAt
            PriorSentOrder     = if ($null -ne $legacy) { $legacy.Order } else { "" }
            PriorSentTimestamp = if ($null -ne $legacy) { $legacy.Timestamp } else { "" }
            LastStatus         = $lastStatus
            LastStatusAt       = $lastStatusAt
            Notes              = $notes
        }
    }

    $rows | Export-Csv -Path $ChecklistPath -NoTypeInformation -Encoding UTF8
    return ,$rows
}

function Update-ChecklistEntry {
    param(
        [ref]$ChecklistRows,
        [string]$ChecklistPath,
        [string]$FullPath,
        [hashtable]$Updates
    )

    $row = $ChecklistRows.Value | Where-Object { $_.FullPath -eq $FullPath } | Select-Object -First 1
    if ($null -eq $row) {
        return
    }

    foreach ($name in $Updates.Keys) {
        if ($row.PSObject.Properties.Name -contains $name) {
            $row.$name = [string]$Updates[$name]
        }
    }

    $ChecklistRows.Value | Export-Csv -Path $ChecklistPath -NoTypeInformation -Encoding UTF8
}

function Stop-AllReaderProcesses {
    $readerProcesses = @(Get-Process AcroRd32 -ErrorAction SilentlyContinue)
    foreach ($readerProcess in $readerProcesses) {
        try {
            Stop-Process -Id $readerProcess.Id -Force -ErrorAction SilentlyContinue
        }
        catch {
        }
    }
}

function Get-QueueJobs {
    param(
        [string]$PrinterName
    )

    try {
        @(Get-PrintJob -PrinterName $PrinterName -ErrorAction Stop | Sort-Object ID)
    }
    catch {
        throw "Unable to read the print queue for '$PrinterName'. $($_.Exception.Message)"
    }
}

function Stop-ReaderProcess {
    param(
        [System.Diagnostics.Process]$Process
    )

    if ($null -eq $Process) {
        return
    }

    try {
        if (-not $Process.HasExited) {
            Stop-Process -Id $Process.Id -Force -ErrorAction SilentlyContinue
        }
    }
    catch {
    }
}

function Test-PrintJobMatch {
    param(
        [object]$Job,
        [string]$FileName,
        [string]$BaseName,
        [string]$UserName
    )

    $matchesUser = $false
    if ($null -ne $Job.UserName -and -not [string]::IsNullOrWhiteSpace([string]$Job.UserName)) {
        $jobUser = ([string]$Job.UserName).Split('\')[-1]
        $matchesUser = $jobUser.Equals($UserName, [System.StringComparison]::OrdinalIgnoreCase)
    }

    $matchesDoc = $false
    $docName = [string]$Job.DocumentName
    if (-not [string]::IsNullOrWhiteSpace($docName)) {
        $matchesDoc =
            $docName.IndexOf($FileName, [System.StringComparison]::OrdinalIgnoreCase) -ge 0 -or
            $docName.IndexOf($BaseName, [System.StringComparison]::OrdinalIgnoreCase) -ge 0
    }

    $matchesUser -or $matchesDoc
}

function Wait-ForNewPrintJobs {
    param(
        [string]$PrinterName,
        [int[]]$ExistingIds,
        [string]$FileName,
        [string]$BaseName,
        [string]$UserName,
        [int]$TimeoutSeconds,
        [int]$PollIntervalSeconds
    )

    $deadline = (Get-Date).AddSeconds($TimeoutSeconds)
    $fallbackJobs = @()

    while ((Get-Date) -lt $deadline) {
        $jobs = Get-QueueJobs -PrinterName $PrinterName
        $newJobs = @($jobs | Where-Object { [int]$_.ID -notin $ExistingIds })

        if ($newJobs.Count -gt 0) {
            $matchingJobs = @(
                $newJobs | Where-Object {
                    Test-PrintJobMatch -Job $_ -FileName $FileName -BaseName $BaseName -UserName $UserName
                }
            )

            if ($matchingJobs.Count -gt 0) {
                return $matchingJobs
            }

            if ($fallbackJobs.Count -eq 0) {
                $fallbackJobs = $newJobs
            }
        }

        Start-Sleep -Seconds $PollIntervalSeconds
    }

    if ($fallbackJobs.Count -eq 1) {
        return $fallbackJobs
    }

    @()
}

if (-not (Test-Path $folder)) {
    Write-Error "Folder not found: $folder"
    exit 1
}

if (-not (Test-Path $reader)) {
    Write-Error "Adobe Reader executable not found: $reader"
    exit 1
}

if (-not (Get-Command Get-PrintJob -ErrorAction SilentlyContinue)) {
    Write-Error "Get-PrintJob is not available on this machine. Install the PrintManagement module or use a different printer automation tool."
    exit 1
}

$defaultPrinter = Get-CimInstance Win32_Printer | Where-Object { $_.Name -eq $preferredPrinter } | Select-Object -First 1

if ($null -eq $defaultPrinter) {
    $defaultPrinter = Get-CimInstance Win32_Printer | Where-Object { $_.Default -eq $true } | Select-Object -First 1
}

if ($null -eq $defaultPrinter) {
    Write-Error "Printer not found. Preferred printer: $preferredPrinter"
    exit 1
}

$printerName = $defaultPrinter.Name
$driverName  = $defaultPrinter.DriverName
$portName    = $defaultPrinter.PortName

Write-Host "Printer selected:"
Write-Host "  Name      : $printerName"
Write-Host "  Driver    : $driverName"
Write-Host "  Port      : $portName"
Write-Host ""

$allPdfs = @(Get-ChildItem -Path $folder -Filter *.pdf | Sort-Object Name)
if (-not $allPdfs -or $allPdfs.Count -eq 0) {
    Write-Host "No PDF files found in $folder"
    exit 0
}

if (-not [string]::IsNullOrWhiteSpace($resumeAfterFile) -and -not ($allPdfs.Name -contains $resumeAfterFile)) {
    Write-Error "Resume file not found in the folder: $resumeAfterFile"
    exit 1
}

$statusInfo = @{}
$legacySentRows = @()

if (Test-Path $logFile) {
    try {
        $existing = @(Import-Csv -Path $logFile -ErrorAction Stop)
        foreach ($row in $existing) {
            if (-not [string]::IsNullOrWhiteSpace([string]$row.Status)) {
                $statusInfo[$row.FullPath] = [PSCustomObject]@{
                    Status    = [string]$row.Status
                    Timestamp = [string]$row.Timestamp
                }
            }

            if ($row.Status -eq "SENT") {
                $legacySentRows += $row
            }
        }
    }
    catch {
    }
}

$checklistRows = Sync-Checklist `
    -PdfFiles $allPdfs `
    -ChecklistPath $checklistFile `
    -LegacySentRows $legacySentRows `
    -CompletedInfo $statusInfo

$alreadyCompleted = @{}
foreach ($row in $checklistRows) {
    if (Test-ChecklistYes -Value $row.ConfirmedPrinted) {
        $alreadyCompleted[$row.FullPath] = $true
    }
}

Write-Host "Found $($allPdfs.Count) PDF files."
Write-Host "Log file: $logFile"
Write-Host "Checklist file: $checklistFile"
Write-Host ""
Write-Host "ConfirmedPrinted = YES in the checklist is the only skip rule."
Write-Host "The script updates LastStatus automatically, but you should keep using the checklist as the source of truth."
if (-not [string]::IsNullOrWhiteSpace($resumeAfterFile)) {
    Write-Host "Resume mode: printing starts after $resumeAfterFile"
}
Write-Host ""

$startPrinting = [string]::IsNullOrWhiteSpace($resumeAfterFile)

foreach ($file in $allPdfs) {

    if (-not $startPrinting) {
        if ($file.Name -eq $resumeAfterFile) {
            $startPrinting = $true
            Write-Host "Resume point found: $($file.Name)"
            continue
        }

        Write-Host "Skipping before resume point: $($file.Name)"
        continue
    }

    if ($alreadyCompleted.ContainsKey($file.FullName)) {
        Write-Host "Skipping already completed: $($file.Name)"
        continue
    }

    $completed = $false

    for ($attempt = 1; $attempt -le $maxRetries; $attempt++) {
        Write-Host "Printing [$attempt/$maxRetries]: $($file.Name)"

        $proc = $null

        try {
            Stop-AllReaderProcesses
            Start-Sleep -Seconds 2

            $existingJobs = Get-QueueJobs -PrinterName $printerName
            $existingIds = @($existingJobs | ForEach-Object { [int]$_.ID })

            $args = "/h /t `"$($file.FullName)`" `"$printerName`" `"$driverName`" `"$portName`""
            $proc = Start-Process -FilePath $reader -ArgumentList $args -PassThru -WindowStyle Hidden

            Start-Sleep -Seconds $sendDelay
            Stop-AllReaderProcesses
            Start-Sleep -Seconds 3

            $queuedJobs = Wait-ForNewPrintJobs `
                -PrinterName $printerName `
                -ExistingIds $existingIds `
                -FileName $file.Name `
                -BaseName $file.BaseName `
                -UserName $env:USERNAME `
                -TimeoutSeconds $jobAppearTimeout `
                -PollIntervalSeconds $queuePollInterval

            $status = "SENT"
            $message = "Print command sent to Adobe Reader using default printer settings."
            if ($queuedJobs -and $queuedJobs.Count -gt 0) {
                $queuedIds = @($queuedJobs | ForEach-Object { [int]$_.ID })
                $jobIdText = $queuedIds -join ", "
                $status = "SENT_QUEUE_VISIBLE"
                $message = "Print command sent to Adobe Reader. Queue showed job id(s): $jobIdText."
                Write-Host "Sent: $($file.Name) [job id(s): $jobIdText]"
            }
            else {
                Write-Host "Sent: $($file.Name) [no queue confirmation visible]"
            }

            $sentLog = Write-Log -FileName $file.Name -FullPath $file.FullName -Status $status -Attempt $attempt -Message $message
            Update-ChecklistEntry `
                -ChecklistRows ([ref]$checklistRows) `
                -ChecklistPath $checklistFile `
                -FullPath $file.FullName `
                -Updates @{
                    LastStatus   = $status
                    LastStatusAt = $sentLog.Timestamp
                }
            $completed = $true
            break
        }
        catch {
            $msg = $_.Exception.Message
            $failedLog = Write-Log -FileName $file.Name -FullPath $file.FullName -Status "FAILED" -Attempt $attempt -Message $msg
            Update-ChecklistEntry `
                -ChecklistRows ([ref]$checklistRows) `
                -ChecklistPath $checklistFile `
                -FullPath $file.FullName `
                -Updates @{
                    LastStatus   = "FAILED"
                    LastStatusAt = $failedLog.Timestamp
                }
            Write-Host "Failed: $($file.Name) -- $msg"

            if ($attempt -lt $maxRetries) {
                Write-Host "Retrying after $retryDelay seconds..."
                Start-Sleep -Seconds $retryDelay
            }
        }
        finally {
            Stop-ReaderProcess -Process $proc
        }
    }

    if (-not $completed) {
        Write-Host "Giving up on: $($file.Name)"
    }

    Start-Sleep -Seconds $betweenFiles
}

Write-Host ""
Write-Host "Done."
Write-Host "Check the log file here:"
Write-Host $logFile
