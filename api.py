#Let's create our own API using python 

#import flask and request object
from flask import Flask, request

#import and create the SQLAlchemy database
from flask_sqlalchemy import SQLAlchemy 

#assign the flask app to a variable named app. 
app = Flask(__name__)

#configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite: ///data.db'

#define db is an instance of alchemy and pass in the flask app variable we have assined earlier
db = SQLAlchemy(app)

#create a class that is going to inherit from db.Model (define the model)
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique = True, nullable = False)
    description = db.Column(db.String(120))
    #the repr method will allow us to get the objects attributes by refereing to it self.something
    #we are going to return a string in this  which will be invoked whenver we try to print out the drink in a list.
    #using f to make parametrized string
    def __repr__(self):
        return f"{self.name} = {self.description}"

#create a route    
@app.route('/')
def index():
    return 'Hello!'

#Let's figure out how to route it to the /drinks path hint:  Drinks.query.all()
#We're going define an empty list for outputs,  we will iterate through drinks, and describe what it will look like, in this case a dictionary, 
#and append it to the empty list, in this case output=[]. Another words we are createing a list of dictionary. 
 
@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()

    output = []
    for drink in drinks: 
     	drink_data = {'name': drink.name, 'description': drink.description}
        output.append(drink_data)
    return {"drinks": output}


#create a new route, so we can pass in just the id to get a drink , and if it doesn exist we can get  404 page. 
@app.route('/drinks/<id>')

#define a new method with 'drink' variable where we can pass in the id 
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {"name": drink.name, "description": drink.desctiption} 


#adding a new drink 
#create a new route for users to add new data, (POST)
@app.route('/drinks, methods = ['POST'])
def add_drink():
    drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id':drink.id}


# remove a drink (DELETE)
@app.route('/drnks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
  	return {"error" "drink not found"}
    db.session.delete(drink)
    db.sesion.commit()
    return {"message": "delete operation was succesfull"}
