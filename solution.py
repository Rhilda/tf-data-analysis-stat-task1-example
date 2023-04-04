import pandas as pd
import numpy as np


chat_id = 773978697 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    t = 10
    n = len(x)
    lmbd = x.sum() / (t*n)
    return lmbd
