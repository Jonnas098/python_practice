#Dos palabras por segundo

#A- Pedirle al usuaio que diga cualquier texto real y:
# - Calcular cuanto tardaria en decir esa frase
# - Cuantas palabras dijo?
#B- Si tarda mas de 1 minuto
# - Decirle: "Habla menos"
#C- Dalto habla un 30% mas rapido:
# - Cuanto tardaria en decirlo?

frase = input("Dime una frase: ")
separed_words = frase.split(" ")
total_words = len(separed_words)

if total_words > 120:
    print("Debes de hablar menos")

print(f'Dijiste {total_words} palabras y tardarias {total_words/2} segundos en decirlo')
print(f'Dalto tardaria {total_words * 100 // 2 /1.3 /100} segundos en decir la misma frase')


