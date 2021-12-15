print("hello world")

import pandas as pd

a = pd.read_csv()


import numpy as np
from numpy import dot
from numpy.linalg import norm

doc1 = np.array([0, 1, 1, 1])  # 문서1 벡터
doc2 = np.array([1, 0, 1, 1])  # 문서2 벡터
doc3 = np.array([2, 0, 2, 2])  # 문서3 벡터


def cos_sim(A, B):
    return dot(A, B) / (norm(A) * norm(B))


import pandas as pd
