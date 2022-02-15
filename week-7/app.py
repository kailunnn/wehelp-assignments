from flask import Flask, render_template, url_for, request, redirect, session, jsonify
import json
app = Flask(__name__)
app.secret_key="1234567890"
app.config["JSON_AS_ASCII"] = False

# 連線到資料庫裡的 website 資料表
import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='0000',
    database='website')
cursor = db.cursor()

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
    sql = "SELECT * FROM `member` WHERE `username` = %s"
    value = (account,)
    cursor.execute(sql, value)
    result = cursor.fetchone()
    if (result):
        return redirect("/error/?message=帳號已經被註冊")
    else:
        insertSql = "INSERT INTO `member` (name, username, password) VALUES (%s, %s, %s)"
        insertValue = (name, account, password)
        cursor.execute(insertSql, insertValue)
        db.commit()
        return redirect("/")

# 會員登入
@app.route("/signin", methods=["post"])
def verify():
    account = request.form["signinAccount"]
    password = request.form["signinPassword"]
    # 查詢該 username & password 的筆數
    sql = "SELECT * FROM `member` WHERE `username` = %s and `password` = %s"
    value = (account, password)
    cursor.execute(sql, value)
    result = cursor.fetchone()
    print(result)
    if (result):
        name = result[1]
        username = result[2] # (2, '小澄', 'orange', 'orange', 10, datetime.datetime(2022, 1, 24, 14, 55, 35))
        session["username"] = username
        session["name"] = name
        return redirect("/member")
    else:
        return redirect("/error/?message=帳號、或密碼輸入錯誤")

# 會員登入成功
@app.route("/member/")
def member():
    if "username" not in session:
        return redirect("/")
    return render_template("member.html", name = session["name"])

# 會員登入失敗
@app.route("/error/")
def error():
    msg = request.args.get("message", "發生錯誤")
    return render_template("error.html", message = msg)

# 會員登出
@app.route("/signout")
def signout():
    del session["username"]
    del session["name"]
    return redirect("/")

# 查詢會員資料的 API
@app.route("/api/members")
def apiMember():
    username = request.args.get("username","錯誤")
    sql = "SELECT * FROM `member` WHERE `username` = %s"
    value = (username,)
    cursor.execute(sql, value)
    result = cursor.fetchone() # (1, '小紅', 'test', 'test', 3, datetime.datetime(2022, 1, 24, 14, 53, 51))
    if (result):
        # "data":{"id":3,"name":"強強","username":"strong"}
        data = {
            "id": result[0],
            "name": result[1],
            "username": result[2]
        }
        return jsonify({"data":data})
    else:
        # "data":null
        return jsonify({"data":None})
    
# 修改會員姓名的 API
@app.route("/api/member", methods=["post"])
def changeName():
    if "username" not in session:
        # {"error":true}
        return jsonify({"error":True})
    else:
        name = json.loads(request.get_data())["name"]
        username = session.get('username')
        # 更改 session 裡的 name
        session["name"] = name
        sql = "UPDATE `member` SET `name` = %s WHERE `username` = %s"
        value = (name, username)
        cursor.execute(sql, value)
        db.commit()
        # {"ok":true}
        return jsonify({"ok":True})


app.run(port=3000,debug=True)

cursor.close()
db.close()
