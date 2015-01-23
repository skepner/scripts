#! /usr/bin/env python

print 'MPG -> L'
for mpg in range(1, 101):
    print '%3d    %3.1f' % (mpg, 235.22 / float(mpg))

print 'F -> C'
for f in range(-50, 150):
    print '%3d    %3.1f' % (f, float(f - 32) * 5.0 / 9.0)
