import numpy as np


class Model:
    def __init__(self):
        self.grads = None
        self.bias = None
        self.weights = None
        self.predictions = None
        self.target = None
        self.data = None
        self.n_features = None
        self.n_examples = None
        self.learning_rate = None
        self.params = dict()

    @property
    def user_data(self):
        return self.predictions

    @user_data.setter
    def user_data(self, data):
        self.learning_rate = data[0]
        self.data = data[1]
        self.target = data[2]
        self.n_examples, self.n_features = self.data.shape
        print("user data set")

    @property
    def model_data(self):
        self.params = {
            "weights": self.weights,
            "bias": self.bias,
            "learning_rate": self.learning_rate
        }
        return self.params

    @model_data.setter
    def model_data(self, data):
        self.weights = data[0]
        self.bias = data[1]
        self.learning_rate = data[2]
        print("model data set")

    @staticmethod
    def custom_sigmoid(activations):
        """
        calculate sigmoid of activations computed on input data

        Args:
            activations (float-numpy array): numpy array of activations(z) having dimensions of (no_of_examples x 1)

        Returns:
            float-numpy array: element wise sigmoid of the activations(z)  of input data

        """
        exponents = np.exp(-activations)
        sigmoids = 1 / (1 + exponents)
        return sigmoids

    @staticmethod
    def custom_softmax(probability):
        """
        covert probabilities into target categories of 0 and/or 1

        Args:
            probability (float- numpy array): numpy array of probabilities of target being 1 or 0

        Returns:
            numpy array: numpy array of 0 or 1 as predicted class of input examples

        """
        probability[probability >= 0.65] = 1
        probability[probability < 0.65] = 0
        predictions = probability.astype(int)
        return predictions

    @staticmethod
    def linear_forward(data, weights):
        linear_activations = np.dot(data, weights)
        return linear_activations

    def compute_cost(self):
        """
        calculate cost according to logistic regression formula

        Returns:
            object: self, model object

        """
        # print("predictions shape: ", self.predictions.shape)
        # print("target shape: ", self.target.shape)
        epsilon = 1e-5
        cost = np.sum(
            (self.target * np.log(self.predictions + epsilon))
            + ((1 - self.target) * np.log(1 - self.predictions + epsilon))
        )
        cost = -(1 / self.n_examples) * cost
        return cost
