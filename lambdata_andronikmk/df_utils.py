""""
Utility functions for working with DataFrames
"""

import pandas as pd
import numpy as np

TEST_DF = pd.DataFrame([1,2,3])


def enlarge(n):
    """
    Enlarge a number, multiplying by 100:

        Params: n

    """
    return n * 100

if __name__ == "__main__":
    result = enlarge(40)
    print(result)