#https://www.thekerneltrip.com/statistics/random-forest-vs-svm/

import numpy as np
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, AdaBoostClassifier
from sklearn.svm import SVR, SVC
from sklearn.neighbors import KNeighborsClassifier  
from sklearn.linear_model import LogisticRegression
from DecisionBoundaryPlotter import DecisionBoundaryPlotter


def random_data_classification(n, p, f):
    predictors = np.random.rand(n, p)
    return predictors, np.apply_along_axis(f, 1, predictors)


def parabolic(x, y):
    return (x**2 + y**3 > 0.5) * 1


def parabolic_mat(x):
    return parabolic(x[0], x[1])


X, Y = random_data_classification(100, 2, parabolic_mat)

dbp = DecisionBoundaryPlotter(X, Y)

named_classifiers = [(RandomForestClassifier(), "RandomForestClassifier"),
                     (SVC(probability=True), "SVC")]

for named_classifier in named_classifiers:
    print(named_classifier[1])
    dbp.PlotContour(named_classifier[0], named_classifier[1])
    dbp.PlotHeatmap(named_classifier[0], named_classifier[1])