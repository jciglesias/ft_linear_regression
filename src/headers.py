import numpy as np

thetafile = "theta.npy"
lrate = 0.1
epoch = 1000

def estimate_price(theta, milage) -> float:
    return theta[0] + theta[1] * milage

def normalize(milage: np.ndarray) -> np.ndarray:
    return (milage - milage.min()) / (milage.max()- milage.min())

def normalize_price(price: np.ndarray, milage: np.ndarray):
    m = (milage.size * np.sum(milage * price) - (np.sum(milage) * np.sum(price))) / (milage.size * np.sum(milage * milage) - (np.sum(milage) * np.sum(milage)))
    b = (np.sum(price) - m * np.sum(milage)) / milage.size
    return estimate_price([b, m], normalize(milage))