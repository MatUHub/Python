print("задача 2, программа вычисляет арифметические выражения, используя операции *, /, + , -")
text_fist = input("введите арифметическое выражение: ")
text = list(text_fist)
number = 0
for i in text:
    if i == ' ':
        text.remove(i)
def conclusion(text):
    if len(text) <= 1:
        print(f'выражение {text_fist} равно {"".join(text)}')
        exit()


def mult(text):
    conclusion(text)
    number = 0
    for i in range(len(text)):
        if "*" == text[i]:
            number = float(text[i-1]) * float(text[i+1])
            text[i-1] = str(number)
            text.pop(i)
            text.pop(i)
            break

def div(text):
    conclusion(text)
    number = 0
    for i in range(len(text)):
        if "/" == text[i]:
            number = float(text[i - 1]) / float(text[i + 1])
            text[i - 1] = str(number)
            text.pop(i)
            text.pop(i)
            break
def plus(text):
    conclusion(text)
    number = 0
    for i in range(len(text)):
        if "+" == text[i]:
            number = float(text[i - 1]) + float(text[i + 1])
            text[i - 1] = str(number)
            text.pop(i)
            text.pop(i)
            break

def sub(text):
    conclusion(text)
    number = 0
    for i in range(len(text)):
        if "-" == text[i]:
            number = float(text[i - 1]) - float(text[i + 1])
            text[i - 1] = str(number)
            text.pop(i)
            text.pop(i)
            break

while True:
    mult(text)
    div(text)
    plus(text)
    sub(text)

