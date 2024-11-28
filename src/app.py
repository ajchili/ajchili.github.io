from flask import Flask, render_template
from data import current_job, previous_jobs

app = Flask(__name__)
app.config.update(TEMPLATES_AUTO_RELOAD=True)


@app.route("/")
def index():
    return render_template("index.html", current_job=current_job, previous_jobs=previous_jobs)
