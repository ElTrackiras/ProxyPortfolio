from flask import Flask, render_template, url_for
from flaskext.mysql import MySQL
import base64


app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'sql6427929'
app.config['MYSQL_DATABASE_PASSWORD'] = 'NjIEsy1LN5'
app.config['MYSQL_DATABASE_DB'] = 'sql6427929'
app.config['MYSQL_DATABASE_HOST'] = 'sql6.freemysqlhosting.net'

# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = ''
# app.config['MYSQL_DATABASE_DB'] = 'trackrsweb'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()


@app.route('/', methods=['GET'])
def index():
    cursor.execute('SELECT * FROM softwares')
    software_data = cursor.fetchall()
    return render_template('index.html', softwares=software_data)

@app.route('/about')
def about():
    cursor.execute('SELECT aboutme FROM social')
    about_me = cursor.fetchone()[0]
    return render_template('about.html', title='About', about_me=about_me)


if __name__ == "__main__":
    app.run(debug=True)
