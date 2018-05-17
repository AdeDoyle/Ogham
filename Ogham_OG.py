"""Takes Ogham text and renders it in Roman characters"""

oghamdict = {" ": " "}

aicmi = {"ᚊ": "Q", "ᚉ": "C", "ᚒ": "U", "ᚐ": "A", "ᚍ": "NG", "ᚇ": "D", "ᚅ": "N", "ᚋ": "M", "ᚁ": "B", "ᚌ": "G", "ᚑ": "O",
         "ᚄ": "S", "ᚂ": "L", "ᚓ": "E", "ᚔ": "I", "ᚃ": "F", "ᚏ": "R", "ᚈ": "T", "ᚆ": "H", "ᚎ": "Z"}

forfeda = {"ᚙ": "AE", "ᚚ": "P", "ᚖ": "OI", "ᚗ": "UI", "ᚘ": "IA", "ᚕ": "EA"}

removables = ["᚛", "᚜"]

def aistrighogham(string):
    oghamdict.update(aicmi)
    oghamdict.update(forfeda)
    for character in string:
        charpos = string.find(character)
        if character in oghamdict:
            string = (string[:charpos]+oghamdict.get(character)+string[charpos+1:])
        if character in removables:
            string = (string[:charpos] + string[charpos + 1:])
    return string


# teststring ="᚛ᚊᚏᚔᚋᚔᚈᚔᚏ ᚏᚑᚅᚐᚅᚅ ᚋᚐᚊ ᚉᚑᚋᚑᚌᚐᚅᚅ\nᚊᚓᚅᚔᚂᚑᚉᚔ ᚋᚐᚊᚔ ᚋᚐᚊᚔ ᚐᚔᚅᚔᚐ ᚋᚒᚉ᚜\n" \
#             "᚛ᚊᚏᚔᚋᚔᚈᚔᚏ ᚏᚑᚅᚐᚅᚅ ᚋᚐᚊ ᚉᚑᚋᚑᚌᚐᚅᚅ\nᚊᚓᚅᚔᚂᚑᚉᚔ ᚋᚐᚊᚔ ᚋᚐᚊᚔ ᚐᚔᚅᚘ ᚋᚒᚉ᚜"
# print(aistrighogham(teststring))
