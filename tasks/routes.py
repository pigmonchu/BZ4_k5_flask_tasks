from tasks import app
from flask import render_template, request, redirect, url_for

import csv

DATOS = './data/tareas.txt'
cabecera = ['title', 'description', 'date']

@app.route("/")
def index():
    fdatos = open(DATOS, 'r')
    csvreader = csv.reader(fdatos, delimiter=",", quotechar='"')

    registros = []
    for linea in csvreader:
        registros.append(linea)

    fdatos.close()
    print()
    print(registros)
    print()
    return render_template("index.html", registros=registros) 


@app.route("/newtask", methods=['GET', 'POST'])
def newTask():
    if request.method == 'GET':
        return render_template("task.html")

    fdatos = open(DATOS, 'a')
    csvwriter = csv.writer(fdatos, delimiter=",", quotechar='"')

    title = request.values.get('title')
    desc = request.values.get('desc')
    date = request.values.get('date')

    csvwriter.writerow([title, desc, date])

    fdatos.close()
    return redirect(url_for("index"))
