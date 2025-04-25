import pandas as pd
import openpyxl
import xlrd


def mainx():
    book = xlrd.open_workbook("sample.xls")
    print("The number of worksheets is {0}".format(book.nsheets))
    print("Worksheet name(s): {0}".format(book.sheet_names()))
    sh = book.sheet_by_index(0)
    print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
    # print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=3)))
    for rx in range(sh.nrows):
        print(sh.row(rx))


def mainy():
    # Open the workbook
    workbook = xlrd.open_workbook("sample.xls")

    # Access the first sheet
    sheet = workbook.sheet_by_index(0)

    # Get the number of rows and columns
    num_rows = sheet.nrows
    num_cols = sheet.ncols

    # Iterate through rows and columns
    for row_idx in range(num_rows):
        for col_idx in range(num_cols):
            cell_value = sheet.cell_value(row_idx, col_idx)
            print(cell_value)


def main():
    print("main")
    # cols = [f"Unnamed: {x}" for x in range(4, 10)]
    # print(cols)
    
    cols = [
        "Advertiser ID",
        "Advertiser Name",
        "Campaign ID",
        "Campaign Name",
        "Placement Name",
        "Placement ID",
        "Site",
        "Start Date",
        "End Date",
        "VAST 2.0 Pre-fetch Tag",
        "VAST 3.0 Pre-fetch Tag",
        "VAST 4.0 Pre-fetch Tag",
    ]
    colsNames = {
        "Advertiser ID":"advid",
        "Advertiser Name":"adv_name",
        "Campaign ID":"cid",
        "Campaign Name":"cname",
        "Placement ID":"pid",
        "Placement Name":"pname",
        "Site":"site",
        "Start Date":"date_start",
        "End Date":"date_end",
        "VAST 2.0 Pre-fetch Tag":"vast2",
        "VAST 3.0 Pre-fetch Tag":"vast3",
        "VAST 4.0 Pre-fetch Tag":"vast4",
    }
    df = pd.read_excel("sample.xls", skiprows=12, usecols=cols)
    
    df.rename(columns=colsNames, inplace=True)
    print(df.info())
    #print(df[cols])
    # print(df.iloc[11:])
    # print(df.describe())

    # df.to_csv("out.csv")


main()
