from flask import Flask,request, jsonify
import util
app = Flask(__name__)

@app.route('/get_columns')
def get_columns():
    response = jsonify({
        'teams':util.get_columns(),
        'venues': util.get_venues()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
@app.route('/predict_score_ipl',methods=['POST'])
def predict_score():
    venue= request.form['venue']
    innings = float(request.form['innings'])
    ball = float(request.form['ball'])
    batting_team = request.form['batting_team']
    bowling_team = request.form['bowling_team']
    response = jsonify({
        'estimated_score' : util.get_estimated_score(venue,innings,ball,batting_team,bowling_team)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server")
    util.load_saved_artifacts()
    app.run()