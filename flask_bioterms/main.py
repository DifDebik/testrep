from flask import Flask, render_template
from datetime import datetime
import calendar
import requests

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/home")
def homesweethome():
    return "Home sweet home "

@app.route("/time")
def time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    # return "Time is:"+ current_time
    return render_template("currenttime.html", current_time=current_time)
@app.route("/cal")

def cal():
    cal1 = calendar.HTMLCalendar(firstweekday=0)
    print(cal1)
    return cal1.formatmonth(2022, 3, withyear=True)

@app.route("/gethtml")
def gethtml():
    return render_template("gethtml.html")

if __name__=='__main__':
    app.run(debug=True)
