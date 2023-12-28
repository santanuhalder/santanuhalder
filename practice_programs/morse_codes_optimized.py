def morseCode(txt: str) -> str:
    encrypt = {
        "a":".-", "b":"-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
        "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-",
        "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."
    }
    decrypt = {val: key for key, val in encrypt.items()}

    if "-" in txt:
        return "".join(decrypt[i] for i in txt.split())
    else:
        return " ".join(encrypt[i] for i in txt)



input_string = "python"
input_morseCode = ".--. -.-- - .... --- -."
print(morseCode(input_string))
print(morseCode(input_morseCode))