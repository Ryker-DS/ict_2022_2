from tensorflow.keras import Model
from tensorflow.keras.layers import Conv2D, Dense, Flatten, MaxPool2D

class Stem:
    def __init__(self):
        pass
    
    def call(self, inputs):
        conv_7 = Conv2D()(inputs)
        max_pool_1 = MaxPool2D()(conv_7)
        conv_1 = Conv2D()(max_pool_1)
        conv_3 = Conv2D()(conv_1)
        return MaxPool2D()(conv_3)

class InceptionModule:
    def __init__(self):
        pass

    def path_1(self, inputs):
        conv_1 = Conv2D()(inputs)
        conv_5 = Conv2D()(conv_1)
        return conv_5

    def path_2(self, inputs):
        conv_1 = Conv2D()(inputs)
        conv_3 = Conv2D()(conv_1)
        return conv_3

    def path_3(self, inputs):
        max_pool = MaxPool2D()(inputs)
        conv_1 = Conv2D()(max_pool)
        return conv_1

    def path_4(self, inputs):
        conv_1 = Conv2D()(inputs)
        return conv_1

    def concat(self, paths):
        x = [paths]
        return x

    def call(self, inputs):
        paths = (
            self.path_1(inputs),
            self.path_2(inputs),
            self.path_3(inputs),
            self.path_4(inputs),
        )

        return self.concat(paths)

class InceptionModule:
    def __init__(self):
        pass

    def call(self, inputs):
        out_level_1 = None
        out_level_2 = None
        out_level_3 = None

        return out_level_1, out_level_2, out_level_3