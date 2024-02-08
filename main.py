from flask import Flask, render_template, request
import utils.get_bank_id as get_bank_id
import pymysql
app = Flask(__name__)

@app.route("/")
def hello_world():
    bank_list = get_bank_id.get_all_bank_id()
    return render_template('index.html', bank_list=bank_list)

@app.route("/info", methods=['POST'])
def info():
    # save bank info to mysql database
    bank_id = request.form['bank_name']
    bank_account = request.form['bank_account']
    bank_name = get_bank_id.get_bank_name_by_id(bank_id)
    if bank_id is None:
        return "Bank not found"
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='lixi',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `bank` (`bank_account`, `bank_name`) VALUES (%s, %s)"
            cursor.execute(sql, (bank_account, bank_name))
        connection.commit()

    finally:
        connection.close()
    return "Success"
