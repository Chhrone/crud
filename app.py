from flask import Flask, render_template, request, flash, redirect, url_for

from werkzeug.utils import redirect
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'kursus'

mysql = MySQL(app)

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM peserta")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', data=data)


@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        nama = request.form['nama']
        alamat = request.form['alamat']
        telpon = request.form['telpon']
        gender = request.form['gender']
        kursus = request.form['kursus']
        tanggal = request.form['tanggal']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO peserta (nama, alamat, telpon, gender, kursus, tanggal) VALUES (%s, %s, %s, %s, %s, %s)", (nama, alamat, telpon, gender, kursus, tanggal))
        mysql.connection.commit()
        return redirect(url_for('Index'))
    flash("Berhasil menambahkan data!!")

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM peserta WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    flash("Berhasil menghapus data!")
    return redirect(url_for('Index'))


@app.route('/update', methods= ['POST', 'GET'])
def update():
    if request.method == 'POST':
        nama = request.form['nama']
        alamat = request.form['alamat']
        telpon = request.form['telpon']
        gender = request.form['gender']
        kursus = request.form['kursus']
        tanggal = request.form['tanggal']
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE peserta SET alamat=%s, telpon=%s, gender=%s, kursus=%s, tanggal=%s
        WHERE nama=%s
        """, (alamat, telpon, gender, kursus, tanggal, nama))
        return redirect(url_for('Index'))
    flash("berhasil mengubah data!")





if __name__ == "__main__":
    app.run(debug=True)