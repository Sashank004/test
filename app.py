from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        age = request.form["age"]

        return render_template(
            "register.html",
            submitted=True,
            name=name,
            email=email,
            age=age
        )

    return render_template("register.html", submitted=False)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)