"""Used to train your model. It will read your dataset file
and perform a linear regression on the data.
Once the linear regression has completed, you will save the variables theta0 and
theta1 for use in the first program."""

from headers import thetafile, lrate, estimate_price
from matplotlib import pyplot
import csv
import numpy as np


def normalize(milage: np.ndarray) -> np.ndarray:
    return (milage - milage.min()) / (milage.max()- milage.min())

def pred_error(theta, milage, price) -> float:
    return estimate_price(theta, milage) - price

def get_theta(theta, milage: np.ndarray, price, size) -> list:
    # if size > 1:
    #     theta = get_theta(theta, milage, price, size - 1)
    # theta[0] -= lrate * np.sum(pred_error(theta, milage[:size], price[:size])) / size
    # theta[1] -= lrate * np.sum(pred_error(theta, milage[:size], price[:size]) * milage[:size]) / size
    for i in range(1,size + 1):
        theta[0] -= lrate * np.sum(pred_error(theta, milage[i:i+size], price[i:i+size])) / i
        theta[1] -= lrate * np.sum(pred_error(theta, milage[i:i+size], price[i:i+size]) * milage[i:i+size]) / i
    return theta

if __name__=="__main__":
    milage, price = [],[]
    theta = [0,0]
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.DictReader(csvfile)
        # spamreader = sorted(spamreader, key=lambda x: float(x['km']))
        for row in spamreader:
            milage.append(int(row["km"]))
            price.append(int(row["price"]))
    for _ in range(1000):
        theta = get_theta(theta, normalize(np.array(milage)), np.array(price), len(milage))
    # theta[1] = (size * sum([milage[i] * price[i] for i in range(size)]) - (sum(milage) * sum(price))) / (size * sum([milage[i] * milage[i] for i in range(size)]) - (sum(milage) * sum(milage)))
    # theta[0] = (sum(price) - theta[1] * sum(milage)) / size
    print(theta)
    pyplot.scatter(milage, price)
    pyplot.plot(milage, estimate_price(theta, np.array(milage)))
    pyplot.show()
    np.save(thetafile, theta)