import pandas as pd
from Classes import product
import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in



def create_excel_file_from_SQL(data):
    ''' Формирует файл экселя по данным
    '''

    pass


def create_excel_file_from_operation(data):
    ''' Формирует файл экселя по данным
    '''

    df = pd.DataFrame(data[3])
    df.to_excel(os.path.join(script_dir, 'excel_buffer/asd.xlsx'))
    pass

def preproc_data_to_excel(data):
    ''' Преобразует данные для эксельки
    :param data:
    :return:
    '''
    pass


def get_excel_data():
    ''' Достать данные из экселя
    '''
    pass

