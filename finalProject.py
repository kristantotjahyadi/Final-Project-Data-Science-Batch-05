from flask import Flask,render_template,request,redirect,send_from_directory
import mysql.connector
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
import folium

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='alfaindah25',
    database='ayosehat'
)

dbku = db.cursor()

app = Flask(__name__)

@app.route('/file/<path:path>')
def aksesFile(path):
    return send_from_directory('file',path)

@app.route('/')
def home():
    return render_template('mainmenu.html')

@app.route('/signin')
def signinn():
    return render_template('homee.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about2!')
def about2():
    return render_template('about2.html')

@app.route('/about3!')
def about3():
    return render_template('about3.html')

@app.route('/abouts')
def abouts():
    return render_template('abouts.html')

@app.route('/abouts2!')
def abouts2():
    return render_template('abouts2.html')

@app.route('/abouts3!')
def abouts3():
    return render_template('abouts3.html')

@app.route('/daftar',methods=['POST'])
def daftar():
        body = request.form
        dbku = db.cursor()
        dbku.execute('select * from user')
        data = dbku.fetchall()
        email_temp = []
        for item in data:
            email_temp.append(item[3])
        for item in data:
            if body['email'] not in email_temp:
                dbku = db.cursor()
                qry = '''insert into user (
                    nama_depan,
                    nama_belakang,
                    email,
                    passwd,
                    address) values
                    (%s,%s,%s,%s,%s)
                    '''
                val = (
                    body['nama_depan'],
                    body['nama_belakang'],
                    body['email'],
                    body['password'],
                    body['alamat'])
                dbku.execute(qry, val)
                db.commit()
                return render_template('message.html', data={'hasil':'You have signed up successfully','quotes':'The First Wealth is Health - "Ralph Waldo Emerson"'})
            else:
                return render_template('message.html', data={'hasil':'That username is taken. Try Another','quotes':'Health is the greatest gift, contentment the greatest wealth, faithfulness the best relationship - "Buddha"'})

@app.route('/subscribe', methods=['POST'])
def subscribe():
    body = request.form
    qry = '''insert into subcribe(
        email,
        pilihan
    ) values
    (%s,%s)
    '''
    val = (
        body['email'],
        body['pilih']
    )
    dbku.execute(qry,val)
    db.commit()
    return render_template('hearts.html',data={'hasil':'You will receive your first newsletter with our next scheduled circulation!'})

@app.route('/subscribes', methods=['POST'])
def subscribes():
    body = request.form
    qry = '''insert into subcribe(
        email,
        pilihan
    ) values
    (%s,%s)
    '''
    val = (
        body['email'],
        body['pilih']
    )
    dbku.execute(qry,val)
    db.commit()
    return render_template('hearters.html',data={'hasil':'You will receive your first newsletter with our next scheduled circulation!'})
    

@app.route('/error')
def errorr():
    return render_template('error.html')

@app.route('/menu', methods=['POST'])
def signin():
    body = request.form
    dbku.execute('select * from user')
    data = dbku.fetchall()
    email_temp = []
    for item in data:
        email_temp.append(item[3])
    for item in data:
        if body['username'] not in email_temp:
            return render_template('message.html',data={'hasil':"Couldn't find your account or password !",'quotes':'Happiness is the highest form of healh - Dalai Lama'})
        else:
            if item[3] == body['username']:
                if item[4] == body['password']:
                    return render_template('menu.html')
                else:
                    return render_template('message.html',data={'hasil':"Couldn't find your account or password !",'quotes':'Happiness is the highest form of healh - Dalai Lama'})

@app.route('/mainmenu',methods=['GET'])
def mainmenu():
    return render_template('menu.html')

@app.route('/predict', methods=['GET'])
def predict():
    return render_template('predict.html')

@app.route('/results', methods=['POST','GET'])
def results():
    body = request.form
    age = int(body['umur'])
    gender = int(body['sex'])
    chest = int(body['cp'])
    fbs = int(body['fbs'])
    rer = int(body['rer'])
    eia = int(body['eia'])
    slope = int(body['slope'])
    vessels = int(body['vessels'])
    thl = int(body['thl'])
    tekanan = int(body['tekananDarah'])
    kolestrol = int(body['kolestrol'])
    st = int(body['st'])
    detak = int(body['detak'])
    modelLoad = joblib.load('heartmodel')
    a = modelLoad.predict([[age,tekanan,kolestrol,detak,st,gender,chest,fbs,rer,eia,slope,thl,vessels]])
    if a == 1:
        a = 'Heart Disease'
    if a == 0:
        a = 'No Heart Disease'
    return render_template('result.html',data={'nama':a})

@app.route('/direction')
def direction():
    df = pd.read_excel('rumahsakit.xlsx')
    rs = []
    almt = []
    lat = []
    lng = []
    map = folium.Map(
    location= [-6.2138526,106.8281324],
    zoom_start=12)
    for i in df['nama_rumah_sakit']:
        rs.append(i)
    for i in df['alamat_rumah_sakit']:
        almt.append(i)
    for i in df['lat']:
        lat.append(i)
    for i in df['lng']:
        lng.append(i)
    for i in range(len(df)):
        folium.Marker(
        [lat[i],lng[i]],
        popup='Rumah Sakit '+str(rs[i])+' '+' '+str(almt[i]), 
        tooltip='Rumah Sakit ' + rs[i]
    ).add_to(map)
    map.save('./templates/map.html')
    return render_template('direction.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/heart')
def heart():
    return render_template('heart.html')

@app.route('/heart2!')
def heart2():
    return render_template('heart2.html')

@app.route('/heart3!')
def heart3():
    return render_template('heart3.html')

@app.route('/hearter')
def hearter():
    return render_template('hearter.html')

@app.route('/hearter2!')
def hearter2():
    return render_template('hearter2.html')

@app.route('/hearter3!')
def hearter3():
    return render_template('hearter3.html')




if __name__ == '__main__':
    app.run(debug=True)
