import numpy
import talib
from numpy import genfromtxt
my_data = genfromtxt('15_minutes.csv', delimiter=',')
data = my_data[:, 4]

# close = numpy.random.random(100)
# output = talib.SMA(close, timeperiod=10)
real = talib.RSI(data, timeperiod=14)
print(real)