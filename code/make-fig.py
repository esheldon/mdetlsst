import biggles

width = 3
# key = biggles.PlotKey(4, 0.1, halign='right')
plt = biggles.FramedPlot(
    # xlabel=r'$m$ 99.7% confidence range $[10^{-3}]$',
    xlabel=r'$m/10^{-3}$ 99.7% confidence range',
    xrange=[-3, 8],
    # key=key,
)
plt.y1.draw_ticks = False
plt.y1.draw_ticklabels = None
plt.y2.draw_ticks = False
plt.y2.draw_ticklabels = None

plt.add(biggles.LineX(0, color='darkgreen', width=width))
plt.add(biggles.LineX(-1, color='red', type='dashed', width=width))
plt.add(biggles.LineX(1, color='red', type='dashed', width=width))

with open('notes.txt') as fobj:
    descs = []
    mvals = []
    err3vals = []
    for line in fobj:
        line = line.strip()

        if 'm1:' in line and 'om1:' not in line:
            # print(line)

            ls = line.split()

            desc = ls[0]

            mean = float(ls[2])/1.0e-3
            err3 = float(ls[4])/1.0e-3

            mvals.append(mean)
            err3vals.append(err3)
            descs.append(desc)

            """
            if 'drcbvp' in line or 'VP' in line:
                c2 = float(ls[8])/1.0e-5
                c2err3 = float(ls[10])/1.0e-5
                clow = c2 - c2err3
                chigh = c2 + c2err3
                c = '$%.1f < c_2 < %.1f$' % (clow, chigh)
            else:
                c = '-'
            """


num = len(mvals)
print('found:', num)

start = 0.1
step = 0.9/num

labx = 7.5

for i in range(num):
    mval = mvals[i]
    err3val = err3vals[i]
    desc = descs[i]

    y = start + step*i
    err = biggles.SymmetricErrorBarsX(
        [mval],
        [y],
        [err3val],
        width=width,
        color='blue',
    )

    plt.add(err)

    text = biggles.DataLabel(labx, y, desc, halign='right')
    plt.add(text)

plt.write('mvals.pdf')
# plt.show()
