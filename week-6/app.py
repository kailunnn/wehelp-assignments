from flask import Flask, render_template, url_for, request, redirect, session
app = Flask(__name__)
app.secret_key="1234567890"

# 連線到資料庫裡的 website 資料表
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='0108',
    database='website')
mycursor = mydb.cursor()

# 首頁
@app.route("/")
def index():
    if "username" in session:
        return redirect("/member")
    return render_template("index.html")

# 會員註冊
@app.route("/signup", methods=["post"])
def signup():
    name = request.form["signupName"]
    account = request.form["signupAccount"]
    password = request.form["signupPassword"]
    # 查詢該 username 的筆數
    sql = "SELECT COUNT(*) FROM `member` WHERE `username` = %s"
    value = (account,)
    mycursor.execute(sql, value)
    myresult = mycursor.fetchone()
    # 若為 1 代表此帳號已經存在資料庫
    if (myresult[0] == 1):
        return redirect("/error/?message=帳號已經被註冊")
    elif (myresult[0] == 0):
        insertSql = "INSERT INTO `member` (name, username, password) VALUES (%s, %s, %s)"
        insertValue = (name, account, password)
        mycursor.execute(insertSql, insertValue)
        mydb.commit()
        return redirect("/")

# 會員登入
@app.route("/signin", methods=["post"])
def verify():
    account = request.form["signinAccount"]
    password = request.form["signinPassword"]
    # 查詢該 username & password 的筆數
    sql = "SELECT COUNT(*) FROM `member` WHERE `username` = %s and `password` = %s"
    value = (account, password)
    mycursor.execute(sql, value)
    myresult = mycursor.fetchone()
    if (myresult[0] == 1):
        nameSearch = "SELECT `name` FROM `member` WHERE `username` = %s and `password` = %s"
        mycursor.execute(nameSearch, value)
        name = mycursor.fetchone()[0]
        session["username"] = name
        return redirect("/member")
    else:
        return redirect("/error/?message=帳號、或密碼輸入錯誤")

# 會員登入成功
@app.route("/member/")
def member():
    if "username" not in session:
        return redirect("/")
    return render_template("member.html", name = session["username"])

# 會員登入失敗
@app.route("/error/")
def error():
    msg = request.args.get("message", "發生錯誤")
    return render_template("error.html", message = msg)

# 會員登出
@app.route("/signout")
def signout():
    del session["username"]
    return redirect("/")

app.run(port=3000)
