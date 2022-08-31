from tensorflow.keras import Model
from tensorflow.keras.layers import BatchNormalization, Conv2D, Dense, Dropout, GlobalAveragePooling2D, Layer, MaxPool2D, ReLU

class ResidualBlock(Layer):
    def __init__(self, **kwargs):
        super(ResidualBlock, self).__init__(**kwargs)
        self.conv1 = Conv2D()
        self.batch_nor1 = BatchNormalization()
        self.acti = ReLU()
        self.conv1 = Conv2D()
        self.batch_nor2 = BatchNormalization()
        self.out = ReLU()

    def call(self, inputs):
        conv1 = self.conv1(inputs)
        batch_nor1 = self.batch_nor1(conv1)
        conv2 = self.conv1(batch_nor1)
        batch_nor2 = self.batch_nor1(conv2)
        return self.relu([conv1, batch_nor2])


class RESNET50(Layer):
    def __init__(self, output_dim, **kwargs):
        super(RESNET50, self).__init__(**kwargs)
        self.output_dim = output_dim
        self.hidden=[
            ResidualBlock([]),
            ResidualBlock([]),
            ResidualBlock([]),
            ResidualBlock([]),
            GlobalAveragePooling2D()

        ]
        self.out = Dense(output_dim)

    def call(self, inputs):
        pass
        

       
        
