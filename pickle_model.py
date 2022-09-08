import pickle
import os
from test_model import TestModel

def picked_model():
    test_model = TestModel()
    path = os.path.abspath(os.path.join('', 'test_truss/data', 'test_truss.pickle'))
    pickle.dump(test_model, open(path, "wb"))

if __name__ == '__main__':
    picked_model()
