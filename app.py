import ast
from flask import Flask, render_template, redirect, url_for, request, flash
import pymysql
from sql_init import Mysql
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)


@app.route('/')  # 登录页
def index():
    return render_template('login.html')


@app.route('/login_fail')
def login_fail():
    return render_template('login_fail.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = Mysql()
        userinfo = db.login(username)
        if userinfo:
            if userinfo['password'] == password:
                if userinfo['type'] == 'admin':
                    return render_template('admin.html')
                elif userinfo['type'] == 'user':
                    return render_template('user.html')

            else:
                print('密码错误')
                return render_template('login_fail.html')
        else:
            print('用户名不存在')
            flash('用户名或密码错误')
            return redirect(url_for('login_fail'))
    return render_template('login.html')


@app.route('/register_success')
def register_success():
    return render_template('register_success.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # usertype = request.form['type']
        usertype = 'user'
        db = Mysql()
        if db.is_user_exist(username):
            return render_template('register_fail.html')
        else:
            db.register(username, password, usertype)
        return redirect(url_for('register_success'))
    return render_template('login.html')


@app.route('/admin')  # 登录页
def admin():
    return render_template('admin.html')


@app.route('/user')  # 登录页
def user():
    return render_template('user.html')


@app.route('/turn_to_register')
def turn_to_register():
    return render_template("register.html")


@app.route("/info", methods=['GET', 'POST'])
def info():
    # 调用
    db = Mysql()
    results = db.getdata()
    return render_template("admin.html", results=results)


@app.route("/info_user", methods=['GET', 'POST'])
def info_user():
    # 调用
    db = Mysql()
    results = db.getdata()
    return render_template("user.html", results=results)


@app.route("/search", methods=['POST'])
def search():
    # 调用
    if request.method == 'POST':
        keywords = request.form.get("keyword")
        print('路由输出：')
        print(keywords)
        db = Mysql()
        results = db.search(keywords)
        if len(results) > 0:
            print('results is not none')
            print(results)
            return render_template("admin.html", results=results)
        else:
            print('not found')
            print(results)
            return render_template("admin_notfound.html")


@app.route("/search_user", methods=['POST'])
def search_user():
    # 调用
    if request.method == 'POST':
        keywords = request.form.get("keyword")
        print('路由输出：')
        print(keywords)
        db = Mysql()
        results = db.search(keywords)
        if len(results) > 0:
            print('results is not none')
            print(results)
            return render_template("user.html", results=results)
        else:
            print('not found')
            print(results)
            return render_template("user_notfound.html")


@app.route("/back_to_admin")
def back_to_admin():
    return render_template('admin.html')


@app.route("/delete", methods=['POST'])
def delete():
    if request.method == 'POST':
        ID = request.form['id']
        print(ID)
        db = Mysql()
        results = db.delete(ID)
        if results == True:
            print('删除成功')
            return redirect(url_for('info'))
        else:
            return render_template('delete_fail.html')


@app.route("/update_by_id", methods=['POST'])
def update_by_id():
    if request.method == 'POST':
        print('update_by_id')
        ID = request.form['id']
        print('ID:')
        print(ID)
        # data_tuple = ast.literal_eval(item)
        # ID=data_tuple[0]
        # print(data_tuple)
        # print('ID='+ID)
        db = Mysql()
        results = db.search_by_id(ID)
        print(results)
        print(results[0])
        return render_template('update_main.html', results=results)


@app.route("/update", methods=['POST'])
def update():
    if request.method == 'POST':
        id = request.form['id']
        ID = ast.literal_eval(id)
        img = request.form['img']
        print('img:' + img)
        name = request.form['name']
        print('name:' + name)
        author = request.form['author']
        print('author:' + author)
        publish = request.form['publish']
        print('publish:' + publish)
        price = request.form['price']
        print('price:' + price)
        amount = request.form['amount']
        print('amount:' + amount)
        position = request.form['position']
        print('position:' + position)
        intro = request.form['intro']
        print('intro:' + intro)
        data = [ID, img, name, author, publish, price, amount, position, intro]
        print(data)
        db = Mysql()
        result = db.update(data)
        print(result)
        if result == True:
            results = db.search_by_id(ID)
            print(results)
            return render_template('update_main.html', results=results)
        else:
            print('update fail')
            return render_template('update_fail.html')


@app.route("/turn_to_insert")
def turn_to_insert():
    return render_template("insert.html")


@app.route("/insert", methods=['POST'])
def insert():
    if request.method == 'POST':
        # id = request.form['id']
        # ID = ast.literal_eval(id)
        img = request.form['img']
        print('img:' + img)
        name = request.form['name']
        print('name:' + name)
        author = request.form['author']
        print('author:' + author)
        publish = request.form['publish']
        print('publish:' + publish)
        price = request.form['price']
        print('price:' + price)
        amount = request.form['amount']
        print('amount:' + amount)
        position = request.form['position']
        print('position:' + position)
        intro = request.form['intro']
        print('intro:' + intro)
        data = [img, name, author, publish, price, amount, position, intro]
        print(data)
        db = Mysql()
        results = db.insert(data)
        if results == False:
            return render_template('insert_fail.html')
        else:
            return render_template('insert_success.html', results=results)


@app.route("/back_to_insert")
def back_to_insert():
    return render_template('insert.html')


if __name__ == '__main__':
    app.run()
