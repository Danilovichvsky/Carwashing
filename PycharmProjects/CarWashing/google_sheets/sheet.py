import gspread

gc = gspread.service_account(filename=r"C:\Users\Данил\PycharmProjects\CarWashing\credationals.json")

def write_to_sheet(data = None):
    sheets = gc.open("Django-test")
    worksheet = sheets.sheet1
    worksheet.append_row(data)

def get_info():
    sheets = gc.open("Django-test")
    worksheet = sheets.sheet1
    print(worksheet.get_all_values())



if __name__ == '__main__':
    write_to_sheet(['test1','test2','test3'])
    #get_info()