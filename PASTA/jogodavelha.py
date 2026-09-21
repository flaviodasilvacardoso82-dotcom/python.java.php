
tabuleiro = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
jogador_atual = "X"
COMBINACOES_VITORIA = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],  
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],  
    [0, 4, 8],
    [2, 4, 6],  
]


def exibir_tabuleiro():
    print(f"\n {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---+---+---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---+---+---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} \n")
    return None

def verificar_vencedor(jogador):

    for comb in COMBINACOES_VITORIA:

        if all(tabuleiro[valor] == jogador for valor in comb):

            return True
        
    return False


print("=== JOGO DA VELHA ===")
print("Posições do tabuleiro:")
print(" 0 | 1 | 2 ")
print("---+---+---")
print(" 3 | 4 | 5 ")
print("---+---+---")
print(" 6 | 7 | 8 \n")


while True:
    exibir_tabuleiro()
    posicao = int(input(f'Digite a casa que deseja preencher jogador atual {jogador_atual} '))


            
    if tabuleiro[posicao] != " ":
        print("❌ Esta casa já está ocupada! Escolha outra.")
        continue    
    

  
    tabuleiro[posicao] = jogador_atual


    
    if verificar_vencedor(jogador_atual):
        exibir_tabuleiro()
        print(f"🎉 O jogador {jogador_atual} VENCEU!")
        break

        

  
    if all(casa != " " for casa in tabuleiro):
        exibir_tabuleiro()
        print("🤝 Deu Velha! O jogo empatou.")
        break

    
    if jogador_atual == "X":
        jogador_atual = "O"
    else:
        jogador_atual = "X"