estado = int(input("Qual o código do estado de origem da carga do caminhão? "))
peso = float(input("Qual o peso da carga do caminhão, em toneladas? "))
codigo = int(input("Digite o código da carga: "))

pesoCargaKg = peso * 1000

if (codigo <=20):
    precoPorKg = 100
if (codigo >20 and codigo<=30):
    precoPorKg = 250
if (codigo >30 and codigo<=40):
    precoPorKg = 340

if (estado == 1):
    imposto = 0.35
if (estado == 2):
    imposto = 0.25
if (estado == 3):
    imposto = 0.15
if (estado == 4):
    imposto = 0.05
if (estado == 5):
    imposto = 0
precoDaCarga = precoPorKg * pesoCargaKg
valorTotal = precoDaCarga + (precoDaCarga * imposto)
print(f'O valor total transportado é de {valorTotal} R$')