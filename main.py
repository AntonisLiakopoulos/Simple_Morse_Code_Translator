from flask import Flask,render_template,request
from morse_code import CODE_DICT

reversed_code = {value: key for key, value in CODE_DICT.items()}

def morse_translator(text):
    output = []
    for letter in text.strip():
        if letter == " ":
            output.append("***")
        elif letter in CODE_DICT:
            output.append(CODE_DICT[letter])
    return (" ".join(output))

def reversed_translator(text):
    output=[]
    for letter in text.split(" "):
        if letter == "***":
            output.append(" ")
        elif letter in reversed_code:
            output.append(reversed_code[letter])
    return ("".join(output))


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/translation",methods=["POST"])
def translate():
    word = request.form["word"].upper()
    if "." in word or "-" in word:
            return reversed_translator(word)
    else:
        return morse_translator(word)


if __name__ == "__main__":
    app.run(debug=True, port=5001)