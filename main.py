import numpy as np
import pandas as pd

if __name__ == '__main__':
    # arr = [1, 3, 5, 67, 7, 9]
    # print(np.mean(arr))
    data = pd.read_csv('data/THPT2017_HaNoi_A.csv')
    print(data.to_string())