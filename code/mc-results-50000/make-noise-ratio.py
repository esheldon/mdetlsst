

def read_one(fname):

    with open(fname) as fobj:
        for line in fobj:
            if 'm1:' in line:
                ls = line.split()

                m = float(ls[1])
                merr = float(ls[3])/3.0

    return m, merr


def main():

    # for dcut in [40]:
    for dcut in [5, 10, 20, 40, 60, 80, 100]:
        outfile = 'noise-ratio-dcut%03d.txt' % dcut

        print(outfile)
        with open(outfile, 'w') as fobj:

            for s2n_cut in [10, 15, 20, 25, 30]:
                fname = 'mc-expand-notrim-50000-s2n%02d' % s2n_cut
                fname_stars = (
                    'mc-expand-notrim-psf-dims-50000-s2n%02d-cut%03d' % (s2n_cut, dcut)
                )
                # print(s2n_cut, fname, fname_stars)

                m, merr = read_one(fname)
                ms, mserr = read_one(fname_stars)

                rat = mserr/merr

                print(s2n_cut, rat, file=fobj)


main()
