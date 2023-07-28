## Create a simple Flask application

from flask import Flask ,render_template,request,redirect,url_for  #flask is the lib
app=Flask(__name__) #entry point

@app.route('/')
def home():
    return "<h2>Hello World</h2>"

@app.route('/Welcome')
def welcome():
    return "Welcome to Flask tutorials"

@app.route('/Index')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "the person passed and the score is "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and the score is "+str(score)

@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(maths+science+history)/3
        results="" 
        if average_marks>=50:
            results="success"
        else:
            results="fail"
       # return redirect(url_for(result,score=average_marks))

       


        return render_template('result.html',results=average_marks)
       # return render_template('calculate.html',results=average_marks)









if __name__=='__main__':# in entry pt we run flask app
    app.run(debug=True)
