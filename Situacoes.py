# ----- Situação 1 --------
# Todos os equipamentos "impressora" receberão uma desvalorização após certo periodo de 10%
# Monte o código que seria responsavel por alterar o valor de todos os equipamentos "impressora"

equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta=="S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta=input("Digite 'S' para continuar: ").upper()

for indice in range(0, len(equipamentos)):
    print("Equipamento: ", (indice+1))
    print("Nome: ", equipamentos[indice])
    print("Valor: ", valores[indice])
    print("Serial: ", seriais[indice])
    print("Departamento: ", departamentos[indice])

depreciacao = input("Digite o nome do equipamento que será deprecioado: ")
for indice in range(0, len(equipamentos)):
    if depreciacao==equipamentos[indice]:
        print("Valor antigo: ", valores[indice])
        valores[indice] = valores[indice] * 0.9
        print("Novo valor: ", valores[indice])

# ------------ Situação 2 ------------------------------
# Um equipamento com um determinado numero serial foi danificado e será descartado. 
# Precisamos eliminar esse equipamento 
# Dica: para eliminar um item de uma lista, voce utilizara o comando 'del' Ex: del lista[<indice>]