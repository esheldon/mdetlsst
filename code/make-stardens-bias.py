import numpy as np
from glob import glob

def read_one(fname):

    density_cut = float(fname.split('-')[-1].replace('cut', ''))
    with open(fname) as fobj:
        for line in fobj:
            if 'm1:' in line:
                ls = line.split()
                m = float(ls[1])/0.001
                merr = float(ls[3])/0.001/3

    return density_cut, m, merr


flist = glob('mc-*')
flist.sort()

density_cut = []
m = []
merr = []
for f in flist:
    tdcut, tm, tmerr = read_one(f)

    density_cut.append(tdcut)
    m.append(tm)
    merr.append(tmerr)

density_cut = np.array(density_cut)
m = np.array(m)
merr = np.array(merr)
merr_rat = merr/merr[-1]

for i in range(density_cut.size):
    print(density_cut[i], m[i], merr[i], merr_rat[i])

