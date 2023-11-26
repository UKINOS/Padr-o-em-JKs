### Socorro, estou enlouquecendo :)


### Funções:
## Verifica se a resposta esta correta (e também serve como organização para listas)
# Se o valor de lista_locassa for igual a "-69", ele pula o check de procurar na lista:v
def resposta_correta(tamanho_mínimo, tamanho_máximo, lista_locassa):
    while True:
        resposta = input()
        if resposta.isdigit() == True:
            resposta = int(resposta)
            if tamanho_mínimo <= resposta <= tamanho_máximo:
                if lista_locassa == -69:
                    return resposta
                else:
                    if resposta not in lista_locassa:
                        lista_locassa.append(resposta)
                        return resposta
                    else:
                        print(f"O seu número tem que ser um que não está na lista (vc tem números entre {tamanho_mínimo} e {tamanho_máximo})")
            else:
                print(f"Escreva um valor entre {tamanho_mínimo} e {tamanho_máximo}, e que não seja um dos números já usados:")

## Printa uma linha de respostas
def printando_tabela(offset, tamanho, lista_principal):
    lista_coluna_11 = list(range(2, 16, 4))
    lista_coluna_10 = list(range(3, 16, 4))
    if tamanho > 2:
        for n in range((0 + offset), (4 + offset)):
            if n in lista_coluna_11:
                consertado = conserto(lista_de_números, (n + 1))
            elif n in lista_coluna_10:
                consertado = conserto(lista_de_números, (n - 1))
            else:
                consertado = conserto(lista_de_números, n)
            print(lista_principal[consertado], end=" ")
        print()
    else:
        print(f"{lista_principal[0]}  {lista_principal[1]}\n{lista_principal[2]}  {lista_principal[3]}")

## Como isso iria repetir várias e várias vezes, eu já coloquei em sua própria função
def preparação_para_printar(lista):
    printando_tabela(0, JKs, lista)
    if JKs > 2:
        printando_tabela(4, JKs, lista)
        if JKs > 3:
            printando_tabela(12, JKs, lista)
            printando_tabela(8, JKs, lista)

## Loucura
def loucura_para_JK(lista1, linha, lista_de_mudanças_J, lista_de_mudanças_K):
    for n in range(0,(len(lista1))):
        valor = lista1[n]
        valor_lista = list(valor)
        
        m = (int(n)) + 1
        if m >= len(lista1):
            m = 0
        
        valor2 = lista1[m]
        valor2_lista = list(valor2)

        if valor_lista[linha] == '0':
            if valor2_lista[linha] == '1':
                lista_de_mudanças_J.append('1')
            else:
                lista_de_mudanças_J.append('0')
            lista_de_mudanças_K.append('X')

        else:
            if valor2_lista[linha] == '1':
                lista_de_mudanças_K.append('0')
            else:
                lista_de_mudanças_K.append('1')       
            lista_de_mudanças_J.append('X')

## Conserto :)
def conserto(lista69, número):
    for n in range(0,len(lista69)):
        if lista69[n] == número:
            return n


### Configuração
print("Escolha quantos JKs (Bits) vc irá usar:")
JKs = resposta_correta(2,4, -69)

print(f"Você escolheu que vai calcular {JKs} JKs...")

lista_de_números = [0]
if   JKs == 2: Final = 3
elif JKs == 3: Final = 7
else:          Final = 15

print("Agora, me fale todos os elementos da sua lista\nLembrando que os elemento 0 é adicionando ao começo e você não pode repetir elementos...")
for n in range(0, (Final)):
    print(f"Escreva o número do elemento {n + 1}:")
    resposta_correta(0,(Final),lista_de_números)
    print(lista_de_números, "\n")

# Por favor, faça o favor de me organizar uma tabela com os valores q eu preciso -Daniel para Daniel :)
lista_de_números_mas_binario = []

for n in lista_de_números: #Bing me deu uma ajuda nessa aqui (put****** não sabia q tinha isso)
    números_mas_em_binario = bin(n)[2:]
    números_mas_em_binario = números_mas_em_binario.zfill(JKs)
    lista_de_números_mas_binario.append(números_mas_em_binario)

J0 = []; K0 = []; J1 = []; K1 = []

loucura_para_JK(lista_de_números_mas_binario, (JKs - 1), J0, K0)
loucura_para_JK(lista_de_números_mas_binario, (JKs - 2), J1, K1)
if JKs > 2:
    J2 = []; K2 = []
    
    loucura_para_JK(lista_de_números_mas_binario, (JKs - 3), J2, K2)
    if JKs > 3:
        J3 = []; K3 = []
        
        loucura_para_JK(lista_de_números_mas_binario, (JKs - 4), J3, K3)


## Printando coisas
# binário
print("\n\nAqui seus valores em binário:")
for n in range(0, Final + 1):
    if lista_de_números[n] < 10:
        print(end=" ")
    print(lista_de_números[n], end=" = ")
    print(lista_de_números_mas_binario[n])

# Valores de 0, 1 e X para cada um
print("\n\nAqui uma lista de 0, 1 e X para cada valor :)")
print(end="     ")

if JKs > 3: 
    print("J3  K3", end="    ")
    
if JKs > 2:
    print("J2  K2", end="    ")
    
print("J1  K1    J0  K0")

for n in range(0, len(J0)):
    if lista_de_números[n] < 10:
        print(end=" ")
    print(f"{lista_de_números[n]} =  ",end="")
    
    if JKs > 3:
        print(J3[n], end="   ")
        print(K3[n], end="     ")
    if JKs > 2:
        print(J2[n], end="   ")
        print(K2[n], end="     ")
        
    print(J1[n], end="   ")
    print(K1[n], end="     ")
    print(J0[n], end="   ")
    print(K0[n], end="     ")
    
    print()

# tabela
print("\n\nAqui estão suas tabelas :)")

print("\nJ0")
preparação_para_printar(J0)

print("\nK0")
preparação_para_printar(K0)

print("\nJ1")
preparação_para_printar(J1)

print("\nK1")
preparação_para_printar(K1)

if JKs > 2:
    print("\nJ2")
    preparação_para_printar(J2)
    
    print("\nK2")
    preparação_para_printar(K2)
    
    if JKs > 3:
        print("\nJ3")
        preparação_para_printar(J3)
        
        print("\nK3")
        preparação_para_printar(K3)

input("Aperte enter para fechar o código...")