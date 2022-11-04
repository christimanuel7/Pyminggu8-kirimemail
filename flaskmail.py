from flask import Flask, render_template, request
from flask_mail import Mail, Message

app=Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USE_SSL']=False

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        username=request.form['txtUserName']
        password = request.form['txtPassword']
        to = request.form['txtTo']
        subject = request.form['txtSubject']
        message= request.form['areaMessage']

        app.config['MAIL_USERNAME']=username
        app.config['MAIL_PASSWORD']=password

        pesan=Message(subject,sender=username,recipients=[to])
        pesan.body=message

        try:
            mail=Mail(app)
            mail.connect()
            mail.send(pesan)
            return render_template('sukses.html',to=to)
        except:
            return render_template('gagal.html')
    return render_template('form.html')

if __name__=='__main__':
    app.run(debug=True)