import pandas as pd
import numpy as np
import scipy.stats as sps


chat_id = 422119389 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: 
    p_value = sps.permutation_test((x, y), lambda x, y, axis: np.mean(x, axis=axis) - np.mean(y, axis=axis), vectorized=True, n_resamples=5000, alternative='greater').pvalue 
    alpha = 0.09
    return p_value < alpha
