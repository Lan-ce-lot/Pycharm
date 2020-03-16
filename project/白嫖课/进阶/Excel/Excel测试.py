import openpyxl

print('Opening workbook...')
wb = openpyxl.load_workbook('test.xlsx')
ws = wb.active
cell = ws['A1' : 'C2']
print('hang', cell)
# wb = wb.get_sheet_by_name('Popu')