import openpyxl,requests,bs4,pymysql
import GetFile as g

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='sys')
cursor = db.cursor()
wb = openpyxl.load_workbook('')
sheet = wb.worksheets[0]
for i in range(1, sheet.max_row+1):
    print("row="+str(i))
    for j in range(1, sheet.max_column+1):
        ing = str(sheet.cell(row=i, column=j).value)
        name, what_it_does, irritancy, comedogenicity, rank, alias = g.incide2(ing)
        sql = "INSERT INTO ingres (name,irr,com,rank) VALUES (name,irritancy,comedogenicity,rank)"