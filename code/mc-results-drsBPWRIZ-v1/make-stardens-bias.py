import numpy as np
from glob import glob


def read_one(fname):

    density_cut = float(fname.split('-')[-1].replace('cut', ''))
    with open(fname) as fobj:
        for line in fobj:
            ls = line.split()
            if 'm1err' in line:
                merr = float(ls[1])/0.001
            elif ' m1 ' in line:
                ls = line.split()
                mlow = float(ls[0])
                mhigh = float(ls[4])
                m = (mlow + mhigh)/2/0.001

    return density_cut, m, merr


def main():
    s2ns = [10, 15, 20, 25, 30]
    offs = [-2, -1, 0, 1, 2]
    for s2n_cut, off in zip(s2ns, offs):
        output = 'm-vs-star-density-s2n%02d.txt' % s2n_cut
        print(output)
        with open(output, 'w') as fobj:

            flist = glob(
                'mc-run-drsBPWRIZ-v1-s2n%02d-Tratio1.2-cut*' % s2n_cut
            )

            flist.sort()

            density_cut = []
            m = []
            merr = []
            for f in flist:
                tdcut, tm, tmerr = read_one(f)

                density_cut.append(tdcut + off)
                m.append(tm)
                merr.append(tmerr)

            density_cut = np.array(density_cut)
            m = np.array(m)
            merr = np.array(merr)

            for i in range(density_cut.size):
                print(density_cut[i], m[i], merr[i], file=fobj)


main()
