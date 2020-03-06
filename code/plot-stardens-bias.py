import numpy as np
from glob import glob
import biggles


def get_m(fname):

    density_cut = float(fname.split('-')[-1].replace('cut', ''))
    with open(fname) as fobj:
        for line in fobj:
            if 'm1:' in line:
                ls = line.split()
                m = float(ls[1])
                merr = float(ls[3])/3

    return density_cut, m, merr


flist = glob('mc-*')
flist.sort()

density_cut = []
m = []
merr = []
for f in flist:
    tdcut, tm, tmerr = get_m(f)

    density_cut.append(tdcut)
    m.append(tm)
    merr.append(tmerr)

m = np.array(m)
merr = np.array(merr)
merr_rat = merr/merr[-1]

xmin = 0
xmax = 110
arr = biggles.FramedArray(
    2, 1,
    xlabel='Stellar Density Cut [#/sq arcmin]',
    cellspacing=3,
    aspect_ratio=1.2,
    xrange=[xmin, xmax], 
)



sx = [xmin, xmax]
high = [0.001]*2
low = [-0.001]*2

shaded = biggles.FillBetween(sx, low, sx, high)
zl = biggles.LineY(0)
pts = biggles.Points(density_cut, m, type='filled circle', color='blue')
perr = biggles.SymmetricErrorBarsY(density_cut, m, merr, color='blue')
curve = biggles.Curve(density_cut, m, type='filled circle', color='blue')

arr[0, 0].ylabel = 'm'
arr[0, 0].yrange=[-0.002, 0.007]
arr[0, 0] += shaded, zl, pts, perr, curve


onel = biggles.LineY(1)
pts = biggles.Points(density_cut, merr_rat, type='filled circle', color='blue')
curve = biggles.Curve(density_cut, merr_rat, type='filled circle', color='blue')

arr[1, 0].ylabel = r'$\sigma_m/\sigma_m^{100}$'
arr[1, 0].yrange = [0.9, 1.5]
arr[1, 0] += onel, pts, curve

arr.write('stardens-bias.pdf')
