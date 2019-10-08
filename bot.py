from flask import Flask,render_template,request
from flask_mysqldb import MySQL
import MySQLdb
app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='123456'
app.config['MYSQL_DB']='flask'
mysql=MySQL(app)
@app.route('/', methods=["POST","GET"])
def index():
	if request.method=="POST":
		d=request.form
		sendermsg=d["msg"]
		conn = MySQLdb.connect(host="localhost", user = "root", passwd = "123456", db = "mark")
		cur = conn.cursor()
		cur.execute("select * from bot")
		conn.commit()
		r=cur.fetchall()
		k=list(r)
		c=0
		for i in k:
			if i[0]==sendermsg:
				msg=i[1]
				print(msg)
				c=c+1
		if c==1:
			return render_template("bot.html",msg=msg)
		else:
			return "new word"
	return render_template("bot.html")
@app.route('/add',methods=["POST","GET"])
def hello():
	if request.method=="POST":
		m=request.form
		send=m["msg1"]
		botmsg=m['msg2']
		conn = MySQLdb.connect(host="localhost", user = "root", passwd = "123456", db = "mark")
		cur = conn.cursor()
		cur.execute("insert into bot(sender,bot) values(%s,%s)",(send,botmsg))
		conn.commit()

		return "done"
	return render_template("bot1.html") 
if __name__ == '__main__':
	app.run(debug=True)