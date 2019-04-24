from CNN.CNN import CNN
import numpy as np
import pickle

CHANNEL_NUM = 5


class Discriminator(CNN):

    def __init__(self, isTraining=True):
        super(Discriminator, self).__init__(isTraining)

    def buildNetwork(self):
        self.addConvLayer(np.random.rand(8, 7, 7, CHANNEL_NUM), 0.01)
        self.addReluLayer()
        self.addConvLayer(np.random.rand(4, 7, 7, CHANNEL_NUM), 0.01)
        self.addReluLayer()
        self.addPoolingLayer()
        self.addConvLayer(np.random.rand(2, 7, 7, CHANNEL_NUM), 0.01)
        self.addReluLayer()
        self.addPoolingLayer()
        self.addFullyConnectedLayer(np.random.rand(98), 0.01)
        # do that again

        # self.addFullyconnectedLayer(classes = 2) # is / isn't generated music

    def dump_model(self, filename):
        """Dumps the model to filename.
        """
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load_model(filename):
        """Loads a previously trained (hopefully) model from filename.
           Returns it.
        """
        with open(filename, "rb") as f:
            return pickle.load(f)