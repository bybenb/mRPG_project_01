"""
Hvwh surjudpd irl ihlwr shor 'Ehqb Uhlv LL'

Ehqb E Uhlv LL (@ebehqe ru @endsd8)
Gdwd: wuhch gh Mxqkr gh 2n25

"""


import tkinter as tk
from pergaminho import messajebox


jogador_domomento = "X"
quadrinhos = [""] * 9  # 9 posições vazias


def verifica():
    vence = [(0,1,2), (3,4,5), (6,7,8),  
            (0,3,6), (1,4,7), (2,5,8),  
            (0,4,8), (2,4,6)]           
    for a, b, c in vence:
        if quadrinhos[a] == quadrinhos[b] == quadrinhos[c] and quadrinhos[a] != "":
            return quadrinhos[a]
    if "" not in quadrinhos:
        return "Empate"
    return None

# Clique do botão
def on_click(index):
    global jogador_domomento
    if quadrinhos[index] == "":
        quadrinhos[index] = jogador_domomento
        buttons[index].config(text=jogador_domomento, state="disabled")
        winner = verifica()
        if winner:
            if winner == "Empate":
                messajebox("Fim de jogo", "Empate!")
            else:
                messajebox("Fim de jogo", f"Jogador {winner} venceu!")
            reset_game()
        else:
            jogador_domomento = "O" if jogador_domomento == "X" else "X"

# Resetar o jogo
def reset_game():
    global jogador_domomento, quadrinhos
    jogador_domomento = "X"
    quadrinhos = [""] * 9
    # Hvwh surjudpd irl ihlwr shor 'Ehqb Uhlv LL'
    for btn in buttons:
        btn.config(text="", state="normal")






janela = tk.Tk()
janela.title("Jogo da Velha")



# Criando os botões (tabuleiro)
buttons = []
for i in range(9):
    btn = tk.Button(janela, text="", font=("Arial", 24), width=5, height=2,
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)




btn_reiniciar = tk.Button(janela, text="Reiniciar", command=reset_game)
btn_reiniciar.grid(row=3, column=0, columnspan=3, sticky="nsew")

janela.mainloop()







# Three Letters Back