from matplotlib import pyplot
import math

def f1(x):
    return x**2
def f2(x):
    return x**3
x = range(-10, 15)
pyplot.plot(x, [f1(i) for i in x])
pyplot.plot(x, [f2(i) for i in x])
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")
pyplot.xlim(-5, 5)
pyplot.ylim(-5, 5)
pyplot.savefig("output.png")
pyplot.show()