import pymysql
from flask import jsonify, Flask

app = Flask(__name__)

class Database:
    def __init__(self):
        host = "mysql"
        port = "3306"
        user = "root"
        password = "123456"
        db = "pi"
        self.con = pymysql.connect(host=host, user=user, password=password, port=port, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def test(self):
    	self.cur.execute("SELECT * FROM tbl_users LIMIT 50")
    	result = self.cur.fetchall()
    	return result

@app.route('/', methods=['GET'])
def add_user():
	db = Database()
	emps = db.list_employees()
	return ('OK')
		
if __name__ == "__main__":
    app.run()