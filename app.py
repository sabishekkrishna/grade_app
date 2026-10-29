from flask import Flask
app = Flask(__name__)
def calculate_total(m1, m2, m3, m4):
    return m1 + m2 + m3 + m4
def calculate_average(m1, m2, m3, m4):
    return (m1 + m2 + m3 + m4) / 4
@app.route("/")
def home():
    a = 92
    b = 95
    c = 87
    d = 90
    tot_marks = calculate_total(a, b, c, d)
    avg_marks = calculate_average(a, b, c, d)  
    return f"""
    <h1>Grade Calculator</h1>
    <p>Total marks is: <b>{tot_marks}</b></p>
    <p>Average of marks is: <b>{avg_marks}</b></p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
