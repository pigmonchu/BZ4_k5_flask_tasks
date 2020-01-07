from tasks import app
from flask import render_template, request, redirect, url_for

import csv

DATOS = './data/tareas.dat'
header = ['title', 'description', 'date']

def todas():
    fdatos = open(DATOS, 'r')
    csvreader = csv.reader(fdatos, delimiter=",", quotechar='"')

    registros = []
    for linea in csvreader:
        registros.append(linea)
        print(linea)

    filas = []
    for datos in registros:
        d = {}

        for ix, nombre_campo in enumerate(header): 
            d[nombre_campo] = datos[ix]
        filas.append(d)

    fdatos.close()

    return filas

def append(task):
    fdatos = open(DATOS, 'a')
    csvwriter = csv.writer(fdatos, delimiter=",", quotechar='"')

    title = task.get('title')
    desc = task.get('description')
    date = task.get('date')

    csvwriter.writerow([title, desc, date])

    fdatos.close()



@app.route("/")
def index():
    filas = todas()
    return render_template("index.html", tareas=filas)

@app.route("/newtask", methods=['GET', 'POST'])
def newTask():
    if request.method == 'GET':
        return render_template("task.html")

    append(request.values)

    return redirect(url_for("index"))