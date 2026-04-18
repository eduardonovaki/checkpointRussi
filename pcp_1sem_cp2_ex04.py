# FUNÇÕES OBRIGATÓRIAS
################################################################################
def calcular_horas_extras(salario_base, horas):
    return salario_base *0.015* horas
################################################################################
def calcular_descontos_faltas(salario_base, faltas):
    return salario_base *0.02* faltas
################################################################################
def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus.lower() == 's':
        if cargo ==1:
            return 1.000
        elif cargo ==2:
            return 500
        elif cargo ==3:
            return 300
        elif cargo ==4:
            return 100
    return 0.0
################################################################################
# PROGRAMA PRINCIPAL
nome = input("Digite seu nome: ")
cargo = int(input("Digite seu cargo(1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário): "))
salario_base = float(input("Salário base: "))
horas_extras = float(input("Total de horas extras: "))
faltas = int(input("Total de faltas: "))
recebeu_bonus_input = input(("Recebeu bônus? (s/n): "))

#################################################################################
# CHAMANDO AS FUNÇÕES
valores_extras = calcular_horas_extras(salario_base, horas_extras)
valores_faltas = calcular_descontos_faltas(salario_base, faltas)
valores_bonus = calcular_bonus(cargo, recebeu_bonus_input)

################################################################################
# CONTAS FINAIS
total_acrescentar = valores_extras + valores_bonus
salario_final = salario_base + total_acrescentar - valores_faltas

###############################################################################
#RESULTADO
print (f"Salário Bruto: R${salario_base:.2f}")
print (f"Acréscimos: R${total_acrescentar:.2f}")
print (f"Descontos: R${valores_faltas:.2f}")
print (f"Salário final: R${salario_final:.2f}")

###############################################################################



















