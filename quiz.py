print("Seja muito bem vindo ao quiz")
começar = input("Deseja começar? (S/N) ")

if começar != "S":
    print("utilize S maiúsculo")
    quit()

score = 0

print("Começando....")
print("Qual é o símbolo químico do elemento Ouro? \n a) Au \n b) Ag \n c) O \n d) Hg" )
resposta1 = input("resposta: ")

if resposta1 == "a":
    print("---------------")
    print("você acertou!")
    print("---------------")
    score = score + 1
else:
    print("---------------")
    print("você errou!")
    print("---------------")

print("Qual é o pH de uma solução neutra? \n a) 0 \n b) 10 \n c) 14 \n d) 7" )
resposta2 = input("resposta: ")

if resposta2 == "d":
    print("---------------")
    print("você acertou!")
    print("---------------")
    score = score + 1
else:
    print("---------------")
    print("você errou!")
    print("---------------")


print("Qual gás é mais abundante na atmosfera da Terra? \n a) Oxigênio \n b) Nitrogênio \n c) Dióxido de carbono \n d) Hidrogênio" )
resposta3 = input("resposta: ")

if resposta3 == "b":
    print("---------------")
    print("você acertou!")
    print("---------------")
    score = score + 1
else:
    print("---------------")
    print("você errou!")
    print("---------------")


print("Qual é o nome da ligação química formada pelo compartilhamento de elétrons? \n a) Ligação iônica \n b) Ligação covalente \n c) Ligação metálica \n d) Ligação de hidrogênio" )
resposta4 = input("resposta: ")

if resposta4 == "b":
    print("---------------")
    print("você acertou!")
    print("---------------")
    score = score + 1
else:
    print("---------------")
    print("você errou!")
    print("---------------")


print("Qual é a unidade básica da matéria? \n a) Molécula \n b) Íon  \n c) Átomo \n d) Próton" )
resposta5 = input("resposta: ")

if resposta5 == "c":
    print("---------------")
    print("você acertou!")
    print("---------------")
    score = score + 1
else:
    print("---------------")
    print("você errou!")
    print("---------------")

if score == 5:
    print("Parabéns você acertou Todas as Respostas tome um bolo 🍰" )
else: 
    print(f"Você acertou  {score} / 5 tente novamente.")