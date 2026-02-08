from flask import Flask, render_template, request
import math
from flask_wtf.csrf import CSRFProtect
import forms
from formsC import CinepolisForm

# Crear la app una sola vez
app = Flask(__name__)
app.secret_key = 'clave_Secreta'  # Necesaria para CSRF

# Inicializar CSRF
csrf = CSRFProtect(app)

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
         
@app.route("/operasbas", methods=["GET", "POST"])
def operasbas():
    res=None
    if request.method == 'POST':
        n1=request.form.get('num1')
        n2=request.form.get('num2')
        if request.form.get('operacion')=='suma':
            res=float(n1)+float(n2)
        if request.form.get('operacion')=='resta':
            res=float(n1)-float(n2)
        if request.form.get('operacion')=='div':
            res=float(n1)/float(n2)
        if request.form.get('operacion')=='multi':
            res=float(n1)*float(n2)
    return render_template("operasbas.html", res=res)
    

@app.route("/resultado", methods=["POST", "GET"])
def result():
    n1=request.form.get("num1")
    n2=request.form.get("num2")
    return f"<h1>La suma es: {float(n1) + float(n2)}</h1>"

@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    res = None
    if request.method == 'POST':
        x1 = float(request.form.get('x1'))
        y1 = float(request.form.get('y1'))
        x2 = float(request.form.get('x2'))
        y2 = float(request.form.get('y2'))
        res = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return render_template("distancia.html", res=res)
    
@app.route("/alumnos", methods=["GET", "POST"] )
def alunmos():
    mat=0
    nom=""
    ape=""
    email=""
    alumno_class=forms.Userform(request.form)
    if request.method == 'POST' and alumno_class.validate():
        mat=alumno_class.matricula.data
        nom=alumno_class.nombre.data
        ape=alumno_class.apellido.data
        email=alumno_class.correo.data
    return render_template("alumnos.html", form=alumno_class, mat=mat, nom=nom, ape=ape, email=email)

@app.route("/cinepolis", methods=['GET', 'POST'])
def cinepolis():
    form = CinepolisForm(request.form)
    total_pagar = 0.0
    mensaje = ""

    if request.method == 'POST' and form.validate():
        try:
            nombre = form.nombre.data
            compradores = int(form.cant_compradores.data)
            boletas = int(form.cant_boletas.data)
            tarjeta = form.tarjeta.data        
            max_boletas_permitidas = compradores * 7
            if boletas > max_boletas_permitidas:
                mensaje = f"Error: No se pueden comprar más de 7 boletas por persona. (Máximo permitido para {compradores} personas: {max_boletas_permitidas})"
            else:
                precio_unitario = 12
                total = boletas * precio_unitario
                if boletas > 5:
                    total = total * 0.85 
                elif boletas >= 3:
                    total = total * 0.90 
                if tarjeta == 'Si':
                    total = total * 0.90 
                total_pagar = total
                mensaje = f"Procesado exitosamente para {nombre}"
        except Exception as e:
            mensaje = "Ocurrió un error en el cálculo"
    return render_template("cinepolis.html", form=form, total=total_pagar, mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
