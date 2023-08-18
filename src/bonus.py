from matplotlib import pyplot
import numpy as np
from headers import *
import csv

if __name__=="__main__":
    theta = [0,0]
    try:
        theta = np.load(thetafile)
    except Exception as e:
        print("The program has not been trained please run `python3 train.py` first")
    price, milage = [], []
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            milage.append(int(row["km"]))
            price.append(int(row["price"]))
    milage = np.array(milage)
    price = np.array(price)
    r2 = 1 - (np.sum((price - estimate_price(theta, milage))**2) / np.sum(((price - price.mean()))**2))
    print(f"Precision = {r2 * 100:.2f}%")
    pyplot.scatter(milage, price)
    pyplot.plot(milage, estimate_price(theta, milage), color="g")
    pyplot.show()