
from flask import Flask

app = Flask(__name__)

def total(m1,m2,m3,m4):
    return m1+m2+m3+m4


def average(m1,m2,m3,m4):
    return (m1+m2+m3+m4)/4

def grade_cal(avg):
    if avg >= 90:
        return 'S'
    else if avg >= 80:
        return 'A'
    else if avg >= 70:
        return 'B'
    else if avg >= 60:
        return 'C'
    else if avg >= 50:
        return 'D'
    else:
        return 'F'

@app.route("/")
def home():

    a=92
    b=95
    c=87
    d=90    
    tot = total(a,b,c,d)
    avg = average(a,b,c,d)
    grad = grade_cal(avg)
    return f"""
    <h1>Grade Calculator</h1>
    <p>Total marks is: <b>{tot}</b></p>
    <p>Average of marks is: <b>{avg}</b></p>
    <p>Grade of the student is: <b>{grad}</b></p>
    """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)











