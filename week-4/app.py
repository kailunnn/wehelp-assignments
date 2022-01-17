from flask import  Flask, render_template, url_for, request, redirect, session
app = Flask(__name__)
app.secret_key="1234567890" # 設定 session 密鑰

# 網址路徑 / 的對應函式 -> 首頁
@app.route("/")
def index():
    if session.get("status") == "已登入":
        return render_template("member.html")
    return render_template("index.html")

# 網址路徑 /signin 的對應函式 -> 驗證
@app.route("/signin", methods=["post"])
def verify():
    account = request.form["acount"]
    password = request.form["password"]
    if(account == "test" and password == "test"):
        session["status"] = "已登入"
        return redirect("/member")
    elif(account == "" or password == ""):
        return redirect("/error/?message=請輸入帳號、密碼")
    else:
        return redirect("/error/?message=帳號、或密碼輸入錯誤")

# 網址路徑 /member/ 的對應函式 -> 登入成功
@app.route("/member/")
def member():
    if(session.get("status") == "未登入"):
        return redirect("/")
    return render_template("member.html")

# 網址路徑 /error/ 的對應函式 -> 登入錯誤訊息
@app.route("/error/")
def error():
    msg = request.args.get("message", "發生錯誤")
    return render_template("error.html", message = msg)

# 網址路徑 /signout 的對應函式 -> 登出
@app.route("/signout")
def signout():
    session["status"] = "未登入"
    return redirect("/")
    
# 啟動網站伺服器
app.run(port=3000)
