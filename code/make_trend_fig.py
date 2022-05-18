import numpy as np
import argparse
from matplotlib import pyplot as mplt

ALPHA = 0.3
WIDTH = 6

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
LCOLOR = 'brown'
# FCOLOR = '#8c564b'
FCOLOR = 'black'

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
    ax.axhline(0, color='black')  # , zorder=zorder)
    ax.axhline(-lim, color=LCOLOR, linestyle='dashed')  # , zorder=zorder)
    ax.axhline(+lim, color=LCOLOR, linestyle='dashed')  # , zorder=zorder)

    ax.axhline(0.4, color='blue', lw=2, alpha=0.5)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pdf', required=True)
    return parser.parse_args()


def do_Tratio_bias_plot(ax):

    ax.set(
        xlabel='minimum $T/T_{PSF}$',
        ylabel='m / 0.001',
        ylim=(-3, 3),
    )

    Tratios = [1.2, 1.3, 1.4, 1.5]
    # run-riz-drcbWP-cells
    mlows = np.array(
        [0.000227885, -0.000161471,  -0.000193378, -0.000423672]
    )/0.001
    mhighs = np.array(
        [0.00148068, 0.00118696, 0.00143503, 0.00158595]
    )/0.001
    # add run-drcbWP here

    ax.fill_between(
        Tratios,
        mlows,
        mhighs,
        color=FCOLOR,
        alpha=ALPHA,
    )

    add_lines(ax)

    ax.text(
        1.2,
        -2,
        r'99.7\% confidence errors',
    )


def do_s2n_bias_plot(ax):

    ax.set(
        xlabel='minimum S/N',
        ylabel='m / 0.001',
        ylim=(-3, 3),
    )

    s2ns = [10, 12.5, 15, 20]
    # run-riz-drcbWP-cells
    mlows = np.array(
        [0.000553132, -5.80659e-05, 0.000227885, -3.67881e-05]
    )/0.001
    mhighs = np.array(
        [0.0020267, 0.00131326, 0.00148068, 0.00113388]
    )/0.001

    ax.fill_between(
        s2ns,
        mlows,
        mhighs,
        color=FCOLOR,
        alpha=ALPHA,
        hatch=HATCHES[0],
        label='cells',
    )

    # add run-drcbWP here
    mlows = np.array(
        [-0.00052429, -0.000516172, -0.000374928, -0.000414037],
    )/0.001
    mhighs = np.array(
        [0.000572595, 0.000440756, 0.0005201, 0.000372421],
    )/0.001
    ax.fill_between(
        s2ns,
        mlows,
        mhighs,
        color=FCOLOR,
        alpha=ALPHA,
        hatch=HATCHES[1],
        label='no cells',
    )


    add_lines(ax)

    ax.text(
        10,
        -2,
        r'99.7\% confidence errors',
    )
    ax.legend()


def main():
    args = get_args()

    figsize = (WIDTH, 1.8 * WIDTH/1.618)

    fig, axs = mplt.subplots(nrows=2, figsize=figsize)

    do_s2n_bias_plot(axs[0])
    do_Tratio_bias_plot(axs[1])

    print('writing:', args.pdf)
    mplt.savefig(args.pdf)


main()
