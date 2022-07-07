import numpy as np
import proplot as pplt

ALPHA = 0.3
WIDTH = 2.8

MARKERS = ('o', 'd', '^', 's', 'v', 'h', 'p', 'P', 'H', 'X')

EXTRA_LINESTYLES = {
    'loose dotted': (0, (1, 10)),
    'dense dotted': (0, (1, 1)),

    'loose dashed': (0, (5, 5)),
    'very loose dashed': (0, (5, 10)),
    'dense dashed': (0, (5, 1)),

    'dashdotdot': (0, (3, 5, 1, 5, 1, 5)),

    'dense dashdot': (0, (3, 1, 1, 1)),
    'dense dashdotdot': (0, (3, 1, 1, 1, 1, 1)),
}

LINESTYLES = (
    'solid', 'dashed', 'dotted',
    EXTRA_LINESTYLES['dense dashdot'],
    EXTRA_LINESTYLES['loose dashed'],
    EXTRA_LINESTYLES['dense dashdotdot'],
    EXTRA_LINESTYLES['dense dotted'],
    'dashdot',
    EXTRA_LINESTYLES['very loose dashed'],
    EXTRA_LINESTYLES['dense dashed'],
)
LCOLOR = 'sienna'
# SECCOLOR = 'orange5'
SECCOLOR = 'sand'
# FCOLOR = '#8c564b'
FCOLOR = 'black'

COLORS = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
    '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
]
COLORS = ['black']*4

HATCHES = [
    None,
    '//',
    '\\\\',
    '||',
    # '-',
    # '+',
    # 'x',
    # 'o',
    # 'O',
    # '.',
    # '*',
    None,
]


def add_lines(ax):
    lim = 1
    lw = 1
    ax.axhline(0, color='black', lw=0.5*lw)
    ax.axhline(-lim, color=LCOLOR, linestyle='dashed', lw=lw)
    ax.axhline(+lim, color=LCOLOR, linestyle='dashed', lw=lw)

    ax.axhline(0.4, color=SECCOLOR, lw=lw, alpha=0.5, linestyle='dashdot')


def do_Tratio_bias_plot(ax):

    ax.set(
        xlabel='Minimum $T/T_{PSF}$',
        ylabel='m / 0.001',
        xlim=(1.15, 1.55),
        ylim=(-3, 3),
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

    # ax.text(
    #     1.2,
    #     -2,
    #     r'99.7\% confidence errors',
    # )


def do_s2n_bias_plot(ax):

    ax.set(
        xlabel='Minimum S/N',
        ylabel='m / 0.001',
        xlim=(9, 21),
        ylim=(-3, 3),
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
        15,
        2,
        r'99.7\% confidence range',
    )
    ax.legend(
        loc='lower right',
        ncol=1,
        pad=1,
    )


def main():

    fig, axs = pplt.subplots(
        nrows=2, ncols=1, refwidth=WIDTH,
        # spany=True,
        refaspect=(1.618, 1),
        share=False,
    )
    # axs.format(
        # abc='a)', abcloc='ul',
        # abc_kw={'color': 'dark red'},
    # )

    do_s2n_bias_plot(axs[0])
    do_Tratio_bias_plot(axs[1])

    fname = 'trends.pdf'
    print('writing:', fname)
    fig.savefig(fname)


main()
