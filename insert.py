import pymysql

# 전역변수 선언부
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql=""

# 메인 코드
con = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='sqlDB', charset='utf8')
cur = con.cursor()

while (True) :
    data1 = input("사용자 ID ==> ")
    if data1 == "" :
        break;
    data2 = input("사용자 이름 ==> ")
    data3 = input("사용자 이메일 ==> ")
    data4 = input("사용자 출생연도 ==> ")
    sql = "INSERT INTO userTbl VALUES('" +data1+ "', '" +data2+ "', '" +data3+ "', '" +data4+ "')"
    cur.execute(sql)

con.commit()
con.close()