from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Microbiologist',
        'location': 'Uyo, Nigeria',
        'salary': 'NGN 300,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Uyo, Nigeria',
        'salary': 'NGN 250,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
    },
    {
        'id': 4,
        'title': 'Penetration Tester',
        'location': 'Uyo, Nigeria',
        'salary': 'NGN 320,000'
    }
]

@app.route("/")
def home():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)