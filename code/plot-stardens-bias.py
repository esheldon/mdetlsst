import os
from glob import glob
import numpy as np
import argparse
import fitsio
import proplot as pplt

# WIDTH = 3
WIDTH = 2.8
ASPECT = (1.618, 1)

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
COLORS = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
    '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
]


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('flist', nargs='+')
    parser.add_argument('--pdf', required=True)
    parser.add_argument(
        '--add-nostars', action='store_true', help='add nostar point'
    )
    return parser.parse_args()


def read_data(path, weighted, nocancel):

    if weighted:
        pattern = 'gweight-mc-weighted-s2n-*'
    else:
        pattern = 'mc-s2n-*'

    if nocancel:
        pattern = 'nocancel-' + pattern

    pattern = os.path.join(path, 'mc-results', pattern)

    flist = glob(pattern)
    flist.sort()
    data = {}
    for f in flist:
        tdata = fitsio.read(f)[0]

        s2n_min = tdata['s2n_min']
        sdens = tdata['max_star_density']
        Tratio_min = tdata['Tratio_min']

        key = f's2n-{s2n_min:.1f}-Tratio-{Tratio_min:.1f}'

        m1err = tdata['m1err'] * 3
        m1high = tdata['m1'] + m1err
        m1low = tdata['m1'] - m1err
        m1 = tdata['m1']

        if key in data:
            data[key]['sdens'].append(sdens)
            data[key]['m1high'].append(m1high)
            data[key]['m1low'].append(m1low)
            data[key]['m1'].append(m1)
            data[key]['m1err'].append(m1err)
        else:
            data[key] = {}
            data[key]['sdens'] = [sdens]
            data[key]['m1high'] = [m1high]
            data[key]['m1low'] = [m1low]
            data[key]['m1'] = [m1]
            data[key]['m1err'] = [m1err]

    fields = ['sdens', 'm1low', 'm1high', 'm1', 'm1err']
    offeach = 0.0
    for i, key in enumerate(data):
        for field in fields:
            data[key][field] = np.array(data[key][field])

        s = data[key]['sdens'].argsort()
        for field in fields:
            data[key][field] = data[key][field][s]

        data[key]['sdens'] += i * offeach

    return data


def key2label(key):
    ks = key.split('-')
    # import IPython; IPython.embed()
    ks = [
        r'S/N $>$',
        ks[1],
        # '$T/T_{PSF} > $',
        # ks[3],
    ]
    # if ks[0] == 'imfrac':
    #     ks = ks[2:]
    # if ks[0] == 's2n':
    #     ks[0] = r'S/N $>$'
    #     ks = ks[:2]
    return ' '.join(ks)


def do_error_plot(fname, data, wdata):

    alpha = 0.5
    fig = pplt.figure(refwidth=WIDTH, refaspect=ASPECT, spany=True)
    axs = fig.subplots(nrows=2, ncols=1, space=0)
    axs.format(
        abc=True, abcloc='ul',
        # abcbbox=True,
        xlabel='Maximum stellar density [per sq. arcmin]',
        ylabel=r'$\sigma(\gamma) / \sigma_{min}(\gamma)$',
        xlim=(-5, 110),
        ylim=(0.95, 1.55),
    )

    axs[0].axhline(1, color='black', lw=0.5)
    axs[1].axhline(1, color='black', lw=0.5)

    lw = 1
    for tdata, ax in zip((data, wdata), axs):
        errvals = []
        for key in tdata:
            mdata = tdata[key]
            errvals += list(mdata['m1err'])

        minval = min(errvals)
        for i, key in enumerate(sorted(tdata)):
            mdata = tdata[key]

            label = key2label(key)

            ax.plot(
                mdata['sdens'],
                mdata['m1err']/minval,
                linestyle=LINESTYLES[i],
                lw=lw,
                color=COLORS[i],
                marker=MARKERS[i],
                markeredgecolor='black',
                markersize=4,
                label=label,
                alpha=alpha,
            )

    axs[0].legend(ncol=1, pad=1)
    print('writing:', fname)
    fig.savefig(fname)


def do_bias_plot(fname, data, wdata):

    alpha = 0.3

    # figsize = (WIDTH, WIDTH/1.618)

    # fig, ax = mplt.subplots(nrows=2, figsize=figsize)
    fig = pplt.figure(refwidth=WIDTH, refaspect=ASPECT, spany=True)
    axs = fig.subplots(nrows=2, ncols=1, space=0)
    axs.format(
        abc=True, abcloc='ul',
        # abcbbox=True,
        xlabel='Maximum stellar density [per sq. arcmin]',
        ylabel='m / 0.001',
        xlim=(-5, 110),
        ylim=(-2.9, 3.9),
    )
    # ax.set(
    #     xlabel='maximum stellar density [per sq. arcmin]',
    #     ylabel='m / 0.001',
    #     ylim=(-2, 4),
    # )
    hatches = [
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
    lw = 1
    for tdata, ax in zip((data, wdata), axs):

        lim = 1
        # lcolor = 'seagreen'
        lcolor = 'sienna'
        ax.axhline(0, color='black', lw=0.5)
        ax.axhline(-lim, color=lcolor, linestyle='dashed', lw=lw)
        ax.axhline(+lim, color=lcolor, linestyle='dashed', lw=lw)

        ax.axhline(
            0.4, color='sand', lw=lw, alpha=0.5, linestyle='dashdot',
        )

        for i, key in enumerate(sorted(tdata)):
            mdata = tdata[key]

            label = key2label(key)

            ax.fill_between(
                mdata['sdens'],
                mdata['m1high'] / 0.001,
                mdata['m1low'] / 0.001,
                label=label,
                alpha=alpha,
                color='black',
                hatch=hatches[i],
            )

    axs[0].legend(ncol=2, pad=1)

    axs[0].text(
        # 5, 3,
        50, -2,
        r'99.7\% confidence range',
    )

    print('writing:', fname)
    fig.savefig(fname)


def main():
    # args = get_args()

    data = read_data(
        path='data/run-riz-drcbWsBPv0.1-cells-s2n-imfrac0.10-mfrac0.02',
        weighted=False, nocancel=False,
    )
    nc_data = read_data(
        path='data/run-riz-drcbWsBPv0.1-cells-s2n-imfrac0.10-mfrac0.02',
        weighted=False, nocancel=True,
    )
    wdata = read_data(
        path='data/run-riz-drcbWsBPv0.1-cells-s2n-imfrac0.10-mfrac0.02-weight',
        weighted=True, nocancel=False,
    )
    nc_wdata = read_data(
        path='data/run-riz-drcbWsBPv0.1-cells-s2n-imfrac0.10-mfrac0.02-weight',
        weighted=True, nocancel=True,
    )

    do_bias_plot('stardens-bias.pdf', data, wdata)
    do_error_plot('stardens-nocancel-error.pdf', nc_data, nc_wdata)


main()
