

class TestModel:
    def __init__(self):
        pass
    def run(self, inputs: dict):
        # {
        #     'a': [1, 2, 3],
        #     'b': [100, 200, 300]
        # }
        res = {}
        for key in inputs:
            res.update({key: [n * 2 for n in inputs[key]]})
        return res