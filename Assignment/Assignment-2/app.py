from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
  return render_template('about.html')


@app.route("/aboutme")
def aboutme():
  return render_template('aboutme.html')

@app.route("/login")
def login():
  return render_template('login.html')

@app.route("/register")
def register():
  return render_template('register.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         name = request.form['name']
         addr = request.form['address']

         
         with sql.connect("student_database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(name,addr,city,pin) )
            con.commit()
            msg = "Record successfully added!"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("list.html",msg = msg)
         con.close()