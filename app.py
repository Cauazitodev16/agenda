from flask import Flask, render_template, request, redirect, url_for
from models.tarefa import Tarefa
from models.database import init_db

app = Flask(__name__)

init_db()

@app.route('/')
def home():
    return render_template('home.html', titulo='Home')

@app.route('/agenda', methods=['GET', 'POST'])
def agenda():

    if request.method == 'POST':
        titulo = request.form['titulo-tarefa']
        data_prevista = request.form['data-conclusao']

        if data_prevista == "":
            data_prevista = None

        tarefa = Tarefa(titulo, data_prevista)
        tarefa.salvar_tarefa()

        return redirect(url_for('agenda'))

    tarefas = Tarefa.obter_tarefas()
    return render_template('agenda.html', titulo='Agenda', tarefas=tarefas)


@app.route('/delete/<int:idTarefa>')
def delete(idTarefa):
    tarefa = Tarefa.id(idTarefa)
    tarefa.excluir_tarefa()
    return redirect(url_for('agenda'))


@app.route("/concluir/<int:idTarefa>")
def concluir(idTarefa):
    tarefa = Tarefa.id(idTarefa)
    tarefa.concluir_tarefa()
    return redirect(url_for("agenda"))


@app.route('/update/<int:idTarefa>', methods=['GET', 'POST'])
def update(idTarefa):

    if request.method == 'POST':
        titulo = request.form['titulo-tarefa']
        data_prevista = request.form['data-conclusao']

        if data_prevista == "":
            data_prevista = None

        tarefa = Tarefa(titulo, data_prevista, None, idTarefa)
        tarefa.atualizar_tarefa()

        return redirect(url_for('agenda'))

    tarefas = Tarefa.obter_tarefas()
    tarefa_selecionada = Tarefa.id(idTarefa)

    return render_template(
        'agenda.html',
        titulo=f'Editando tarefa {idTarefa}',
        tarefas=tarefas,
        tarefa_selecionada=tarefa_selecionada
    )


@app.route('/ola')
def ola_mundo():
    return "Olá, Mundo!"