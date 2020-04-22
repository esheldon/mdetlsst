

def read_one(fname):

    with open(fname) as fobj:
        for line in fobj:
            if 'm1err:' in line:
                ls = line.split()

                merr = float(ls[1])/3.0

    return merr


def main():

    # for dcut in [40]:
    for dcut in [5, 10, 20, 40, 60, 80, 100]:
        outfile = 'noise-ratio-dcut%03d.txt' % dcut

        print(outfile)
        with open(outfile, 'w') as fobj:

            for s2n_cut in [10, 15, 20, 25, 30]:
                fname = 'mc-nocancel-nojack-run-drWRIZ-v2-s2n%02d-Tratio1.2' % s2n_cut
                fname_stars = (
                    'mc-nocancel-nojack-run-drsWRIZ-v3-s2n%02d-Tratio1.2-cut%03d' % (s2n_cut, dcut)
                )
                # print(s2n_cut, fname, fname_stars)

                merr = read_one(fname)
                mserr = read_one(fname_stars)

                rat = mserr/merr

                print(s2n_cut, rat, file=fobj)


main()
