import pandas as pd
import numpy as np


chat_id = 773978697 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    mean_count = np.mean(x)
    t = 10
    L = mean_count / t
    return L
