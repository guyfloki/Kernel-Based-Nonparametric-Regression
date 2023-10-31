
import unittest
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from estimators import *
from data import *
from plotting import *

class TestNonparametricRegressionsWithSinusoidalData(unittest.TestCase):

    def setUp(self):
        self.sample_x, self.sample_y = generate_sinusoidal_data(num_points=30)
        self.true_x = np.linspace(0, 2*np.pi, 400)
        self.true_y = np.sin(self.true_x)
        self.bandwidth = 0.5

    def test_all_estimators(self):
        gm_estimations = [gasser_muller(x, self.sample_x, self.sample_y, self.bandwidth) for x in self.true_x]
        nw_estimations = [nadaraya_watson(x, self.sample_x, self.sample_y, self.bandwidth) for x in self.true_x]
        pc_estimations = [priestley_chao(x, self.sample_x, self.sample_y, self.bandwidth) for x in self.true_x]
        
        all_estimations = [gm_estimations, nw_estimations, pc_estimations]
        labels = ["Gasser-Muller", "Nadaraya-Watson", "Priestley-Chao"]
        
        plot_estimations(self.true_x, self.true_y, self.sample_x, self.sample_y, all_estimations, labels)
