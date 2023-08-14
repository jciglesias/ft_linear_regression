# Used to train your model. It will read your dataset file
# and perform a linear regression on the data.
# Once the linear regression has completed, you will save the variables theta0 and
# theta1 for use in the first program.
from headers import thetafile, lrate
import csv
import numpy as np

def estimate_price(theta, milage) -> float:
    return theta[0] + theta[1] * milage

def get_theta(theta, milage, price, pos) -> []:
    if pos == 0:
        theta[0] = lrate * estimate_price(theta, milage[pos]) - price[pos]
        theta[1] = lrate * (estimate_price(theta, milage[pos]) - price[pos]) * milage[pos]
        return theta
    theta = get_theta(theta, milage, price, pos - 1)
    theta[0] = lrate * np.sum([estimate_price(theta, milage[i]) - price[i] for i in range(pos + 1)]) / (pos + 1)
    theta[1] = lrate * np.sum([(estimate_price(theta, milage[i]) - price[i]) * milage[i] for i in range(pos + 1)]) / (pos + 1)
    return theta

if __name__=="__main__":
    milage, price = [],[]
    size = 0
    theta = [0,0]
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            milage.append(int(row["km"]))
            price.append(int(row["price"]))
            size += 1
    np.save(thetafile, np.polyfit(milage, price, 1))
    # theta = get_theta(theta, milage, price, size - 1)
    # np.save(thetafile, theta)