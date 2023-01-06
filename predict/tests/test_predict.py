

import unittest
from unittest.mock import MagicMock
import tempfile
import pandas as pd
from predict.predict.run import TextPredictionModel

import os
import json

class TestPredict(unittest.TestCase):
    def test_predict(self):
        model = TextPredictionModel.from_artefacts("train/data/artefacts/2023-01-05-18-53-32")
        
        predictions = model.predict([
            "Is it possible to execute the procedure of a function in the scope of the caller?",
            "Hi I'm steve"
            ], top_k = 2)

        # assert that accuracy is equal to 1.0
        self.assertEqual(predictions,["python","php"])