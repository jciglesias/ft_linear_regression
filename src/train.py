"""Used to train your model. It will read your dataset file
and perform a linear regression on the data.
Once the linear regression has completed, you will save the variables theta0 and
theta1 for use in the first program."""

from headers import *
from matplotlib import pyplot
import csv
import numpy as np


def normalize(milage: np.ndarray) -> np.ndarray:
    return (milage - milage.min()) / (milage.max()- milage.min())

# def norm_ret(arg: np.ndarray):
#     return arg * (arg.max() - arg.min()) + arg.min()

def pred_error(theta, milage, price) -> float:
    return estimate_price(theta, milage) - price

def get_theta(theta, milage: np.ndarray, price: np.ndarray, size: int) -> list:
    tmp = theta
    tmp[0] -= lrate * np.sum(pred_error(theta, milage, price)) / size
    tmp[1] -= lrate * np.sum(pred_error(theta, milage, price) * milage) / size
    # print(tmp)
    return tmp

if __name__=="__main__":
    milage, price = [],[]
    theta = [0,0]
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.DictReader(csvfile)
        # spamreader = sorted(spamreader, key=lambda x: float(x['km']))
        for row in spamreader:
            milage.append(int(row["km"]))
            price.append(int(row["price"]))
    milage = np.array(milage)
    price = np.array(price)
    theta[1] = (milage.size * np.sum(milage * price) - (np.sum(milage) * np.sum(price))) / (milage.size * np.sum(milage * milage) - (np.sum(milage) * np.sum(milage)))
    theta[0] = (np.sum(price) - theta[1] * np.sum(milage)) / milage.size
    tmp = estimate_price(theta, normalize(milage))
    # theta = [0,0]
    for _ in range(epoch):
        theta = get_theta(theta, normalize(milage), tmp, milage.size)
    # theta[1] = (np.sum(price) - (theta[0] * milage.size)) / np.sum(milage)
    print(f"{theta[0]:.2f}, {theta[1]:.2f}")
    # pyplot.scatter(milage, price)
    # pyplot.plot(milage, estimate_price(theta, milage))
    # pyplot.show()
    np.save(thetafile, theta)