from flask import Flask,request,jsonify


app=Flask(__name__)   #application instance

#we are using a protocol called WSGI 
'''
Web
Server
Gateway
Interface


we use different view functions to adress all the different routes.
'''

'''
REST: Representational State Transfer.
We have 4 kinds of HTTP requests,
GET
POST
PUT
DELETE
'''

@app.route('/')
def index():
    return('Hello world!')

#Adding some Dynamic Routing

@app.route('/<name>')
def return_name(name):
    return(f"Hello user, {name}")
    

if __name__=='__main__':
    app.run(debug=True) #by adding the debugger, we can get auto refresh.