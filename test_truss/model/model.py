import os.path
from typing import Dict, List
import pickle

# This works in truss because packages directory is added to the path
# it will however show as incorrect in pycharm
from test_model import TestModel


class Model:
    def __init__(self, **kwargs) -> None:
        self._data_dir = kwargs["data_dir"]
        self._config = kwargs["config"]
        self._model = None

    def load(self):
        # Load model here and assign to self._model.
        path = self._data_dir / 'test_truss.pickle'
        self.model = pickle.load(open(path, "rb"))

    def preprocess(self, request: Dict) -> Dict:
        """
        Incorporate pre-processing required by the model if desired here.

        These might be feature transformations that are tightly coupled to the model.
        """
        return request

    def postprocess(self, request: Dict) -> Dict:
        """
        Incorporate post-processing required by the model if desired here.
        """
        return request

    def predict(self, request: Dict) -> Dict[str, List]:
        # request = {'inputs': [{
        #     'a': [1, 2, 3],
        #     'b': [100, 200, 300]
        # }]}
        response = {}
        inputs = request["inputs"]  # noqa
        # Invoke model and calculate predictions here.
        predictions = []
        for input in inputs:
            predictions.append(self.model.run(input))

        response["predictions"] = predictions
        return response

