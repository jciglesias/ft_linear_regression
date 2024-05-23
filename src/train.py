"""Used to train your model. It will read your dataset file
and perform a linear regression on the data.
Once the linear regression has completed, you will save the variables theta0 and
theta1 for use in the first program."""

from headers import *
from matplotlib import pyplot, animation
from copy import copy
import csv, random
import numpy as np

def pred_error(theta, milage, price) -> float:
    return estimate_price(theta, milage) - price

def get_theta(theta, milage: np.ndarray, price: np.ndarray, size: int) -> list:
    tmp = copy(theta)
    for i in range(size):
        tmp[0] -= lrate * np.sum(pred_error(theta, milage[:i + 1], price[:i + 1])) / size
        tmp[1] -= lrate * np.sum(pred_error(theta, milage[:i + 1], price[:i + 1]) * milage[:i + 1]) / size
    return tmp

def animate(i):
    pyplot.clf()
    pyplot.scatter(milage, price)
    pyplot.plot(milage, estimate_price(theta[i], milage), color="g")
    pyplot.title(f"Epoch: {i}")
    return []

if __name__=="__main__":
    milage, price = [],[]
    theta = [[random.uniform(-1, 1),random.uniform(-1, 1)]]
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            milage.append(int(row["km"]))
            price.append(int(row["price"]))
    milage = np.array(milage)
    price = np.array(price)
    fig, ax = pyplot.subplots()
    line, = ax.plot(milage, estimate_price(theta[0], milage))

    ax.scatter(milage, price)
    for i in range(epoch):
        theta.append(get_theta(theta[i], normalize(milage), normalize_price(price, milage), milage.size))
    print(theta[epoch - 1])
    anim = animation.FuncAnimation(fig, animate, frames=epoch, blit=True, repeat=False, interval=1)
    
    # ----- save animation as gif -------
    # anim.save('animation.gif', writer='imagemagick', fps=30)
    
    np.save(thetafile, theta[epoch - 1])
    pyplot.show()