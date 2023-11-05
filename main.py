#Dalej programowanie funkcyjne
#dekoratorowi zazwyczaj wysyłamy jeden argument w postaci funkcji
def dekorator(func):
    #otoczka
    def wrapper():
        print("------")
        func()
        print("------")
    return wrapper

def hello():
    print("HELLO WORLD")

#zwykłe wywołanie funkcji
hello()

hello = dekorator(hello)
hello()


#łatwiejszy sposób

@dekorator
def witaj():
    print("Witaj Świecie")

witaj()

