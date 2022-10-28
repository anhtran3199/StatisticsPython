import numpy as np
import pandas as pd
import matplotlib as mpl
from matplotlib import pyplot as plt

def readData():
    return pd.read_csv('data/diem_thi_thpt_2022.csv')

def meanExample(data):
    plt.bar(['toan', 'ngu_van', 'ngoai_ngu', 'vat_li', 'hoa_hoc', 'sinh_hoc',
             'lich_su', 'dia_li', 'gdcd'],
            data[['toan', 'ngu_van', 'ngoai_ngu', 'vat_li', 'hoa_hoc', 'sinh_hoc',
                                                 'lich_su', 'dia_li', 'gdcd']].mean(),
            width=0.6)
    plt.gcf().set_size_inches(10, 8)
    plt.show()

def modeExample(data):
    plt.bar(['toan', 'ngu_van', 'ngoai_ngu', 'vat_li', 'hoa_hoc', 'sinh_hoc',
             'lich_su', 'dia_li', 'gdcd'],
            data[['toan', 'ngu_van', 'ngoai_ngu', 'vat_li', 'hoa_hoc', 'sinh_hoc',
                  'lich_su', 'dia_li', 'gdcd']].mode(),
            width=0.6)
    plt.gcf().set_size_inches(10, 8)
    plt.show()

def medianExample(data):
    plt.bar(['toan', 'ngu_van', 'ngoai_ngu', 'vat_li', 'hoa_hoc', 'sinh_hoc',
             'lich_su', 'dia_li', 'gdcd'], data[['toan', 'ngu_van', 'ngoai_ngu', 'vat_li', 'hoa_hoc', 'sinh_hoc',
                                                 'lich_su', 'dia_li', 'gdcd']].median(), width=0.6)
    plt.gcf().set_size_inches(10, 8)
    plt.show()

def histExample(data):
    plt.hist(data[['toan']], bins=30, facecolor='blue', alpha=0.5)
    # plt.gcf().set_size_inches(20, 8)
    plt.show()


if __name__ == '__main__':
    data = readData()
    # meanExample(data)
    # medianExample(data)
    # modeExample(data)
    histExample(data)
    data[['toan', 'ngu_van', 'ngoai_ngu', 'vat_li', 'hoa_hoc', 'sinh_hoc',
                                                 'lich_su', 'dia_li', 'gdcd']].hist()



