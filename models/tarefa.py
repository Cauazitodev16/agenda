from models.database import Database
from typing import Self
from sqlite3 import Cursor

class Tarefa:

    def __init__(self,
                 titulo_tarefa: str,
                 data_prevista: str | None = None,
                 data_conclusao: str | None = None,
                 id_tarefa: int | None = None) -> None:
        
        self.titulo_tarefa = titulo_tarefa
        self.data_prevista = data_prevista
        self.data_conclusao = data_conclusao
        self.id_tarefa = id_tarefa

    @classmethod
    def id(cls, id: int) -> Self:
        with Database() as db:
            query = """
            SELECT titulo_tarefa, data_prevista, data_conclusao
            FROM tarefas WHERE id = ?;
            """
            resultado = db.buscar_tudo(query, (id,))
            [[titulo, data_prevista, data_conclusao]] = resultado
        
        return cls(titulo, data_prevista, data_conclusao, id)

    def salvar_tarefa(self) -> None:
        with Database() as db:
            query = """
            INSERT INTO tarefas (titulo_tarefa, data_prevista, data_conclusao)
            VALUES (?, ?, ?);
            """
            params = (self.titulo_tarefa, self.data_prevista, None)
            db.executar(query, params)

    @classmethod
    def obter_tarefas(cls) -> list[Self]:
        with Database() as db:
            query = """
            SELECT titulo_tarefa, data_prevista, data_conclusao, id
            FROM tarefas;
            """
            resultados = db.buscar_tudo(query)

            tarefas = [
                cls(titulo, data_prevista, data_conclusao, id)
                for titulo, data_prevista, data_conclusao, id in resultados
            ]
            return tarefas

    def excluir_tarefa(self) -> Cursor:
        with Database() as db:
            return db.executar(
                'DELETE FROM tarefas WHERE id = ?;',
                (self.id_tarefa,)
            )

    def concluir_tarefa(self) -> Cursor:
        with Database() as db:
            return db.executar(
                'UPDATE tarefas SET data_conclusao = date("now") WHERE id = ?;',
                (self.id_tarefa,)
            )

    def atualizar_tarefa(self) -> Cursor:
        with Database() as db:
            return db.executar(
                '''
                UPDATE tarefas
                SET titulo_tarefa = ?, data_prevista = ?
                WHERE id = ?;
                ''',
                (self.titulo_tarefa, self.data_prevista, self.id_tarefa)
            )