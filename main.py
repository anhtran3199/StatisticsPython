import numpy as np
import pandas as pd

def readData(filePath):
    return pd.read_csv(filePath)

if __name__ == '__main__':
    data = readData('data/THPT2017_HaNoi_1.csv')
    # print(data.to_string())
    # print(data.shape)
    # print(data.columns)
    # print(data.info())

    score = data['DIEM_THI']
    print(score[0])
    # print(score[0].split("   "))


    # for i in range (0, data.size):

