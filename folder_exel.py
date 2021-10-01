""" folder and exel creating script """
import os
import pandas as pd
from config import hotels,columns


def creating_output_folder():
    """ creating output folder """
    path = os.getcwd()
    try:
        path = os.path.join(path, 'output')
        os.mkdir(path)
    except OSError:
        pass


def creating_folders():
    """ creating folders and returning paths """
    paths = []
    path = os.getcwd()
    try:
        path1 = os.path.join(path,"otchety")
        os.mkdir(path1)
        for hotel in hotels:
            try:
                path2 = path1
                path2 = os.path.join(path2,hotel)
                os.mkdir(path2)
                paths.append(path2)
            except OSError:
                paths.append(path2)
    except OSError:
        for hotel in hotels:
            try:
                path2 = path1
                path2 = os.path.join(path2,hotel)
                os.mkdir(path2)
                paths.append(path2)
            except OSError:
                paths.append(path2)
    return paths


def creating_xl(paths):
    """ geting paths and creating excel files  """
    for path in paths:
        col = columns

        if path[-6:] == 'другое':
            col.append('Отель')

        data_frame = pd.DataFrame(columns=col)
        for i in ['09','10','11','12']:
            for j in range(1,32):
                if i in ['09', '11'] and j == 31:
                    break
                date = str(j) + '.' + i
                xl_name = date + '.xlsx'
                xl_path = os.path.join(path, xl_name)
                data_frame.to_excel(xl_path, index=False)



if __name__ == "__main__":
    path_ = creating_folders()
    creating_xl(path_)
    creating_output_folder()
