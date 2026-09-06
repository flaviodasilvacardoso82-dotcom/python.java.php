
# Exercício - Adiando execução de funções
def soma(y,x):
    return y + x   

def criar_funcao(funcao,x):
    def interna(y):
        return funcao(x,y)
    return interna
        




soma_com_cinco = criar_funcao(soma,2)
print(soma_com_cinco(5))