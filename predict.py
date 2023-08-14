# Predict the price of a car for a given mileage.
# When you launch the program, it should prompt you for a mileage, and then give
# you back the estimated price for that mileage.
# 
# Before the run of the training program, theta0 and theta1 will be set to 0
import numpy as np
from headers import thetafile
import sys

if __name__=="__main__":
    theta = [0,0]
    try:
        theta = np.load(thetafile)
    except Exception as e:
        print("The program has not been trained please run `python3 train.py` first")
    miles = input("Enter milage:\n")
    try:
        print(f"Estimated price is {theta[1] + theta[0] * int(miles):.2f}")
    except Exception:
        print("Please enter a valid number")