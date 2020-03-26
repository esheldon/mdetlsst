import numpy as np
from glob import glob
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--s2n-cut', type=int)
    return parser.parse_args()


def read_one(fname):

    density_cut = float(fname.split('-')[-1].replace('cut', ''))
    with open(fname) as fobj:
        for line in fobj:
            if 'm1:' in line:
                ls = line.split()
                m = float(ls[1])/0.001
                merr = float(ls[3])/0.001/3

    return density_cut, m, merr

def main():

    args = get_args()

    if args.s2n_cut is not None:
        flist = glob('mc-s2n%02d*' % args.s2n_cut)
    else:
        flist = glob('mc-cut*')

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


main()
