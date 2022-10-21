import numpy as np
import proplot as pplt

ALPHA = 0.3
WIDTH = 2.8
# YLIM = (-2.5, 2.5)
YLIM = (-3.5, 3.5)
REQUIREMENT = 0.002

LCOLOR = 'sienna'
SECCOLOR = 'sand'
FCOLOR = 'black'

# COLORS = [
#     '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
#     '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
# ]
COLORS = ['black']*4

HATCHES = [
    # None,
    '//',
    '\\\\',
    '||',
    '-',
    # '+',
    # 'x',
    # 'o',
    # 'O',
    # '.',
    # '*',
    None,
]


def add_lines(ax):
    lw = 1
    ax.axhline(0, color='black', lw=0.5*lw)
    # ax.axhline(-REQUIREMENT/0.001, color=LCOLOR, linestyle='dashed', lw=lw)
    # ax.axhline(+REQUIREMENT/0.001, color=LCOLOR, linestyle='dashed', lw=lw)

    ax.axhline(
        0.4, color=SECCOLOR, lw=lw, alpha=0.5, linestyle='dashdot',
        # label='Higher Order Shear',
        label='Nonlinear Shear',
    )


def do_Tratio_bias_plot(ax):

    xlim = (1.15, 1.55)
    ax.set(
        xlabel='Minimum $T/T_{PSF}$',
        ylabel='m / 0.001',
        xlim=xlim,
        ylim=YLIM,
    )
    ax.fill_between(
        xlim,
        [REQUIREMENT/0.001]*2,
        [-REQUIREMENT/0.001]*2,
        alpha=0.1,
        color=LCOLOR,
        hatch=None,
        label='Requirement',
    )


    Tratios = [1.2, 1.3, 1.4, 1.5]

    # run-riz-drcbWP-cells
    # mlows = np.array(
    #     [0.000227885, -0.000161471,  -0.000193378, -0.000423672]
    # )/0.001
    # mhighs = np.array(
    #     [0.00148068, 0.00118696, 0.00143503, 0.00158595]
    # )/0.001

    # run-WPv0.1-nowarp
    mlows = np.array(
        [0.000211992, 0.000151222, -5.32513e-05, -0.000346328]
    )/0.001
    mhighs = np.array(
        [0.000967327, 0.00104341, 0.000960636, 0.000968678]
    )/0.001

    ax.fill_between(
        Tratios,
        mlows,
        mhighs,
        color=COLORS[0],
        alpha=ALPHA,
        hatch=HATCHES[0],
        # label='cells',
        label='LSST 10 year PSF',
    )

    # run-drcbWP
    # mlows = np.array(
    #     [-0.000375975, -0.000637519, -0.000838113, -0.00100003]
    # )/0.001
    # mhighs = np.array(
    #     [0.000483453, 0.000308397, 0.000336744, 0.000378551],
    # )/0.001
    #
    # ax.fill_between(
    #     Tratios,
    #     mlows,
    #     mhighs,
    #     color=COLORS[1],
    #     alpha=ALPHA,
    #     hatch=HATCHES[1],
    #     label='no cells',
    # )

    # run-WM-nowarp
    mlows = np.array(
        [0.000165007, -8.56819e-05, -0.000114263, -0.000370727]
    )/0.001
    mhighs = np.array(
        [0.000915298, 0.000799206, 0.000858479, 0.000987993]
    )/0.001

    ax.fill_between(
        Tratios,
        mlows,
        mhighs,
        color=COLORS[3],
        alpha=ALPHA,
        hatch=HATCHES[2],
        label='constant PSF',
    )

    add_lines(ax)


def do_s2n_bias_plot(ax):

    xlim = (9, 21)

    ax.set(
        xlabel='Minimum S/N',
        ylabel='m / 0.001',
        xlim=xlim,
        ylim=YLIM,
    )

    s2ns = [10, 12.5, 15, 20]
    # run-riz-drcbWP-cells
    # mlows = np.array(
    #     [0.000553132, -5.80659e-05, 0.000227885, -3.67881e-05]
    # )/0.001
    # mhighs = np.array(
    #     [0.0020267, 0.00131326, 0.00148068, 0.00113388]
    # )/0.001

    # run-WPv0.1-nowarp
    mlows = np.array(
        [0.000219245, 7.80083e-05, 0.000213062, 0.000257441]
    )/0.001
    mhighs = np.array(
        [0.00121502, 0.000868853, 0.000972641, 0.000891671]
    )/0.001

    ax.fill_between(
        xlim,
        [REQUIREMENT/0.001]*2,
        [-REQUIREMENT/0.001]*2,
        alpha=0.1,
        color=LCOLOR,
        label='Requirement',
    )

    ax.fill_between(
        s2ns,
        mlows,
        mhighs,
        color=COLORS[0],
        alpha=ALPHA,
        hatch=HATCHES[0],
        # label='cells',
        label='LSST 10 year PSF',
    )

    # run-drcbWP
    # mlows = np.array(
    #     [-0.000506131, -0.000547303, -0.000375975, -0.000404532]
    # )/0.001
    # mhighs = np.array(
    #     [0.000519134, 0.000391566, 0.000483453, 0.000371225],
    # )/0.001
    # ax.fill_between(
    #     s2ns,
    #     mlows,
    #     mhighs,
    #     # color=FCOLOR,
    #     color=COLORS[1],
    #     alpha=ALPHA,
    #     hatch=HATCHES[1],
    #     label='no cells',
    # )

    # run-WM-nowarp
    mlows = np.array(
        [0.000176295, -8.26672e-06, 0.000165007, 0.000111993]
    )/0.001
    mhighs = np.array(
        [0.00113744, 0.000789173, 0.000915298, 0.000765478]
    )/0.001
    ax.fill_between(
        s2ns,
        mlows,
        mhighs,
        # color=FCOLOR,
        color=COLORS[3],
        alpha=ALPHA,
        hatch=HATCHES[2],
        label='constant PSF',
    )

    add_lines(ax)

    ax.text(
        0.50,
        0.87,
        r'99.7\% confidence range',
        transform=ax.transAxes,
    )
    ax.legend(
        loc='lower right',
        ncol=2,
        # pad=.5,
    )


def main():

    fig, axs = pplt.subplots(
        nrows=2, ncols=1, refwidth=WIDTH,
        # spany=True,
        refaspect=(1.618, 1),
        share=False,
    )
    # axs.format(
    #     abc='a)', abcloc='ul',
    #     abc_kw={'color': 'dark red'},
    # )

    do_s2n_bias_plot(axs[0])
    do_Tratio_bias_plot(axs[1])

    fname = 'trends.pdf'
    print('writing:', fname)
    fig.savefig(fname)


main()
