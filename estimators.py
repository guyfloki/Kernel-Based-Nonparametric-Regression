import numpy as np
from scipy import integrate


def gaussian(u):
    return (1/np.sqrt(2*np.pi)) * np.exp(-0.5 * u**2)

def gasser_muller(x, data_x, data_y, bandwidth):
    n = len(data_x)
    estimator_value = 0
    for i in range(1, n):
        s_i_minus_1 = (data_x[i-1] + data_x[i]) / 2
        s_i = (data_x[i] + (data_x[i+1] if i < n-1 else data_x[i])) / 2
        integral, _ = integrate.quad(lambda u: gaussian((x-u)/bandwidth), s_i_minus_1, s_i)
        estimator_value += integral * data_y[i]
    return (1/bandwidth) * estimator_value

def nadaraya_watson(x, data_x, data_y, bandwidth):
    num = sum(data_y[i] * gaussian((x - data_x[i]) / bandwidth) for i in range(len(data_x)))
    den = sum(gaussian((x - data_x[i]) / bandwidth) for i in range(len(data_x)))
    return num / den if den != 0 else 0

def priestley_chao(x, data_x, data_y, bandwidth):
    n = len(data_x)
    estimator_value = 0
    for i in range(1, n):
        estimator_value += (data_x[i] - data_x[i-1]) * gaussian((x - data_x[i]) / bandwidth) * data_y[i]
    return (1/bandwidth) * estimator_value

