from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Dictionary to store user statuses
user_statuses = {
    "Dr Pookie Badmosh": "",
    "Chonk E Pupper": ""
}

@app.route("/")
def home():
    return render_template("index.html", user_statuses=user_statuses)

@app.route("/update_status", methods=["POST"])
def update_status():
    user = request.form.get("user")
    status = request.form.get("status")
    if user in user_statuses:
        user_statuses[user] = status
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)