from flask import Flask,render_template,request
import pickle  


app = Flask(__name__)
@app.route('/')
def base():
    return render_template('home.html')
@app.route('/predict',methods=['post'])
def predict():
#loading the model
    model = pickle.load(open('diabetic_model.pkl','rb'))
    prega = int(request.form.get('preg'))
    plasa = int(request.form.get('plas'))
    presa = int(request.form.get('pres'))
    skina = int(request.form.get('skin'))
    testa = int(request.form.get('test'))
    massa = int(request.form.get('mass'))
    predia =int(request.form.get('predi'))
    agea =int(request.form.get('age'))
    print("experience :::: ",prega,plasa,presa,skina,testa,massa,predia,agea)
    output= model.predict([[prega,plasa,presa,skina,testa,massa,predia,agea]])
    if output[0]==0:
     data ="U are not diabetic"
    else:
     show="U are diabetic :("
    return render_template('home.html',data=data)

# @app.route('/galary')
# def galary():
#     return 'Welcome to Galary '
# @app.route('/contact')
# def contact():
#     return 'Welcome to contact page '
# @app.route('/cart')
# def cart():
#     return 'Welcome to Cart Page'

app.run(debug=True)
