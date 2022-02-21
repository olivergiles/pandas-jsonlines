import pandas as pd
import pandas_jsonlines.read_jsonlines as rjsl
import os

def test_rjsl():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'data', 'data.jsonlines') 
    assert(isinstance(rjsl.read_jsonlines(filename), pd.DataFrame))
