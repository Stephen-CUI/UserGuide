"""
@File  : Density Estimation for a Gaussian mixture.py
@Author: Stephen CUI
@Time  : 2024-04-08 11:01:16
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

from sklearn import mixture

n_samples = 300

np.random.seed(0)

# generate spherical data centered on (20, 20)
shifted_gaussian = np.random.randn(n_samples, 2) + np.array([20, 20])

C = np.array([[0.0, -0.7], [3.5, 0.7]])
stretched_gaussian = np.dot(np.random.randn(n_samples, 2), C)
X_train = np.vstack([shifted_gaussian, stretched_gaussian])

clf = mixture.GaussianMixture(n_components=2, covariance_type="full")
clf.fit(X_train)

x = np.linspace(-20, 30)
y = np.linspace(-20, 40)
X, Y = np.meshgrid(x, y)

XX = np.array([X.ravel(), Y.ravel()]).T
Z = -clf.score_samples(XX)
Z = Z.reshape(X.shape)

CS = plt.contour(
    X, Y, Z, norm=LogNorm(vmin=1.0, vmax=1000.0), levels=np.logspace(0, 3, 10)
)
CB = plt.colorbar(CS, shrink=0.8, extend="both")
plt.scatter(X_train[:, 0], X_train[:, 1], 0.8)
plt.title("Negative log-likelihood predicted by a GMM")
plt.axis("tight")
plt.show()
