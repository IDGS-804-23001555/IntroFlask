from flask import Flask, render_template, request 



app = Flask(__name__)

@app.route("/")
def index():
    title="IDGS804 - intro flask"
    listado=["juan", "juanito"]
    return render_template("index.html", title=title, listado=listado)
    

@app.route("/saludo1")
def saludo1():
    return render_template("saludo1.html")

@app.route("/saludo2")
def saludo2():
    return render_template("saludo2.html")




@app.route("/hola")
def func():
    return "debug activado"

@app.route("/user/<string:user>")
def user(user):
    return f"Hola {user}"

@app.route("/numero/<int:n>")
def numero(n):
    return f"<h1>Numero: {n}</h1>"

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f"<h1>Userid: {id}, username: {username}</h1>"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"<h1>La suma es: {n1 + n2}</h1>"

@app.route("/default/")
@app.route("/default/<string:parm>")
def func2(parm = "juanito perez"):
    return f"<h1>Hola {parm}</h1>"

@app.route("/operas")
def operas():
    return '''
            <form>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name">
            <br>
            <label for="name">apaterno:</label>
            <input type="text" id="name" name="name">
            <br>
            <button type="submit">Submit</button>
            </form>
        '''
        
        
@app.route("/operasbas")
def operasbas():
    return render_template("operasbas.html")
    

@app.route("/resultado", methods=["POST", "GET"])
def result():
    n1=request.form.get("num1")
    n2=request.form.get("num2")
    return f"<h1>La suma es: {float(n1) + float(n2)}</h1>"


    

if __name__ == '__main__':
    app.run(debug=True)