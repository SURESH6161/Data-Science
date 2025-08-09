import os
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)


model = joblib.load('model.pkl')
pass_map = joblib.load('pass_map.pkl')


pass_map_rev = {}
for pass_name, number in pass_map.items():
    pass_map_rev[number] = pass_name

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':     
        hours_studied = float(request.form['hours_studied'])
        attendance = float(request.form['attendance'])
        assignments_completed = float(request.form['assignments_completed'])
        sleep_hours = float(request.form['sleep_hours'])
        pred_num = model.predict([[hours_studied, attendance, assignments_completed, sleep_hours]])[0]

        prediction = pass_map_rev.get(pred_num, "Unknown")

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)
