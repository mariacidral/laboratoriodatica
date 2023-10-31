#aqui podemos ver como concatenar strings:

x = "andré"
y = "maria"

print(x + " ama muito a " + y) #eu amo muito a maria


###############################

x = ["andré", "maria", "tuco", "tica"]
numero_de_cheirinhos = 0
for pessoa in x:
    for outra_pessoa in x:
        if pessoa != outra_pessoa:
            print(pessoa + " dá cheirinhos em " + outra_pessoa)
            numero_de_cheirinhos = numero_de_cheirinhos + 1

print(numero_de_cheirinhos)

##############################

