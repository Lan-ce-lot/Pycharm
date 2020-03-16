import openpyxl, pprint

print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')  # 获取人口统计Sheet工作表
countyData = {}  # 定义统计结果保存字典
print('Reading rows...')

for row in range(2, sheet.max_row + 1):  # 从Excel文件第二行开始读取数据，至最后一行。 range()函数前闭后开，不包括max_row+1行
    state = sheet['B' + str(row)].value  # 读取州名
    county = sheet['C' + str(row)].value  # 读取县名
    pop = sheet['D' + str(row)].value  # 读取人口数量值

    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    countyData[state][county]['tracts'] += 1  # 该县的人口普查次数+1
    countyData[state][county]['pop'] += int(pop)  # 该县所有普查次区人口数量相加

print('Writing results...')
resultFile = open('census2010_result.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))  # pprint格式化打印输出
resultFile.close()
print('Done.')
