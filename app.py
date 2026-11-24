"""Aplicação Flask: expõe a API REST do JOKENPÔ ARENA e serve o front-end."""
import os

from flask import Flask, jsonify, render_template, request

from jokenpo import (Jogo, JogadaInvalidaError, PartidaFinalizadaError,
                     PartidaNaoEncontradaError)

BASE = os.path.dirname(os.path.abspath(__file__))


def create_app(jogo=None):
    app = Flask(__name__)
    jogo = jogo or Jogo(os.path.join(BASE, "data", "estatisticas.json"))

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.get("/api/regras")
    def regras():
        return jsonify(jogo.regras())

    @app.get("/api/estatisticas")
    def estatisticas():
        return jsonify(jogo.estatisticas())

    @app.post("/api/partidas")
    def criar_partida():
        dados = request.get_json(silent=True) or {}
        partida = jogo.criar_partida(dados.get("modo"))
        return jsonify(partida.estado()), 201

    @app.get("/api/partidas/<partida_id>")
    def ver_partida(partida_id):
        return jsonify(jogo.obter_partida(partida_id).estado())

    @app.post("/api/partidas/<partida_id>/jogadas")
    def jogar(partida_id):
        dados = request.get_json(silent=True) or {}
        registro, estado = jogo.jogar(partida_id, dados.get("escolha"))
        return jsonify({"rodada": registro, "partida": estado, "estatisticas": jogo.estatisticas()})

    # -- erros sempre em JSON
    @app.errorhandler(JogadaInvalidaError)
    def invalida(e):
        return jsonify(erro=str(e)), 400

    @app.errorhandler(PartidaNaoEncontradaError)
    def nao_encontrada(e):
        return jsonify(erro="Partida não encontrada."), 404

    @app.errorhandler(PartidaFinalizadaError)
    def finalizada(e):
        return jsonify(erro=str(e)), 409

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
