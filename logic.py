"""this is functions of logic of my app"""
import pandas as pd


def get_df_columns(data_frame):
    '''this functions get data frame and returning his column names'''

    return list(data_frame.columns)

def from_df_to_dict(data_frame):
    '''this functions get data frame and returning dictionary'''

    dict_1 = {}
    colums = get_df_columns(data_frame)
    index_of_empty_column = checking_if_some_data_is_empty(data_frame)

    for index, row in data_frame.iterrows():
        list_1 = []
        if index_of_empty_column[index]:
            for i in range(1,len(colums)):
                list_1.append(str(row[i]))
            dict_1[str(row[str(colums[0])])] = list_1

    return dict_1

