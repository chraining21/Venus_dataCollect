import pymysql
import GetFile as g

#資料庫連線設定
db = pymysql.connect(host='163.13.201.83', port=3306, user='root', passwd='rootroot', db='sys')
#建立操作游標
cursor = db.cursor()
ingre_name, what_it_does, irritancy, comedogenicity, rank, alias = g.incide2('GLYCERIN')
sql = "INSERT INTO ingres (name,irr,com,tier) VALUES (%s, %s, %s, %s)"
val = (ingre_name,irritancy,comedogenicity,rank)
cursor.execute(sql,val)
try:
  #提交修改
  db.commit()
  print('success')
except:
  #發生錯誤時停止執行SQL
  db.rollback()
  print('error')

#關閉連線
db.close()
