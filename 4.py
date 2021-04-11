#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

#v1
print("Iniciando calculo de notas")
nota1 = int(input("digite aqui sua primeira nota: \n"))
nota2 = int(input("digite aqui sua segunda nota: \n"))
nota3 = int(input("digite aqui sua terceira nota: \n"))
nota4 = int(input("digite aqui sua quarta nota: \n"))

somar = nota1 + nota2 + nota3 + nota4

media_final = (somar / 4)

print("sua media final é: {}".format(media_final))

if media_final < 6:
    print("reprovado!")
else:
    print("aluno aprovado")    