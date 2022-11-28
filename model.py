
otvet = ""


def calculation(text_first):
    text = list(text_first)
    for i in text:
        if i == ' ':
            text.remove(i)

    def conclusion(text):
        global otvet
        if len(text) <= 1:
            print(f'выражение {text_first} равно {"".join(text)}')
            ot = "".join(text)
            otvet = f"ответ {ot}"
            return False

    def mult(text):
        if conclusion(text) == False:
            return False
        else:
            for i in range(len(text)):
                if "*" == text[i]:
                    number = float(text[i - 1]) * float(text[i + 1])
                    text[i - 1] = str(number)
                    text.pop(i)
                    text.pop(i)
                    break

    def div(text):
        if conclusion(text) == False:
            return False
        else:
            for i in range(len(text)):
                if "/" == text[i]:
                    number = float(text[i - 1]) / float(text[i + 1])
                    text[i - 1] = str(number)
                    text.pop(i)
                    text.pop(i)
                    break

    def plus(text):
        if conclusion(text) == False:
            return False
        else:
            for i in range(len(text)):
                if "+" == text[i]:
                    number = float(text[i - 1]) + float(text[i + 1])
                    text[i - 1] = str(number)
                    text.pop(i)
                    text.pop(i)
                    break

    def sub(text):
        if conclusion(text) == False:
            return False
        else:
            for i in range(len(text)):
                if "-" == text[i]:
                    number = float(text[i - 1]) - float(text[i + 1])
                    text[i - 1] = str(number)
                    text.pop(i)
                    text.pop(i)
                    break

    while True:

       if mult(text) == False:
           return False
       if div(text) == False:
           return False
       if plus(text) == False:
           return False
       if sub(text) == False:
           return False