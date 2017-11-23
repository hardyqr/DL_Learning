# Freddy/Fangyu
# 12/14/2016


"""Softmax."""

scores = [3.0, 1.0, 0.2]

import numpy as np

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    s=0
    for num in x:
        s+=np.exp(num)
    aws=[]
    for num in x:
        aws.append(np.exp(num)/s)
    return np.array(aws)



print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])
print(scores)
plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()
