from flask import Flask, render_template, request, redirect, url_for
from check_winf import check_win
from check_impf import check_imp

app = Flask(__name__)

#estado do jogo
tab = [' '] * 9
jogador =  None
jogador1 = None
atual = None
messages = ["Welcome to Tic Tac Toe!"]

@app.route("/")
def index():
    return render_template("index.html", tab=tab, messages=messages, atual=atual)

@app.route("/escolher", methods=["POST"])
def escolher():
    global jogador, jogador1, atual
    escolha = request.form["simbolo"].upper()

    if escolha not in ["X", "O"]:
        messages.append("Invalid input. Choose between X and O.")
        return redirect(url_for("index"))
    
    jogador = escolha
    jogador1 = "O" if jogador == "X" else "X"
    atual = jogador
    messages.append(f"Player 1 chose {jogador}. Player 2 will be {jogador1}")
    return redirect(url_for("index"))

@app.route("/jogar", methods=["POST"])
def jogar():
    global tab, atual, jogador, jogador1

    try:
        pos = int(request.form["posicao"])
    except ValueError:
        messages.append("Insert a valid number (0-8).")
        return redirect(url_for("index"))
    
    if not check_imp(tab,atual, pos):
        messages.append("Invalid position, try again.")
        return redirect(url_for("index"))
    
    #verifica vitoria ou empate
    ganhou, vencedor =  check_win(tab)
    if ganhou == "empate":
        messages.append(f"The game ended in a draw.")
    elif ganhou:
        messages.append(f"Player {vencedor} won!")
    else:
        #alterna jogador
        atual = jogador1 if atual == jogador else jogador

    return redirect(url_for("index"))
@app.route("/reset")
def reset():
    global tab, atual, messages, jogador, jogador1
    tab = [' '] * 9
    atual = None
    jogador = None
    jogador1 = None
    messages = ["New game started"]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

