from flask import Flask, render_template  
app = Flask(__name__)

# Definición del menú como diccionario anidado con varios niveles
menu = {
    "Inicio": "/",
    "Oferta Educativa": {
        "Licenciaturas e Ingenierías": {
            "Ingeniería Ambiental": "/ambiental",
            "Ingeniería Electromecánica": "/electromecanica",
            "Ingeniería Electrónica": "/electronica",
            "Ingeniería Industrial": "/industrial",
            "Ingeniería Química": "/quimica",
            "Ingeniería en Gestión Empresarial": "/gestion",
            "Ingeniería en Sistemas Computacionales": "/sistemas"
        },
        "Posgrado": "/posgrado"
    },
    "Contacto": "/contacto"
}

# Ruta principal
@app.route('/')
def inicio():
    return render_template('menu.html', menu=menu, title="Inicio")

# Rutas para evitar errores 404
@app.route('/<path:subpath>')
def subpagina(subpath):
    return render_template('menu.html', menu=menu, title=subpath.capitalize())

if __name__ == '__main__':
    app.run(debug=True)