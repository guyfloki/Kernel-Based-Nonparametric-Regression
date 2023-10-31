import numpy as np

def generate_sinusoidal_data(num_points=100, noise_std=0.1):
    x = np.linspace(0, 2*np.pi, num_points)
    y = np.sin(x) + np.random.normal(0, noise_std, num_points)
    return x, y


