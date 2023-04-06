import json

#Exercicio 2
def verificarFibonaci(numero):
    x = 0
    y = 1
    while (True):
        if numero == x:
            return True
        elif numero < x:
            return False
        aux = y
        y = x + y
        x = aux
    return False
#Exercico 3
def mediaFatura(arq):
        file = open(arq)
        arquivo = json.load(file)
        total = 0
        totalDias = 0
        maiorFaturamento = 0
        diaMMedia = 0
        for dia in arquivo:
            if(int(arquivo[dia])  != 0):
                total += arquivo[dia]
                totalDias += 1
                if(arquivo[dia] > maiorFaturamento):
                    maiorFaturamento = arquivo[dia]
        media = total / totalDias
        menorFaturamento = maiorFaturamento
        for dia in arquivo:
            if (arquivo[dia] > 0):
                diaMMedia += 1
                if (arquivo[dia] < menorFaturamento):
                    menorFaturamento = arquivo[dia]

        print("Maior Faturamento: "+ str(maiorFaturamento))
        print("Menor Faturamento: " + str(menorFaturamento))
        print("Media Faturamento: " + str(media))
        print("Dias superior a Media: " + str(diaMMedia))
        file.close()
        return 0
#Exercico 4
def porcEstado(arq):
        file = open(arq)
        arquivo = json.load(file)
        total = 0
        for cidade in arquivo:
            total += arquivo[cidade]
        for cidade in arquivo:
            print(cidade + ": "+ str(100 / (total / arquivo[cidade])) + "%")
        file.close()
        return 0
#Execico 5
def strReverse(str):
    reverseStr = ""
    for char in str:
        reverseStr = char + reverseStr
    return reverseStr
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(verificarFibonaci(4))
    mediaFatura("exercicio3.json")
    porcEstado("exercicio4.json")
    print(strReverse("jonas"))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
