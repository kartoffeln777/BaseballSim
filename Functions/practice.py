from pylab import *

# Generate some random data...
x = linspace(55478, 55486, 100)
y = random(100) - 0.5
y = cumsum(y)
y -= y.min()
y *= 1e-8

# plot
plot(x,y)

# xticks
locs,labels = xticks()
print locs
print labels
xticks(locs, map(lambda x: "%g" % x, locs))

# ytikcs
locs,labels = yticks()
yticks(locs, map(lambda x: "%.1f" % x, locs*1e9))
ylabel('microseconds (1E-9)')

show()

