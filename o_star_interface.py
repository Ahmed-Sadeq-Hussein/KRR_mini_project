from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    selected_value = None

    if request.method == "POST":
        selected_value = request.form.get("my_select")

    return render_template("index.html", selected_value=selected_value)

if __name__ == "__main__":
    app.run(debug=True)
