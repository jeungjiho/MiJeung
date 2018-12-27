# _*_ coding: utf-8 _*_
from flask import Flask, render_template, request,session
import pymysql.cursors
app = Flask(__name__)


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123123',
                             db='info',
                             charset='utf8mb4')


try:
    curs = connection.cursor()

    sql = "select name from userinfo"
    curs.execute(sql)


    rows = curs.fetchall()
    Rows = list(rows)

finally:
    connection.close()


def do_the_login():
    return 0


@app.route('/')
def student():
   return render_template('study.html')

@app.route('/account/login', methods=['POST'])
def login():
    if request.method == 'POST':
        userId = request.form['id']
        wp = request.form['wp']

        if len(userId) == 0 or len(wp) == 0:
            return userId+', '+wp+' You did not enter the login information correctly.'

        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='123123',
                                     db='info',
                                     charset='utf8mb4')

        curs = connection.cursor()
        sql = "insert into userinfo(name,usercode) value (%s,%s)"
        curs.execute(sql,(userId,wp))
        connection.commit()
        connection.close()



        session['logFlag'] = True
        session['userId'] = userId

        return session['userId'] + ' Welcome'
    else:
        return 'It is a wrong approach.'

app.secret_key = 'sample_secreat_key'

@app.route('/user/<username>')
def showUserProfile(username):
    app.logger.debug('RETRIEVE DATA - USER ID : %s' % username)
    app.logger.debug('RETRIEVE DATA - Check Compelete')
    app.logger.warn('RETRIEVE DATA - Warning... User Not Found.')
    app.logger.error('RETRIEVE DATA - ERR! User unauthenification.')
    return 'USER : %s' % username


@app.route('/user', methods=['GET'])
def getUser():

    if session.get('logFlag') != True:
        return 'It is a wrong approach.'

    userId = session['userId']
    return '[GET][USER] USER ID : {0}'.format(userId)


@app.route('/caller')
def result():
      return render_template('caller.html')

@app.route('/exe', methods=['GET','POST'])
def Login():
    if request.method == 'POST':
        return render_template('study.html')
    else :
        return 'Failed'

@app.route('/index/')
def input():
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='123123',
                                db='info',
                                charset='utf8mb4')

    try:
        curs = connection.cursor()

        sql = "select name from userinfo"
        curs.execute(sql)

        rows = curs.fetchall()
        Rows = list(rows)
        for i in range(len(Rows)) :
           Rows[i] = list(Rows[i])

    finally:
        connection.close()
        return render_template('index.html', my_list = Rows, len = len(Rows))

print(Rows)


if __name__ == '__main__':
   app.run(debug = True)