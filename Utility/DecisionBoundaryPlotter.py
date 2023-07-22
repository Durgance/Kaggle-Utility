import numpy as np
import matplotlib.pyplot as plt


class DecisionBoundaryPlotter:

    def __init__(self, X, Y, xs=np.linspace(0, 1, 100),
                 ys=np.linspace(0, 1, 100)):
        self._X = X
        self._Y = Y
        self._xs = xs
        self._ys = ys

    def _predictor(self, model):
        model.fit(self._X, self._Y)
        return (lambda x: model.predict_proba(x.reshape(1,-1))[0, 0])

    def _evaluate_height(self, f):
        fun_map = np.empty((self._xs.size, self._ys.size))
        for i in range(self._xs.size):
            for j in range(self._ys.size):
                v = f(
                    np.array([self._xs[i], self._ys[j]]))
                fun_map[i, j] = v
        return fun_map

    def PlotHeatmap(self, model, name):
        f = self._predictor(model)
        fun_map = self._evaluate_height(f)

        fig = plt.figure()
        s = fig.add_subplot(1, 1, 1, xlabel='$x$', ylabel='$y$')
        im = s.imshow(
            fun_map,
            extent=(self._ys[0], self._ys[-1], self._xs[0], self._xs[-1]),
            origin='lower')
        fig.colorbar(im)
        fig.savefig(name + '_Heatmap.png')
    
    def PlotContour(self, model, name):
        f = self._predictor(model)
        fun_map = self._evaluate_height(f)

        fig = plt.figure()
        s = fig.add_subplot(1, 1, 1, xlabel='$x$', ylabel='$y$')
        s.contour(self._xs, self._ys, fun_map, levels = [0.5])
        s.scatter(self._X[:,0], self._X[:,1], c = self._Y)
        fig.savefig(name + '_Contour.png')