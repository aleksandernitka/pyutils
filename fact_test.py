
import datetime as dt
import math
import statistics as st

t = list()

print('\n-------------\n')

for i in range(0,10):
    start = dt.datetime.now()
    math.factorial(1000000)
    end = dt.datetime.now()
    delta = end-start
    t.append(delta.total_seconds())
    print(delta)

print('\n-------------\n')

print('Mean time to compute = {} seconds, SD = {}\n'.format(st.fmean(t), st.stdev(t)))