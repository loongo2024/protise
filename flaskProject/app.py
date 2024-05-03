from flask import Flask, render_template, request
from data_1 import passwold_book

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    # 返回网页文件
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def hello_login():  # put application's code here
    # 登录到服务器，获取用户名与密码，然后进行校验，再记录信息，在返回后台页面
    username = request.form['username']
    password = request.form['password']
    print(username,password)
    if username == '管理员' and password == "123456":
        return render_template('admin_1.html', passwold_book=passwold_book)
    #for i in passwold_book:
    #     if username == i['user'] and password == i['pass_word']:
    #         break
    else:
        return render_template('admin.html')
    # 登录成功之后，返回后台页面
    # return render_template('admin_1.html', passwold_book=passwold_book)
@app.route('/delete/<user>')
def hello_delete(user):  # put application's code here
    # 删除逻辑 先找到信息
    for n in passwold_book:
        if n['user'] == user:
            passwold_book.remove(n)
    return render_template('admin_1.html', passwold_book=passwold_book)

@app.route('/change/<user>')
def hello_change(user):  # put application's code here
    for n in passwold_book:
        if n['user'] == user:
            return render_template('change.html', use=n)

@app.route('/changed/<name>', methods=["POST"])
def hello_changed(name):  # put application's code here
    # 修改 拿到提交的信息
    for n in passwold_book:
        if n['user'] == name:
            n['user'] = request.form.get('user')
            n['age'] = request.form.get('age')
            n['buff'] = request.form.get('buff')
            n['height'] = request.form.get('height')
            n['weight'] = request.form.get('weight')
    return render_template('admin_1.html', passwold_book=passwold_book)

@app.route("/add")
def hello_add():
    return render_template('add.html')

@app.route("/add2", methods=["POST"])
def hello_add2():
    n = {}
    n['user'] = request.form.get('user')
    n['age'] = request.form.get('age')
    n['buff'] = request.form.get('buff')
    n['height'] = request.form.get('height')
    n['weight'] = request.form.get('weight')

    passwold_book.insert(0, n)
    return render_template('admin_1.html', passwold_book=passwold_book)

@app.route('/find/<user>')
def hello_find(user):  # put application's code here
    # 先找到信息，再删除后放到前列
    for n in passwold_book:
        if n['user'] == user:
            passwold_book.remove(n)
            passwold_book.insert(0, n)
    return render_template('admin_1.html', passwold_book=passwold_book)

if __name__ == '__main__':
    app.run()
