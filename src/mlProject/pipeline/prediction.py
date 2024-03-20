import joblib
import numpy as np
import pandas as pd
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))  # get the trained model path

# we are directly loading the model as the data is clean . But preprocessing/transforming the data for prediction, we can create different
# BUT if you have scaling/pca, for scaling operations or PCA operations, you can create preprocessor.pickle file and perform those operations on test data.        
    
    def predict(self, data):
        prediction = self.model.predict(data)

        return prediction