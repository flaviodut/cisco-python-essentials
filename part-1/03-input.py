#1 - input
print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

#2 - mensagem como argumento
anything = input("Tell me anything...\n")
print("Hmm...", anything, "...Really?")

#3 - todo valor digitado é recebido como uma string
anything = input("Digite um número > ")
print(anything ** 2)

#4 - int(str) float(str)
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

#5
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)

#6 - concatenação
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")
print("Your name is", fnam, lnam, end=".")

#7 - multiplicacao de string
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

#8 - str()
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))
