import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


import product
import pandas
import selenium

class parser():
    pass

def get_table_check() -> pd.DataFrame:
    '''
    В открытом селениуме поиск инфомормацию о чеке из таблицы.
    Возвращает таблицу с покупками в чеке
    '''
    all_products = driver.find_elements(By.CLASS_NAME, "b-check_item")
    tmp_arr = []
    for elem in all_products:
        tmp = elem.find_elements(By.TAG_NAME, 'td')
        tmp = [elem.text for elem in tmp]
        tmp_arr.append(tmp)

    df = pd.DataFrame(tmp_arr, columns=['id', 'name', 'price', 'count', 'sum'])
    df = df.astype({'price': 'float', 'count': 'int32', 'sum': 'float'})
    return df

def get_aboutCheck_information():
    '''
    Достать дополнительную информацию о чеке.
    :return:

    '''
    name_organisation = driver.find_elements(By.TAG_NAME, 'td')[0].text
    check_date = driver.find_elements(By.TAG_NAME, 'td')[4].text.split(' ')[0]

    return name_organisation, check_date




driver = webdriver.Chrome()