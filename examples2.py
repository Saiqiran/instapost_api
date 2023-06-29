from flask import Flask,session

app = Flask(__name__)
app.secret_key = 'dfasfdfd5436554'
app.app_context().push()

@app.route('/give-data')
def give_data():
    print(session)
    return 'Data stored in session'

if __name__=="__main__":
    app.run(debug=True)