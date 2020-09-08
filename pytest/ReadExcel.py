import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expcon

filepath = 'C:\Automation\TestData\PythonTest.xlsx'
browseroptions = webdriver.ChromeOptions()
browseroptions.add_argument("--start-maximized")
#browseroptions.add_argument(("--incognito"))
#browseroptions.headless=True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=browseroptions)
#driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://www.orangehrm.com/orangehrm-30-day-trial/')

'''Open a workbook and assign it to a reference variable'''
workbook = xlrd.open_workbook(filepath)

'''Open a sheet and create a reference variable'''
worksheet = workbook.sheet_by_name('First')

'''Get number of rows and columns'''
rowcount = worksheet.nrows
columncount = worksheet.ncols
print(rowcount)
print(columncount)

'''Read data from the sheet'''
'''Range defined here is from the 1st row to the last row,which is stored in rowcount. Start with 1 as the top is for the headings'''
for current_row in range(1, rowcount):
    '''Store cell value in a variable'''
    row_one = worksheet.cell_value(current_row, 0)
    row_two = worksheet.cell_value(current_row, 1)

    print(row_one+" and "+row_two)

