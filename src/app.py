from flask import Flask, render_template
from .data import current_job, previous_jobs, pod_enterprise_engineering, projects

app = Flask(__name__)
app.config.update(TEMPLATES_AUTO_RELOAD=True)

data = {
    "jobs": {
        "current": current_job,
        "previous": previous_jobs
    },
    "businesses": {
        "pod_enterprise_engineering": pod_enterprise_engineering
    },
    "projects": projects
}

@app.route("/")
def index():
    return render_template("index.html", data=data)
