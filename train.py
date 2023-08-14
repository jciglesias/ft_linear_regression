# Used to train your model. It will read your dataset file
# and perform a linear regression on the data.
# Once the linear regression has completed, you will save the variables theta0 and
# theta1 for use in the first program.
from headers import thetafile
import csv
import numpy as np

if __name__=="__main__":
    x,y = [],[]
    with open('data.csv', newline='') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            x.append(int(row["km"]))
            y.append(int(row["price"]))
    np.save(thetafile, np.polyfit(x, y, 1))