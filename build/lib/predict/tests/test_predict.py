import unittest
from unittest.mock import MagicMock
import tempfile
import pandas as pd
from predict.predict.run import TextPredictionModel

import os
import json

class TestPredict(unittest.TestCase):
    
    artefacts_path = "train/data/artefacts/2023-01-04-23-23-57"
    
    def test_from_artefacts(self):
        # Act
        model = TextPredictionModel.from_artefacts(self.artefacts_path)
        # Assert
        self.assertIsInstance(model, TextPredictionModel)
        self.assertIsNotNone(model.model)
        self.assertIsNotNone(model.params)
        self.assertIsNotNone(model.labels_to_index)


    def test_predict(self):
        model = TextPredictionModel.from_artefacts(self.artefacts_path)
        predictions = model.predict([
            "Is it possible to execute the procedure of a function in the scope of the caller?",
            "Hi I'm steve"
            ], top_k = 2)

        # assert that accuracy is equal to 1.0
        self.assertEqual(predictions, ['php', 'c#'])