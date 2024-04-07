import numpy as np

s = [1,2,3,4,5]
median = np.median(s)
print(f"The median is: {median}")

mean = np.mean(s)
print(f"The mean is: {mean}")

s.sort()
q1=np.percentile(s,25)
q3=np.percentile(s,75)
print(f"Q1 is {q1}")
print(f"Q3 is {q3}")
iqr = q3-q1
print(f"The interquartile range is {iqr}")
