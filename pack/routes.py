from pack import app,db
from flask import render_template,redirect,url_for,flash,session
from pack.models import Registerdb
from pack.forms import Register,Login

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route('/Register',methods=['GET','POST'])
def register():
    f=Register()
    if f.validate_on_submit():
        obj=Registerdb.query.filter_by(email=f.email.data).first()
        if obj:
            flash("Email already Registered")
            pass
        else:
            i1 = Registerdb(name=f.name.data,email=f.email.data,passhash=f.password.data)
            db.session.add(i1)
            db.session.commit()
            session['user_id']=int(Registerdb.query.filter_by(email=f.email.data).first().id)
            session.modified = True 
            return redirect(url_for('home'))
    if f.errors != {}:
        for i in f.errors.values():
            flash(i)
            print(i)
    return render_template('register.html',form=f)

@app.route('/login', methods=['GET', 'POST'])
def login():
    f=Login()
    if f.validate_on_submit():
        obj=Registerdb.query.filter_by(email=f.email.data).first()
        if obj:
            if obj.checkpass(f.password.data):
                session['user_id']=int(obj.id)
                session['email']=obj.email
                session.modified = True 
                print(f"✅ Session Set: {session.get('user_id')}, {session.get('email')}") 
                flash('Successfully signed in')
                return redirect(url_for('home'))
            else:
                flash('Incorrect Password')
        else:
            flash("Email Not Registered")
            return redirect(url_for('login'))
    if f.errors != {}:
        for i in f.errors.values():
            flash(i)
            print(i)
    return render_template('login.html',form=f)