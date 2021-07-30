import pandas as pd

INPUT_PREFIX = './data/TCS_영업소간통행시간_1시간_1개월_2020'
OUTPUT_PREFIX = './data/data_2020'
OUTPUT_EXTENSION = '.csv'

output_dataframes = []


def generateData(month):
    month_string = str(month)
    length_month_string = len(month_string)
    if length_month_string == 1:
        month_string = '0' + month_string
    input_file = INPUT_PREFIX + month_string
    output_file = OUTPUT_PREFIX + month_string + OUTPUT_EXTENSION
    print('INPUT :', input_file, '  OUTPUT : ', output_file)
    data = pd.read_csv(input_file, sep=",", encoding="euc-kr")
    data_clean = data.drop(['Unnamed: 6'], axis='columns')
    data_clean = data_clean[data_clean.통행시간 > 0]
    df_data = pd.DataFrame(data_clean, columns=['집계일자', '집계시', '출발영업소코드', '도착영업소코드', '통행시간'])
    start_from_101 = df_data[df_data.출발영업소코드 == 101]
    start_from_101_to_140 = start_from_101[start_from_101['도착영업소코드'].isin([105, 110, 115, 120, 125, 130, 135, 140])]
    start_from_101_to_140 = start_from_101_to_140.assign(
        요일=pd.to_datetime(start_from_101_to_140['집계일자'], format='%Y%m%d').dt.dayofweek)
    start_from_101_to_140.sort_values(by=['집계일자', '집계시'])
    start_from_101_to_140.to_csv(output_file, index=None, header=True)
    output_dataframes.append(start_from_101_to_140)


for month in range(1, 13):
    generateData(month)

output_data = pd.concat(output_dataframes, ignore_index=True, sort=False)
final = OUTPUT_PREFIX + OUTPUT_EXTENSION
output_data.to_csv(final, index=None, header=True)