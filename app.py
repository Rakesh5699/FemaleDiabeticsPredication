from flask import Flask, render_template,request

app = Flask(__name__,template_folder='templates')
import pickle
#model load
model = pickle.load(open('Diabetics_model.pkl','rb'))

@app.route("/") 
def home():
    return render_template("index.html")

values = 0
@app.route("/predict",methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        pregnancies = int(request.form['Pregnancies'])
        glucose = int(request.form['Glucose'])
        bloodpressure = int(request.form['BloodPressure'])
        skinthickness = int(request.form['SkinThickness'])
        insulin = int(request.form['Insulin'])
        bmi = float(request.form['bmi'])
        diabetespedigreefunction = float(request.form['DiabetesPedigreeFunction'])
        age = int(request.form['age'])
        values = [pregnancies,glucose,bloodpressure,skinthickness,insulin,bmi,diabetespedigreefunction,age]
        predicted_res = model.predict([values])
        pred= predicted_res[0]
        if pred == 1:
            return render_template("index.html", result="Yes,you have diabetics")
        elif pred == 0:
            return render_template("index.html", result="No,You are not effected to diabetic")
        else:
            return render_template("index.html", result="Somthing worng")
    else:
        return render_template('index.html',result="NO result")



if __name__=="__main__":
    app.run(debug=True)