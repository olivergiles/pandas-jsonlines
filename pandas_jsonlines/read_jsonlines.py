import numpy as np
import pandas as pd

null = np.nan

def read_jsonlines(filepath):
        with open(filepath) as f:
            lines = f.read().splitlines()
        dicts = [eval(line) for line in lines]
        return pd.DataFrame(dicts)
