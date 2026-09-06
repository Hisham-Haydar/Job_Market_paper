"""Render v4.1 figures from frozen data; all MNL inputs are read only.

Notebook cells 61/63 supply the Box-Cox inversion used for indifference curves.
The selected households' own priced nodes replace its aggregated type profiles.
No source notebook/renderer is executed; no estimation or pricing is run.
"""
from __future__ import annotations

import argparse
import json
import hashlib
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import PercentFormatter
from matplotlib.lines import Line2D

from make_slide_figures_v1 import (
    DEFAULT_SPRINT, SLIDE_RC, C_ACC, C_PREF, C_ENV, C_NEEDS, INK, INDEX, new_ax, save,
)


def household_a(sprint: Path, out: Path) -> None:
    """Employment mass, conditional hours/occupation factors, wage mixture."""
    source = 'figE1_matched_pair.csv'
    data = pd.read_csv(sprint / 'figures' / source)
    data = data.loc[data.household.eq('A')]
    meta = json.loads((sprint / 'runs/figE1_matched_households/'
                       'e1_matched_households_v1.json').read_text('utf-8'))
    person = meta['pairs']['employed::forward']['household_1']
    pi = float(person['pi_participation'])
    nonwork = float(data.loc[data.panel.eq('non_employment_mass'), 'y'].iloc[0])
    np.testing.assert_allclose(1-nonwork, pi)
    fig, ax = new_ax('', 'Employment mass')
    ax.bar(['Non-employment', 'Employment'], [nonwork, pi],
           color=['#b2b2b2', C_ACC], width=.52)
    ax.set_ylim(0, 1)
    ax.yaxis.set_major_formatter(PercentFormatter(1))
    for i,value in enumerate([nonwork,pi]):
        ax.text(i,value+.025,f'{value:.1%}',ha='center',va='bottom')
    save(fig,'household_a_employment',out,source,'household A / employment mass')
    panels = [
        ('hours_offer_density', 'household_a_hours',
         'Weekly hours offered', 'Hours density given employment'),
        ('occupation_offer_probability', 'household_a_occupation',
         'Occupation group', 'Occupation share given employment'),
        ('wage_offer_density', 'household_a_wages',
         'Hourly wage offer (EUR)', 'Density given employment'),
    ]
    for panel, name, xlabel, ylabel in panels:
        rows = data.loc[data.panel.eq(panel)].sort_values('x').copy()
        assert len(rows) > 0 and np.isfinite(rows[['x', 'y']]).all().all()
        if panel in ['hours_offer_density','occupation_offer_probability']:
            rows['y'] /= pi
        fig, ax = new_ax(xlabel, ylabel)
        if panel == 'occupation_offer_probability':
            bars = ax.bar(rows.x, rows.y, width=.65, color=C_ACC, alpha=.85)
            ax.set_xticks(rows.x)
            ax.yaxis.set_major_formatter(PercentFormatter(1))
            for bar, group in zip(bars, rows.x):
                if group == person['observed_occupation']:
                    bar.set_edgecolor(INK)
                    bar.set_linewidth(3)
            np.testing.assert_allclose(rows.y.sum(), 1)
        else:
            ax.plot(rows.x, rows.y, color=C_ACC)
            if panel != 'preference_profile':
                ax.fill_between(rows.x, 0, rows.y, color=C_ACC, alpha=.13)
                observed = person['observed_hours' if panel == 'hours_offer_density'
                                  else 'observed_wage_eur_per_hour']
                ax.axvline(observed, color=INK, linewidth=2, linestyle='--')
                ax.set_ylim(bottom=0)
            ax.set_xlim(rows.x.min(), rows.x.max())
        save(fig, name, out, source, 'household A / ' + panel+
             (' / divided by employment mass' if panel!='wage_offer_density' else ''))


def compensation_by_age(sprint: Path, out: Path) -> None:
    """The final model's two exact analytic figAB02 curves."""
    source = 'figAB02_mrs_by_age_sex.csv'
    data = pd.read_csv(sprint / 'figures' / source)
    data = data.loc[data.panel.eq('analytic')]
    meta = json.loads((sprint / 'runs/agebound_addendum_s2/'
                       'ab_step2_profiles_v1.json').read_text('utf-8'))
    fig, ax = new_ax('Age', 'Compensation (EUR/month)\nper extra weekly hour')
    for sex, colour, style, label in [('female', C_PREF, '-', 'Women'),
                                      ('male', C_ACC, '--', 'Men')]:
        rows = data.loc[data.model.eq('S8') & data.sex.eq(sex)].sort_values('age')
        assert len(rows) > 0
        ax.plot(rows.age, rows.mrs_eur_per_month_per_weekly_hour,
                color=colour, linestyle=style, label=label)
    convention = meta['frame_conventions']
    lo, hi = float(data.age.min()), float(data.age.max())
    if convention['observed_age_min'] > lo:
        ax.axvspan(lo, convention['observed_age_min'], color='#f2f2f2', zorder=0)
    if convention['observed_age_max'] < hi:
        ax.axvspan(convention['observed_age_max'], hi, color='#f2f2f2', zorder=0)
    ax.set_xlim(lo, hi)
    ax.set_ylim(bottom=0)
    ax.legend(loc='upper center', ncol=2)
    save(fig, 'compensation_by_age', out, source, 'analytic reference bundle')


def boxcox(x, theta):
    x=np.asarray(x,dtype=float)
    return np.log(x) if abs(theta)<1e-10 else np.expm1(theta*np.log(x))/theta


def inverse_boxcox(y, theta):
    y=np.asarray(y,dtype=float)
    if abs(theta)<1e-10:return np.exp(y)
    z=1+theta*y
    return np.power(np.where(z>0,z,np.nan),1/theta)


def indifference_curves(sprint: Path, out: Path) -> None:
    frame=sprint/'export/gpu_research_bundle_v1/data/fr_p2a_singles2016_regionlive_margqh_floor5_v1__singles.parquet'
    cols=['idhh','is_chosen','hours','consumption','female','working','dag',
          'age_norm','n_children','wage','c_scale','l_scale','l_norm']
    d=pd.read_parquet(frame,columns=cols)
    obs=d.loc[d.is_chosen.eq(1)].copy()
    parameters=pd.read_csv(sprint/'runs/agebound_addendum_s2/ab_parameter_table_S8_v1.csv').set_index('param').estimate
    np.testing.assert_allclose(d.l_norm,(80-d.hours)/d.l_scale,atol=1e-12)
    fig,ax=new_ax('Weekly hours worked','Disposable consumption (EUR/month)')
    ax.axvspan(33.5,36.5,color='#e0a458',alpha=.18,zorder=0)
    hgrid=np.linspace(0,70,501)
    yvalues=[]
    diagnostics=[]
    for female,suffix,col,label,style in [(1,'_sf',C_PREF,'Woman','-'),
                                         (0,'_sm',C_ACC,'Man','--')]:
        pool=obs.loc[obs.female.eq(female)&obs.working.gt(0)&obs.n_children.eq(0)].copy()
        # Deterministic central employed adult: nearest to age 40, 35 hours,
        # and the sex-specific median consumption. Ties retain frame order.
        pool['distance']=((pool.dag-40)/10)**2+((pool.hours-35)/10)**2+((pool.consumption-pool.consumption.median())/pool.consumption.median())**2
        person=pool.sort_values('distance',kind='stable').iloc[0]
        nodes=d.loc[d.idhh.eq(person.idhh)].copy()
        assert len(nodes)==101
        cs=float(person.c_scale); ls=float(person.l_scale)
        tc=float(parameters['theta_c_singles']);tl=float(parameters['theta_l'+suffix])
        age=float(person.age_norm)
        omega=float(parameters['beta_l0'+suffix]+parameters['beta_l_age'+suffix]*age+parameters['beta_l_age2'+suffix]*age**2)
        if female:omega+=float(parameters['beta_l_nkids_sf'])*float(person.n_children)
        def utility(h,c):return omega*boxcox((80-np.asarray(h))/ls,tl)+boxcox(np.asarray(c)/cs,tc)
        attained=float(utility(person.hours,person.consumption))
        # Same analytic inversion as reader's guide cell 63; the middle
        # indifference curve passes through the actual observed job.
        residual=0.
        for delta in [-.22,0,.22]:
            consumption=inverse_boxcox(attained+delta-omega*boxcox((80-hgrid)/ls,tl),tc)*cs
            valid=np.isfinite(consumption)
            residual=max(residual,float(np.max(np.abs(utility(hgrid[valid],consumption[valid])-(attained+delta)))))
            ax.plot(hgrid,consumption,color=col,linestyle=style,
                    linewidth=3 if delta==0 else 1.8,alpha=1 if delta==0 else .4)
        observed_c=float(inverse_boxcox(attained-omega*boxcox((80-person.hours)/ls,tl),tc)*cs)
        np.testing.assert_allclose(observed_c,person.consumption,rtol=1e-12)
        assert residual<1e-10
        # These are the household's own EUROMOD-priced packages. Since wage
        # differs across sampled jobs, no spurious single budget line joins them.
        ax.scatter(nodes.hours,nodes.consumption,s=24,color=col,alpha=.24,linewidths=0)
        ax.scatter([person.hours],[person.consumption],s=185,color=col,marker='D',edgecolors='white',linewidths=1.8,zorder=8)
        yvalues.extend(nodes.consumption.tolist())
        diagnostics.append({'sex':label,'priced_nodes':len(nodes),'utility_residual_max':residual,
                            'observed_curve_consumption_error':abs(observed_c-person.consumption)})
    ax.set_xlim(0,70)
    ax.set_ylim(0,max(yvalues)*1.06)
    ax.legend(handles=[Line2D([],[],color=C_PREF,lw=3,label='Woman'),
                       Line2D([],[],color=C_ACC,lw=3,ls='--',label='Man'),
                       Line2D([],[],color=INK,marker='o',ls='',alpha=.4,label='Priced packages'),
                       Line2D([],[],color=INK,marker='D',ls='',label='Observed job')],
              loc='upper left',ncol=2)
    save(fig,'indifference_curves',out,str(frame.relative_to(sprint)),
         'one actual household per sex; own priced nodes; notebook cells 61/63 inversion')
    (out/'indifference_checks.json').write_text(json.dumps(diagnostics,indent=2),encoding='utf8')


def welfare_distributions(sprint: Path, out: Path) -> None:
    """Original figW01 weighted KDE, checked against every raw summary row.

    Its CSV stores summaries only. The original renderer's frozen household
    parquet is required for the distribution shapes; no parametric substitute.
    """
    source='figW01_welfare_distributions.csv'
    summary=pd.read_csv(sprint/'figures'/source)
    summary=summary.loc[summary.basis.eq('W1_raw')].set_index('cell')
    d=pd.read_parquet(sprint/'runs/final_singles_welfare/ss8_principal_state_distributions_v1.parquet')
    d=d.loc[d.model.eq('S8')&d.reference_arm.eq('singles_female')]
    cells=['{}','{P}','{A,B,D}','{A,B,D,P}']
    arrays=[(d.loc[d.cell.eq(c),'W1_raw'].to_numpy(float),d.loc[d.cell.eq(c),'dwt'].to_numpy(float)) for c in cells]
    lo=min(np.percentile(x,.5) for x,w in arrays)
    hi=max(np.percentile(x,99.5) for x,w in arrays)
    grid=np.linspace(lo,hi,512);floor=(hi-lo)/120
    fig,ax=new_ax('Equivalent income (EUR per month)','Weighted density')
    checks=[];maxdensity=0
    for cell,label,colour,(x,w) in zip(cells,['I00','I10','I01','I11'],[C_ACC,C_PREF,C_ENV,C_NEEDS],arrays):
        w=w/w.sum();mu=float(w@x);sd=float(np.sqrt(w@((x-mu)**2)))
        order=np.argsort(x,kind='stable');xs=x[order];ws=w[order]
        rank=np.cumsum(ws)-.5*ws
        gini=float(2*np.sum(ws*(xs-mu)*(rank-.5))/mu)
        row=summary.loc[cell]
        np.testing.assert_allclose([mu,sd,gini],[row.weighted_mean,row.weighted_sd,row.gini],rtol=1e-10,atol=1e-10)
        assert len(x)==int(row.n)
        if sd<=1e-9*max(abs(mu),1):
            ax.axvline(mu,color=colour,lw=3,ls='--',label=label)
        else:
            bandwidth=max(1.06*sd*(1/(w@w))**(-.2),floor)
            z=(grid[:,None]-x[None,:])/bandwidth
            y=(np.exp(-.5*z*z)@w)/(bandwidth*np.sqrt(2*np.pi))
            ax.plot(grid,y,color=colour,label=label)
            maxdensity=max(maxdensity,float(y.max()))
        checks.append({'state':label,'n':len(x),'mean':mu,'sd':sd,'gini':gini,'summary_matches':True})
    ax.set_xlim(lo,hi);ax.set_ylim(0,maxdensity*1.12)
    ax.legend(loc='upper right',ncol=2)
    save(fig,'welfare_distributions',out,source,'raw / female reference / source weighted KDE; I11 point mass')
    (out/'welfare_distribution_checks.json').write_text(json.dumps(checks,indent=2),encoding='utf8')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sprint', type=Path, default=DEFAULT_SPRINT)
    parser.add_argument('--out', type=Path,
                        default=Path(__file__).parent / 'figures/slides')
    args = parser.parse_args()
    INDEX.clear()
    style={**SLIDE_RC,'font.size':26,'axes.labelsize':26,
           'xtick.labelsize':22,'ytick.labelsize':22,'legend.fontsize':22}
    with matplotlib.rc_context(style):
        household_a(args.sprint, args.out)
        compensation_by_age(args.sprint, args.out)
        indifference_curves(args.sprint,args.out)
        welfare_distributions(args.sprint,args.out)
    indexpath=args.out/'slide_figure_index.csv'
    index=pd.DataFrame(INDEX)
    if indexpath.exists():index=pd.concat([pd.read_csv(indexpath),index],ignore_index=True).drop_duplicates('slide_figure',keep='last')
    index.to_csv(indexpath,index=False)
    sources=[args.sprint/'figures'/s for s in ['figE1_matched_pair.csv','figAB02_mrs_by_age_sex.csv','figW01_welfare_distributions.csv']]
    sources += [args.sprint/'runs'/s for s in ['figE1_matched_households/e1_matched_households_v1.json','agebound_addendum_s2/ab_parameter_table_S8_v1.csv','agebound_addendum_s2/ab_step2_profiles_v1.json','final_singles_welfare/ss8_principal_state_distributions_v1.parquet']]
    sources += [args.sprint/'export/gpu_research_bundle_v1/data/fr_p2a_singles2016_regionlive_margqh_floor5_v1__singles.parquet',args.sprint.parents[1]/'notebooks/france/fr_singles_results_discussion_v1.ipynb']
    records=[{'path':str(p.relative_to(args.sprint.parents[1])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sources]
    (args.out/'v41_source_manifest.json').write_text(json.dumps(records,indent=2),encoding='utf8')


if __name__ == '__main__':
    main()
