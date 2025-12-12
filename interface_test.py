from flask import Flask, render_template, request
import threading
import webview

app = Flask(__name__)

# Your dropdown options
OPTIONS = [
    "Star Types",
    "Galaxies",
    "Planets",
    "Constellations",
    "Nebulae"
]

@app.route("/", methods=["GET", "POST"])
def index():
    selected_value = None

    if request.method == "POST":
        selected_value = request.form.get("my_select")

    return render_template(
        "index.html",
        selected_value=selected_value,
        options=OPTIONS
    )

def start_flask():
    # Flask must listen on 5000 so WebView can load it
    app.run(debug=False, port=5000)

if __name__ == "__main__":
    # Start the Flask server in a separate thread
    threading.Thread(target=start_flask, daemon=True).start()

    # Create a WebView window with icon
    webview.create_window(
        title="O-Star Interface",
        url="http://127.0.0.1:5000",
        width=900,
        height=600,
    )

    webview.start()
