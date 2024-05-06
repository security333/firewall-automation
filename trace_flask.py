from flask import Flask, render_template, request
import tracouteroute

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tracouteroute", methods=["POST"])
def tracouteroute():
    start_point = request.form["start_point"]
    end_point = request.form["end_point"]

    try:
        route = tracouteroute.get_route(start_point, end_point)
        return render_template("result.html", route=route)
    except Exception as e:
        return render_template("error.html", error=e)

if __name__ == "__main__":
    app.run(debug=True)
