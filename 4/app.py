from flask import Flask, render_template_string
app = Flask(__name__)
HTML = """
    <!doctype html>
    <html><body>
    <h1>Student Portal</h1>
    <p>Registration form:</p>
    <form>
    Name: <input name="name"><br>
    Email: <input name="email"><br>
    Phone: <input name="phone"><br>
    Department: <input name="department"><br>
    </form>
    </body></html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
