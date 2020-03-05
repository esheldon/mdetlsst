import numpy as np
from glob import glob
from pyx import *


def get_m(fname):

    density_cut = float(fname.split('-')[-1].replace('cut', ''))
    with open(fname) as fobj:
        for line in fobj:
            if 'm1:' in line:
                ls = line.split()
                m = float(ls[1])
                merr = float(ls[3])/3

    return density_cut, m, merr


flist = glob('doshear.yaml.wqlog.test01-cut*')
flist.sort()

density_cut = []
m = []
merr = []
for f in flist:
    tdcut, tm, tmerr = get_m(f)

    density_cut.append(tdcut)
    m.append(tm)
    merr.append(tmerr)

c = canvas.canvas()


xmin = 0
xmax = 110

gbot = c.insert(
    graph.graphxy(
        width=8,
        x=graph.axis.linear(min=xmin, max=xmax, title='Stellar Density Cut [per sq arcmin]'),
        y=graph.axis.linear(min=0.9, max=1.5, density=1.5, title='$\sigma_m/\sigma_m^{100}$'),
    )
)
gbot.plot(graph.data.function('y(x)=1'))

merr = np.array(merr)
merr_rat = merr/merr[-1]

gbot.plot(
    graph.data.values(x=density_cut, y=list(merr_rat)),
    [
        graph.style.line(lineattrs=[color.rgb.blue,  style.linewidth.Thin, style.linestyle.solid]),
        graph.style.symbol(symbol=graph.style.symbol.circle,
                           size=0.1,
                           symbolattrs=[deco.filled([color.rgb.blue])]),
    ],

)


tg = graph.graphxy(
    width=8,
    ypos=gbot.height+0.5,
    x=graph.axis.linkedaxis(gbot.axes["x"]),
    y=graph.axis.linear(min=-0.0075, max=0.0075, title='$m$', density=2),
    key=graph.key.key(pos="br", dist=0.1),
)

gtop = c.insert(tg)


"""
x1,y1 = gtop.pos(xmin, 0.001)
x2,y2 = gtop.pos(xmax, -0.001)

gtop.stroke(path.rect(x1,y1,x2-x1,y2-y1),[deco.filled([color.gray(0.8)])
])
"""

lattr = [
    graph.style.line(
        lineattrs=[
            # color.gray(0.4),
            color.rgb(r=0, g=100/255, b=0),
            # style.linewidth.Thin,
            style.linestyle.solid,
        ],
    ),
]

gtop.plot(graph.data.function('y(x)=0', title=None))
gtop.plot(graph.data.function("y(x)=0.001", title=None), lattr)
gtop.plot(graph.data.function("y(x)=-0.001", title=None), lattr)

gtop.plot(graph.data.function("y(x)=0.0005*sqrt(x)", title=r'$0.0005*\sqrt{dmax}$'))

gtop.plot(
    graph.data.values(x=density_cut, y=m, dy=merr, title='data'),
    [
        # graph.style.line(lineattrs=[color.rgb.blue,  style.linewidth.Thin, style.linestyle.solid]),
        graph.style.symbol(symbol=graph.style.symbol.circle,
                           size=0.1,
                           symbolattrs=[deco.filled([color.rgb.blue])]),
        graph.style.errorbar(errorbarattrs=[color.rgb.blue]),
    ],
)

"""
gtop.dolayout()

x1,y1 = gtop.pos(xmin, 0.001)
x2,y2 = gtop.pos(xmax, -0.001)

gtop.stroke(path.rect(x1,y1,x2-x1,y2-y1),[deco.filled([color.gray(0.8)]) ])
"""

c.writeGSfile("stardens-bias.png", resolution=150)
c.writePDFfile("stardens-bias.pdf")
