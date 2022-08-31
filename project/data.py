import abc
import os
from glob import glob

import numpy as np
from PIL import Image

CONF = {
    "DIR":{"TRAIN":"./data/train", "TEST":"./data/test"},
    "DATA_OPTS":{"VALID":True, "RATE":0.3}
}
CLASS = {"dog":"cat"}

class DataLoader(metaclass=abc.ABCMeta):
    def __init__(self, conf):
        pass

    @abc.abstractclassmethod
    def load_data(self):
        pass


class TrainDataLoader(DataLoader):
    def __init__(self, conf):
        pass

    