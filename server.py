from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import jinja2


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route("/")
def index():
    """Return homepage"""

    return render_template("index.html")


@app.route("/application-form")
def application_form():
    """Returns application form. Jobs list needed for jinja variable jobs to iterate in application-form"""

    jobs = ["Engineer", "QA Engineer", "Product Manager"]

    return render_template("application-form.html",
                            jobs=jobs)


@app.route("/application-response", methods=['POST'])
def application_success():
    """ Handles submission of a form in application-form.html returns first_name, last_name, salary, and position from form"""

    first_name = request.form["firstName"]
    last_name = request.form["lastName"]
    position = request.form["position"]
    salary_requirements = "${:,.2f}".format(float(request.form["salaryRequirements"]))

    return render_template("application-response.html", first_name=first_name, last_name=last_name, position=position, salary_requirements=salary_requirements)



#base-HTML

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
