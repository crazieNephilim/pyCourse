
import MySQLdb

try:
    db = MySQLdb.connect(host="192.168.56.103", user="root", passwd="owaspbwa", db="bwapp")

    curs = db.cursor()

    curs.execute("select * from users")

    for row in curs.fetchall():
        print("User Name: %s, Email: %s" % (row[1], row[3]))

except Exception as e:
    print(e)

