"""Takes Ogham text and renders it in Roman characters"""

oghamdict = {" ": " "}

aicmi = {"ᚊ": "Q", "ᚉ": "C", "ᚒ": "U", "ᚐ": "A", "ᚇ": "D", "ᚅ": "N", "ᚋ": "M", "ᚁ": "B", "ᚌ": "G", "ᚑ": "O",
         "ᚄ": "S", "ᚂ": "L", "ᚓ": "E", "ᚔ": "I", "ᚃ": "F", "ᚏ": "R", "ᚈ": "T"}

extendedaicmi = {"ᚕ": "K", "ᚆ": "J", "ᚍ": "GW", "ᚎ": "SW", "ᚖ": "TH"}

forfeda = {"ᚙ": "AE", "ᚚ": "P", "ᚖ": "OI", "ᚗ": "UI", "ᚘ": "IA", "ᚆ": "H", "ᚍ": "NG", "ᚎ": "Z", "ᚕ": "EA"}

forfedalist = ["ᚙ", "ᚚ", "ᚗ", "ᚘ"]

removables = ["᚛", "᚜"]


def aistrighogham(string):
    for letter in forfedalist:
        if letter in string:
            oghamdict.update(aicmi)
            oghamdict.update(forfeda)
        else:
            oghamdict.update(aicmi)
            oghamdict.update(extendedaicmi)
    for character in string:
        charpos = string.find(character)
        if character in oghamdict:
            string = (string[:charpos]+oghamdict.get(character)+string[charpos+1:])
        if character in removables:
            string = (string[:charpos] + string[charpos + 1:])
    return string


# teststring = "᚛ᚊᚏᚔᚋᚔᚈᚔᚏ ᚏᚑᚅᚐᚅᚅ ᚋᚐᚊ ᚉᚑᚋᚑᚌᚐᚅᚅ\nᚊᚓᚅᚔᚂᚑᚉᚔ ᚋᚐᚊᚔ ᚋᚐᚊᚔ ᚐᚔᚅᚔᚐ ᚋᚒᚉ᚜\n" \
#              "᚛ᚊᚏᚔᚋᚔᚈᚔᚏ ᚏᚑᚅᚐᚅᚅ ᚋᚐᚊ ᚉᚑᚋᚑᚌᚐᚅᚅ\nᚊᚓᚅᚔᚂᚑᚉᚔ ᚋᚐᚊᚔ ᚋᚐᚊᚔ ᚐᚔᚅᚘ ᚋᚒᚉ᚜"
# print(aistrighogham(teststring))
