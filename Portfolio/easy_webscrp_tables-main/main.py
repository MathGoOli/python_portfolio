import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import Workbook

#
# def read_data():
#     with open('date.txt', mode="r") as data:
#         content = data.read()
#         return content
#
#
# def time_split(time):
#     time_no_comma = time.split(', ')
#     time_no_as = time_no_comma[1].split(' às')
#     return time_no_as[0]


def request_data(site, table_class, file_name, sheet_name):
    data = requests.get(site)
    soup = BeautifulSoup(data.text, 'html.parser')

    print(f'sheet_name name: {sheet_name}')
    table = soup.find(name="table", class_=table_class)
    table_headers = [i.text.strip() for i in table.find_all('th')]
    #  print(table_headers)
    df = pd.DataFrame(columns=table_headers)

    for row in table.find_all('tr')[1:]:
        data = row.find_all('td')
        row_data = [td.text.strip() for td in data]
        length = len(df)
        df.loc[length] = row_data
    try:
        with pd.ExcelWriter(f'excel/{file_name}.xlsx', mode='a') as writer:
            df.to_excel(writer, sheet_name=sheet_name)
    except FileNotFoundError:
        with pd.ExcelWriter(f'excel/{file_name}.xlsx', mode='w') as writer:
            df.to_excel(writer, sheet_name=sheet_name)
    finally:
        print('done')


if __name__ == '__main__':
    request_data('http://www.semicore.com/reference/density-reference', 'reference', 'my_fille_example',
                 'my_sheet_name')
