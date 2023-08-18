"""Used to train your model. It will read your dataset file
and perform a linear regression on the data.
Once the linear regression has completed, you will save the variables theta0 and
theta1 for use in the first program."""

from headers import *
from matplotlib import pyplot
import csv
import numpy as np

def pred_error(theta, milage, price) -> float:
    return estimate_price(theta, milage) - price

def get_theta(theta, milage: np.ndarray, price: np.ndarray, size: int) -> list:
    tmp = theta
    for i in range(size):
        tmp[0] -= lrate * np.sum(pred_error(theta, milage[:i + 1], price[:i + 1])) / size
        tmp[1] -= lrate * np.sum(pred_error(theta, milage[:i + 1], price[:i + 1]) * milage[:i + 1]) / size
    return tmp

if __name__=="__main__":
    milage, price = [],[]
    theta = [0,0]
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            milage.append(int(row["km"]))
            price.append(int(row["price"]))
    milage = np.array(milage)
    price = np.array(price)
    for _ in range(epoch):
        theta = get_theta(theta, normalize(milage), normalize_price(price, milage), milage.size)
    pyplot.scatter(milage, price)
    pyplot.plot(milage, estimate_price(theta, milage), color="green")
    pyplot.show()
    np.save(thetafile, theta)