print(r'''
\begin{table}
\centering
\begin{threeparttable}
      \caption{
      nostack: the LSST DM stack was not used; d: dithers; r: rotations; c: cosmic rays;
      b: bad columns; R: realistic galaxy properties and noise; v: variable pixel scale
      and WCS shear; p: psf $g_2 = 0.02$; RIZ: $r, i$ and $z$ bands used; LD: large dithers;
      VP: spatially variable moffat PSF.
      }
 \label{tab:shearmeas}

  \begin{tabular}{lcc}
    \hline
    \noalign{\vskip 1mm}
    Simulation & m (99.7\% conf.) & c (99.7\% conf.) \\
     &  $[10^{-3}]$ & $[10^{-5}]$ \\
    \noalign{\vskip 1mm}
    \hline
    \noalign{\vskip 1mm}''')

with open('notes.txt') as fobj:
    for line in fobj:
        line = line.strip()

        if 'm1:' in line and 'om1:' not in line:
            # print(line)

            ls = line.split()

            desc = ls[0]

            mean = float(ls[2])/1.0e-3
            err3 = float(ls[4])/1.0e-3

            low = mean - err3
            high = mean + err3

            if 'drcbvp' in line or 'VP' in line:
                c2 = float(ls[8])/1.0e-5
                c2err3 = float(ls[10])/1.0e-5
                clow = c2 - c2err3
                chigh = c2 + c2err3
                c = '$%.1f < c_2 < %.1f$' % (clow, chigh)
            else:
                c = '-'

            print(r'        %s & %.1f $< m_1 <$ %.1f & %s\\' % (desc, low, high, c))
print(r'''
    \noalign{\vskip 1mm}
    \hline
  \end{tabular}

    \end{threeparttable}
\end{table}
''')
