from morse_code import CODE


reversed_code = {value: key for key, value in CODE.items()}

def morse_translator(text):
    output = []
    for letter in text.strip():
        if letter == " ":
            output.append("***")
        elif letter in CODE:
            output.append(CODE[letter])
    print(" ".join(output))

def reversed_translator(text):
    output=[]
    for letter in text.split(" "):
        if letter == "***":
            output.append(" ")
        elif letter in reversed_code:
            output.append(reversed_code[letter])
    print("".join(output))


word = input("What do you want me to translate?")

if "." in word or "-" in word:
    reversed_translator(word)
else:
    morse_translator(word)
