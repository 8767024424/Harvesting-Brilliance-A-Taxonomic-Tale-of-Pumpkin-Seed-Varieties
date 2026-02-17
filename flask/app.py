import numpy as np
import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        Area = float(request.form['Area'])
        Perimeter = float(request.form['Perimeter'])
        Major_Axis_Length = float(request.form['Major_Axis_Length'])
        Solidity = float(request.form['Solidity'])
        Extent = float(request.form['Extent'])
        Roundness = float(request.form['Roundness'])
        Aspect_Ratio = float(request.form['Aspect_Ratio'])
        Compactness = float(request.form['Compactness'])

        features = np.array([[Area, Perimeter, Major_Axis_Length,
                              Solidity, Extent, Roundness,
                              Aspect_Ratio, Compactness]])

        prediction = model.predict(features)[0]

        if prediction == 0:
            result = "Hence, based on calculation: Your seed lies in Çerçevelik class"
        else:
            result = "Hence, based on calculation: Your seed lies in Ürgüp Sivrisi class"

        return render_template("predict.html", prediction_text=result)
    
    return render_template("predict.html")


if __name__ == "__main__":
    app.run(debug=True)
