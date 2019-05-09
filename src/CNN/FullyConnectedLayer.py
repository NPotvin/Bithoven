import numpy as np
from CNN.AbstractLayer import Layer
import CNN.utils as utils


class FullyConnectedLayer(Layer):

    def __init__(self, weights, learningRate, act_f=utils.reLu, isLearning=True):
        super(FullyConnectedLayer, self).__init__(isLearning)
        self._act_f = act_f  # activation function
        self._weights = weights
        self._learningRate = learningRate

    @staticmethod
    def connect(vector, weights, act_f):
        """
        Does the dot product between the input vector and the filter.
        input vector is a   1 x k vector
        weights are         k x m matrix
        result is a         1 x m array
        """
        node = np.dot(vector, weights)
        result = act_f(node)
        return (node, result)

    def squaredError(prediction, actual):
        return 1/2 * np.square(prediction - actual)

    @staticmethod
    def learnFullyConnected(loss, previousLayer, alpha, weights, learningRate, act_f):
        """
        previousLayer : input value received at last forward pass
        alpha : output value at last forward pass, before activation
        weights : current weights matrix
        """
        df = act_f(alpha, derivative=True)
<<<<<<< HEAD
        weightsCorrection = np.matmul(previousLayer, df * loss)
        previousLayerLoss = np.matmul(weights, df * loss)
=======

        weightsCorrection = np.matmul(previousLayer.reshape(-1, 1), df * loss)
        previousLayerLoss = np.matmul(weights, (df * loss).reshape(-1, 1))
>>>>>>> e6e8c70d453ab68998b47cd68d11a69470909a90
        weights -= learningRate * weightsCorrection

        return previousLayerLoss, weights

    def compute(self, tensor):
        """
        basic computation function, calls the main function
        """
<<<<<<< HEAD
        vector = tensor.flatten()
        alpha, res = FullyConnectedLayer.connect(vector, self._weights, self._act_f)
=======
        vector = tensor.reshape(1, -1)
        node, res = FullyConnectedLayer.connect(vector, self._weights, self._act_f)
>>>>>>> e6e8c70d453ab68998b47cd68d11a69470909a90
        # saves last input and intermediate results
        self.saveData((tensor, alpha))
        return res

    def learn(self, loss):
        """
        basic learning method, sets some parameters and calls the main function
        """
        previousLayer, alpha = self.getSavedData()
        previousLayerLoss, self._weights = FullyConnectedLayer.learnFullyConnected(loss, previousLayer, alpha, self._weights, self._learningRate, self._act_f)
        return previousLayerLoss.reshape(previousLayer.shape)
