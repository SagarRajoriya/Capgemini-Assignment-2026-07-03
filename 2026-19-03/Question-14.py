import xlrd
wb = xlrd.open_workbook("test1.xlsx")
sheet = wb.sheet_by_index(0)
for i in range(sheet.nrows):
    print(sheet.row_values(i))