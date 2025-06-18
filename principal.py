"""
Hvwh surjudpd irl ihlwr shor 'Ehqb Uhlv LL'

Ehqb E Uhlv LL (@ebehqe ru @endsd8)
Gdwd: wuhch gh Mxqkr gh 2n25

"""


import tkinter as tekinte
from tkinter import ttk
from pergaminho import messajebox, toqueo_som

# -------------------------------------------------- Variáveis globais # ---------------------------------------------------------------
jogador_domomento = "X"
quadrinhos = [""] * 9
score = {"X": 0, "O": 0}
nomes = {"X": "Jogador X", "O": "Jogador O"}
buttons = []

# --------------------------------------------------Funcoes -------------------------------------------------- 
def verifica():
    vence = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for a, b, c in vence:
        if quadrinhos[a] == quadrinhos[b] == quadrinhos[c] and quadrinhos[a] != "":
            return quadrinhos[a], (a, b, c)
    if "" not in quadrinhos:
        return "Empate", ()
    return None, ()

# Animação de vitória
def animar_vitoria(cells, conta=0):
    cor = ["#00FF00", "#FFFFFF"]
    if conta < 6:
        for i in cells:
            buttons[i].config(background=cor[conta % 2])
        janela.after(300, lambda: animar_vitoria(cells, conta + 1))
    else:
        for i in cells:
            buttons[i].config(background="SystemButtonFace")


def animar_tabuleiro(i=0):
    if i < len(buttons):
        buttons[i].grid()
        janela.after(100, lambda: animar_tabuleiro(i + 1))

# Clique no botão
def on_click(index):
    global jogador_domomento
    if quadrinhos[index] == "":
        toqueo_som("ouvido/clique.mp3")
        quadrinhos[index] = jogador_domomento
        buttons[index].config(text=jogador_domomento, state="disabled", foreground="blue" if jogador_domomento == "X" else "red")
        vence, combo = verifica()
        if vence:
            if vence == "Empate":
                toqueo_som("ouvido/empate.mp3")
                messajebox("Empate", "O jogo terminou empatado.")
            else:
                toqueo_som("ouvido/vitori.mp3")
                score[vence] += 1
                atualizar_score()
                animar_vitoria(combo)
                janela.after(2000, lambda: messajebox("Vitória", f"{nomes[vence]} venceu!"))
            janela.after(2500, reset_game)
        else:
            jogador_domomento = "O" if jogador_domomento == "X" else "X"
            player_label.config(text=f"Vez de: {nomes[jogador_domomento]}")


def reset_game():
    global jogador_domomento, quadrinhos
    jogador_domomento = "X"
    quadrinhos = [""] * 9
    for btn in buttons:
        btn.config(text="", state="normal", background="SystemButtonFace")
    player_label.config(text=f"Vez de: {nomes[jogador_domomento]}")


def atualizar_score():
    label_scorex.config(text=f"{nomes['X']}: {score['X']}")
    label_scoreo.config(text=f"{nomes['O']}: {score['O']}")


def iniciar_jogo():
    nomes["X"] = entrada_jogadorx.get() or "Jogador X"
    nomes["O"] = entrada_jogadoro.get() or "Jogador O"
    janela.destroy()
    construir_tabuleiro()


def construir_tabuleiro():
    global janela, frame_principal, frame_score, label_scorex, label_scoreo, player_label, buttons

    janela = tekinte.Tk()
    janela.title("X Ball   XOXO")
    janela.geometry("410x420")
    janela.resizable(False, False)

    beleza = ttk.Style(janela)
    beleza.theme_use("vista")

    frame_principal = ttk.Frame(janela, padding=10)
    frame_principal.pack()

    frame_score = ttk.Frame(frame_principal)
    frame_score.grid(row=0, column=0, columnspan=3, pady=(0, 10))

    label_scorex = ttk.Label(frame_score, text="", font=("Arial", 12))
    label_scoreo = ttk.Label(frame_score, text="", font=("Arial", 12))
    player_label = ttk.Label(frame_score, text="", font=("Arial", 12, "bold"))

    label_scorex.grid(row=0, column=0, padx=10)
    player_label.grid(row=0, column=1, padx=10)
    label_scoreo.grid(row=0, column=2, padx=10)

    atualizar_score()
    player_label.config(text=f"Vez de: {nomes[jogador_domomento]}")

    # Botões do tabuleiro inicialmente ocultos
    buttons.clear()
    for i in range(9):
        btn = tekinte.Button(frame_principal, relief="ridge", text="", width=10,
                             command=lambda i=i: on_click(i))
        btn.grid(row=1 + i//3, column=i%3, padx=5, pady=5, ipadx=10, ipady=10)
        btn.grid_remove() 
        buttons.append(btn)


    btn_reiniciar = tekinte.Button(frame_principal, relief="ridge", text="Reiniciar Jogo", command=reset_game)
    btn_reiniciar.grid(row=4, column=0, columnspan=3, pady=(15, 0), sticky="nsew")

    
    animar_tabuleiro()

    janela.mainloop()

# TELA INICIAL
janela = tekinte.Tk()
janela.title("Bem-vindo ao X Ball!")
janela.geometry("300x200")
janela.resizable(False, False)

ttk.Label(janela, text="Nome do Jogador X:").pack(pady=5)
entrada_jogadorx = ttk.Entry(janela)
entrada_jogadorx.pack()

ttk.Label(janela, text="Nome do Jogador O:").pack(pady=5)
entrada_jogadoro = ttk.Entry(janela)
entrada_jogadoro.pack()

ttk.Button(janela, text="Começar Jogo", command=iniciar_jogo).pack(pady=20)
credits = ttk.Label(frame_score, text="", font=("Arial", 12))

janela.mainloop()
# Three Letters Back