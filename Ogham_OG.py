"""Takes Ogham text and renders it in Roman characters"""

oghamdict = {" ": " "}

aicmi = {"ᚊ": "Q", "ᚉ": "C", "ᚒ": "U", "ᚐ": "A", "ᚇ": "D", "ᚅ": "N", "ᚋ": "M", "ᚁ": "B", "ᚌ": "G", "ᚑ": "O",
         "ᚄ": "S", "ᚂ": "L", "ᚓ": "E", "ᚔ": "I", "ᚏ": "R", "ᚈ": "T"}

extendedaicmi = {"ᚕ": "K", "ᚆ": "J", "ᚍ": "GW", "ᚃ": "V", "ᚎ": "SW", "ᚖ": "TH"}

forfeda = {"ᚙ": "AE", "ᚚ": "P", "ᚖ": "OI", "ᚗ": "UI", "ᚘ": "IA", "ᚆ": "H", "ᚍ": "NG", "ᚎ": "Z", "ᚕ": "EA", "ᚃ": "F"}

forfedalist = ["ᚙ", "ᚚ", "ᚗ", "ᚘ"]

removables = ["᚛", "᚜"]


def aistrighogham(string, alphabet=None):
    if alphabet is None:
        alphabet = "orthodox"
        for letter in forfedalist:
            if letter in string:
                alphabet = "scholastic"
    if alphabet != "scholastic":
        alphabet = "orthodox"
    if alphabet == "orthodox":
        oghamdict.update(aicmi)
        oghamdict.update(extendedaicmi)
    elif alphabet == "scholastic":
        oghamdict.update(aicmi)
        oghamdict.update(forfeda)
    for character in string:
        charpos = string.find(character)
        if character in oghamdict:
            string = (string[:charpos]+oghamdict.get(character)+string[charpos+1:])
        if character in removables:
            string = (string[:charpos] + string[charpos + 1:])
    return string


# teststring1 = "᚛ᚊᚏᚔᚋᚔᚈᚔᚏ ᚏᚑᚅᚐᚅᚅ ᚋᚐᚊ ᚉᚑᚋᚑᚌᚐᚅᚅ\nᚊᚓᚅᚔᚂᚑᚉᚔ ᚋᚐᚊᚔ ᚋᚐᚊᚔ ᚐᚔᚅᚔᚐ ᚋᚒᚉ ᚃ᚜"
# teststring2 = "᚛ᚊᚏᚔᚋᚔᚈᚔᚏ ᚏᚑᚅᚐᚅᚅ ᚋᚐᚊ ᚉᚑᚋᚑᚌᚐᚅᚅ\nᚊᚓᚅᚔᚂᚑᚉᚔ ᚋᚐᚊᚔ ᚋᚐᚊᚔ ᚐᚔᚅᚘ ᚋᚒᚉ ᚃ᚜"
# print(aistrighogham(teststring1))
# print(aistrighogham(teststring1, "scholastic"))
# print(aistrighogham(teststring2))
# print(aistrighogham(teststring2, "scholastic"))
