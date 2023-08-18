thetafile = "theta.npy"
lrate = 0.1
epoch = 1000

def estimate_price(theta, milage) -> float:
    return theta[0] + theta[1] * milage