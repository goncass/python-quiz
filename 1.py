print ('Bem vindo ao meu Quiz.')

playing = input("Quer jogar?")
if playing.lower () != "sim":
    quit()


print ("Ok! Vamos jogar :)")
score = 0

answer = input("Qual é a capital de França? ")
if answer.title () == "Paris":
    print("Correto!")
    score += 1
else:
    print("Errado!")
answer = input("Qual é o maior planeta do Sistema Solar? ")
if answer.title() == "Júpiter":
    print("Correto!")
    score +=2
else:
    print('Incorreto!')
answer = input ("Em que ano terminou a Segunda Guerra Mundial? ")
if answer.strip() == "1945":
    print("Correto!")
    score +=3
else:
    print("Incorreto!")

answer = input ("Quantos lados tem um hexágono? ")
if answer.strip () == "6":
    print ('Correto!')
    score += 1
else:
    print ('Incorreto!')

answer = input ('Qual é o elemento químico cujo símbolo é Au? ')
if answer.title() == 'Ouro':
    print ('Correto!')
    score +=2
else:
    print('Incorreto!')

answer = input ("Qual é a capital do Cazaquistão? ")
if answer.title () == "Astana":
    print ('Correto!')
    score +=3
else: 
    print ('Incorreto!')

print ("Voce acertou " + str(score) + " respostas")
print ("Voce teve " + str((score/6)*100) + " %.")