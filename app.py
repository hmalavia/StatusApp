from dataclasses import dataclass
from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)
last_updated = {}

# Dictionary to store user statuses
user_statuses = {
    "Dr Pookie Badmosh": {'status':'','time':None},
    "Chonk E Pupper": {'status':'','time':None}
    }


def get_last_updated(user_status):
    time_list = [i[1]['time'] for i in user_statuses.items()]
    time = max([i for i in time_list if not i == None])
    if time is not None :
        for i in user_statuses.items():
            if i[1]['time'] == time:
                user = i[0]
    return (time,user)
    
@app.route("/")
def home():
    return render_template("index.html", user_statuses=user_statuses,last_updated=last_updated)

@app.route("/update_status", methods=["POST"])
def update_status():
    global last_updated
    user = request.form.get("user")
    status = request.form.get("status")
    if user in user_statuses:
        user_statuses[user]['status'] = status
        user_statuses[user]['time'] = datetime.now()
        last_updated['time'] = get_last_updated(user_statuses)[0]
        last_updated['user'] = get_last_updated(user_statuses)[1]
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)