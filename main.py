from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import geopandas as gpd
import seaborn as sns


def preProcessData():
    data = pd.read_csv('data/diem_thi_thpt_2022.csv')
    data.columns = ['SBD', 'Toán', 'Văn', 'Ngoại Ngữ', 'Lý', 'Hoá', 'Sinh', 'Lịch Sử', 'Địa Lý', 'GDCD']

    # Turn score from object type to float type
    for col in ['Toán', 'Văn', 'Ngoại Ngữ', 'Lý', 'Hoá', 'Sinh', 'Lịch Sử', 'Địa Lý', 'GDCD']:
        data[col] = data[col].astype(float)

    # Set year
    data['Year'] = 2022

    # Province code
    def create_province_code(x):
        if len(str(x)) == 7:
            return '0' + str(x)[0]
        return str(x)[:2]

    data['code'] = data['SBD'].apply(create_province_code)
    map_df = gpd.read_file('data/diaphantinh.geojson')
    map_df.head()
    map_df.loc[44, 'ten_tinh'] = 'Quảng Bình'
    map_df.loc[31, 'ten_tinh'] = 'Kiên Giang'
    map_df.loc[12, 'ten_tinh'] = 'Cần Thơ'
    code_provinces = ['51', '52', '18', '11', '60', '19', '56', '37', '44', '43', '47', '61', '55',
                      '06', '04', '40', '63', '62', '48', '50', '38', '05', '24', '01', '30', '21',
                      '03', '64', '23', '22', '41', '54', '36', '07', '42', '10', '08', '49', '25',
                      '29', '27', '45', '15', '39', '31', '34', '35', '17', '32', '59', '14', '46',
                      '26', '12', '28', '33', '53', '02', '58', '09', '57', '16', '13']

    mapping = {code_provinces[i]: map_df['ten_tinh'].unique().tolist()[i] for i in range(len(code_provinces))}
    data['province'] = data['code'].apply(lambda x: mapping[x])

    data_2020_2022 = pd.read_csv('data/diem_thi_2020_2021.csv')
    data_2020_2022 = data_2020_2022[
        ['SBD', 'Toán', 'Văn', 'Ngoại Ngữ', 'Lý', 'Hoá', 'Sinh', 'Lịch Sử', 'Địa Lý', 'GDCD', 'Year', 'code',
         'province']]
    data_2020_2022.head()

    # Sinh file data mới
    data.append(data_2020_2022).to_csv('data/final_data.csv', index=False)


def initData(dataFinal):
    dataFinal.columns = ['SBD', 'Toan', 'Van', 'Ngoai_ngu', 'Ly', 'Hoa',
                         'Sinh', 'Lich_su', 'Dia_ly', 'GDCD', 'Year', 'code', 'province']

    dataFinal.drop_duplicates(inplace=True)


def meanExample(data):
    plt.bar(['Toan', 'Van', 'Ngoai_ngu', 'Ly', 'Hoa', 'Sinh', 'Lich_su', 'Dia_ly', 'GDCD'],
            data[['Toan', 'Van', 'Ngoai_ngu', 'Ly', 'Hoa', 'Sinh', 'Lich_su', 'Dia_ly', 'GDCD']].mean(),
            width=0.6)
    plt.gcf().set_size_inches(10, 8)
    plt.ylim(0, 10)
    plt.show()


def modeExample(data):  # Điểm phổ biến nhất từng môn
    print(data[['Toan', 'Van', 'Ngoai_ngu', 'Ly', 'Hoa', 'Sinh', 'Lich_su', 'Dia_ly', 'GDCD']].mode())

def medianExample(data):  # Trung vị
    plt.bar(['Toan', 'Van', 'Ngoai_ngu', 'Ly', 'Hoa', 'Sinh', 'Lich_su', 'Dia_ly', 'GDCD'],
            data[['Toan', 'Van', 'Ngoai_ngu', 'Ly', 'Hoa', 'Sinh', 'Lich_su', 'Dia_ly', 'GDCD']].median(),
            width=0.6)
    plt.gcf().set_size_inches(10, 8)
    plt.ylim(0, 10)
    arr = []
    for i in range(0, 21):
        arr.append(i / 2)
    plt.yticks(arr)
    plt.title('Median Example')
    plt.show()


def mathHistExample(data):  # Phổ điểm môn toán
    plt.hist(data[['Toan']], bins=300, facecolor='blue', alpha=0.5)
    plt.title('Math histogram example')
    plt.show()

def histExample(data):
    data[['Toan', 'Van', 'Ngoai_ngu', 'Ly', 'Hoa', 'Sinh', 'Lich_su', 'Dia_ly', 'GDCD']].hist(bins=80)
    plt.gcf().set_size_inches(20, 8)
    plt.title('Histogram example')
    plt.show()

def compareMathHistogram(dataFinal):
    sns.kdeplot(data=dataFinal, x='Toan', hue='Year', bw_adjust=2, palette=["C1", "C2", "C4"])
    plt.title('Compare math score between 3 years')
    plt.show()

def mathScoreGroupByProvince(dataFinal):
    dataFinal.groupby('province')[['Toan']].mean().sort_values(ascending=False, by='Toan').plot(kind='bar')
    plt.ylim(0, 10)
    plt.gcf().set_size_inches(20, 8)
    plt.title('Math score all provinces')
    plt.show()

if __name__ == '__main__':
    # preProcessData()
    dataFinal = pd.read_csv('data/final_data.csv')
    dataFinal.head()
    initData(dataFinal)

    # mathScoreGroupByProvince(dataFinal)
    # compareMathHistogram(dataFinal)
    # meanExample(dataFinal)
    # medianExample(dataFinal)
    modeExample(dataFinal)
    # mathHistExample(dataFinal)
    # histExample(dataFinal)
