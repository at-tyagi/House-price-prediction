from flask import Flask, request, jsonify
app=Flask(__name__)

@app.route('/admin')
def admin():
    return "Hi this app is build with ML algorithms and the app is made by Ashutosh Tyagi"

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    total_sqft=float(request.form['total_sqft'])
    location=request.form['location']
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])
    respone = jsonify({
        'estimated_price' : util.get_estimated_price(location,total_sqft,bath,bhk)
    })



if __name__ =="__main__":
    print("starting python flask for home price prediction")
    app.run()