import pickle
import os


class test_model:
    def __init__(self):
        pass
    def run(self, inputs: dict):
        # request = {'inputs': {
        #     'a': [1, 2, 3],
        #     'b': [100, 200, 300]
        # }}
        res = {}
        for key in inputs:
            res.update({key: [n * 2 for n in inputs[key]]})
        return res

def picked_model():
    path = os.path.abspath(os.path.join('.', 'test_truss', 'data', 'test_truss.pickle'))
    pickle.dump(test_model, open(path, "wb"))

if __name__ == '__main__':
    picked_model()