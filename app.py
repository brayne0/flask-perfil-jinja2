from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    # Variables simples
    nombre = "Brayne"
    universidad = "Universidad Nacional Pedro Henríquez Ureña"
    siglas = "UNPHU"

    # Diccionario para los apellidos
    apellidos = {
        "primero": "Duarte",
        "segundo": "Rodríguez",
    }

    # Listas de diccionarios para las asignaturas y los hobbies
    asignaturas = [
        {"codigo": "INF-374", "nombre": "Ciberseguridad en Software"},
        {"codigo": "INF-382", "nombre": "Tecnologías de la Cuarta Revolución Industrial"},
        {"codigo": "INF-383", "nombre": "Machine Learning"},
        {"codigo": "INF-434", "nombre": "Big Data con Procesamiento Distribuido"},
        {"codigo": "INF-435", "nombre": "Proyecto Integrador en Sistemas"},
    ]

    hobbies = [
        {"nombre": "Hacer trading", "detalle": "Mercados, gráficos y estrategia", "icono": "grafica"},
        {"nombre": "Programar", "detalle": "Crear proyectos y automatizar ideas", "icono": "codigo"},
        {"nombre": "Jugar baloncesto", "detalle": "Cancha, equipo y competencia", "icono": "baloncesto"},
    ]

    return render_template(
        "index.html",
        nombre=nombre,
        apellidos=apellidos,
        universidad=universidad,
        siglas=siglas,
        asignaturas=asignaturas,
        hobbies=hobbies,
    )


if __name__ == "__main__":
    app.run(debug=True)
