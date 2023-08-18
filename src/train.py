"""Used to train your model. It will read your dataset file
and perform a linear regression on the data.
Once the linear regression has completed, you will save the variables theta0 and
theta1 for use in the first program."""

from headers import thetafile, lrate, estimate_price
from matplotlib import pyplot
import csv
import numpy as np


def normalize(milage: np.ndarray, pos) -> float:
    return (milage[pos] - milage.min()) / (milage.max()- milage.min())

def get_theta(theta, milage: np.ndarray, price, pos) -> list:
    if pos > 0:
        theta = get_theta(theta, milage, price, pos - 1)
    theta[0] += estimate_price([0,0], normalize(milage, pos)) - price[pos]
    theta[1] += (estimate_price([0,0], normalize(milage, pos)) - price[pos]) * normalize(milage, pos)

    # for i in range(milage.size):
    #     theta[0] += estimate_price(theta, normalize(milage, i)) - price[i]
    #     theta[1] += (estimate_price(theta, normalize(milage, i)) - price[i]) * normalize(milage, i)
    return theta

if __name__=="__main__":
    milage, price = [],[]
    size = 0
    theta = [0,0]
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.DictReader(csvfile)
        spamreader = sorted(spamreader, key=lambda x: float(x['km']))
        for row in spamreader:
            milage.append(int(row["km"]))
            price.append(int(row["price"]))
            # tmp[0] += estimate_price(theta, milage[size]) - price[size]
            # tmp[1] += (estimate_price(theta, milage[size]) - price[size]) * milage[size]
            size += 1
    # theta[1], theta[0] =  np.polyfit(milage, price, 1)
    tmp = get_theta([0, 0], np.array(milage), np.array(price), size - 1)
    theta[0] -= lrate * tmp[0] / size
    theta[1] -= lrate * tmp[1] / size
    # theta[1] = (size * sum([milage[i] * price[i] for i in range(size)]) - (sum(milage) * sum(price))) / (size * sum([milage[i] * milage[i] for i in range(size)]) - (sum(milage) * sum(milage)))
    # theta[0] = (sum(price) - theta[1] * sum(milage)) / size
    print(theta)
    pyplot.scatter(milage, price)
    pyplot.plot(milage, [theta[0] + theta[1] * x for x in milage])
    pyplot.show()
    np.save(thetafile, theta)