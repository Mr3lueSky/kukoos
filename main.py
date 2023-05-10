from flask import Flask, render_template, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()
#configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///financemanager.db"
db.init_app(app)


class Transaction(db.Model):
    __tablename__="Transactions"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    category=db.Column(db.String(200),nullable=False)
    amount = db.Column(db.Float, nullable=False)
    # balance = db.Column(db.Float,nullable=False)

with app.app_context():
    db.create_all()   #creating the table

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/transaction',methods=["GET","POST"])
def transactions():
    return render_template('transaction.html')

@app.route('/viewtransactions',methods=["GET","POST"])
def viewtransactions():
    data=Transaction.query.all()
    return render_template("viewtransactions.html",data=data)
    

@app.route("/addtransactions",methods=["GET","POST"])
def register():
    if request.method=="POST":
      date=request.form["date"]
      description=request.form["description"]
      category=request.form["category"]
      amount=request.form["amount"]
    
      print(request.form)
    #   balance=5000-amount

      transaction=Transaction(date=date,description=description,category=category,amount=amount)
      db.session.add(transaction)
      db.session.commit()
    #   balance=5000
      return render_template("index.html")
    return render_template("transaction.html")


if __name__ == '__main__':
    app.run(debug=True)
