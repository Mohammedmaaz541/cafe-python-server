from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def addition():
    var_1=int(request.args.get('a'))
    var_2=int(request.args.get('b'))
    sum=var_1+var_2
    return str(sum)

if __name__=="__main__":
    app.run(debug=True)