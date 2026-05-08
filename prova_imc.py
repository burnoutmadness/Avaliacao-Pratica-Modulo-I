#programa para calcular IMC
nome = input ("Digite o seu nome: ")
print ( )
print ("Nome registrado:", nome)
print ( )
idade = input ("Digite a sua idade: ")
print ( )
print ("Idade registrada:", idade)
print ( )
#^ informações basicas
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
print (f"O seu peso é", peso)
print (f"A sua altura é", altura)
IMC = peso / (altura ** 2) #conta
print(f"IMC: {IMC:.2f}") #print com formatação
if IMC >= 30.0:
    print("Cuidado com a sua saúde.")
elif IMC <= 30.0:
    print ("Tudo ok.")
