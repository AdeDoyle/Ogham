"""Takes regular text and renders it in either orthodox or scholastic Ogham"""

oghamdict = {" ": " "}

aicmi = {"B": "ᚁ", "L": "ᚂ", "F": "ᚃ", "S": "ᚄ", "N": "ᚅ", "H": "ᚆ", "D": "ᚇ", "T": "ᚈ", "C": "ᚉ", "Q": "ᚊ", "M": "ᚋ",
         "G": "ᚌ", "NG": "ᚍ", "Z": "ᚎ", "R": "ᚏ", "A": "ᚐ", "O": "ᚑ", "U": "ᚒ", "E": "ᚓ", "I": "ᚔ"}

forfeda = {"EA": "ᚕ", "OI": "ᚖ", "UI": "ᚗ", "IA": "ᚘ", "AE": "ᚙ", "P": "ᚚ"}

fada = {"Á": "ᚐ", "Ó": "ᚑ", "Ú": "ᚒ", "É": "ᚓ", "Í": "ᚔ"}

lettercombos = ["NG", "EA", "OI", "UI", "IA", "AE"]

removables = [".", ",", "'", '"', "!", "?", "(", ")"]


def findnth(string, character, n):
    splits = string.split(character, n+1)
    if len(splits) <= n+1:
        return -1
    return len(string) - len(splits[-1]) - len(character)


def deanogham(string, alphabet=None):
    """Sets the available ogham characters in accordance with the type of ogham selected, orthodox as default"""
    if alphabet is None:
        alphabet = "orthodox"
    if alphabet != "scholastic":
        alphabet = "orthodox"
    if alphabet == "orthodox":
        oghamdict.update(aicmi)
        oghamdict.update(fada)
    elif alphabet == "scholastic":
        oghamdict.update(aicmi)
        oghamdict.update(forfeda)
        oghamdict.update(fada)
    """Ogham does not distinguish between upper and lower case letters, all letters are upper case"""
    string = string.upper()
    """all strings of ogham begin and end with designated markers"""
    string = ("᚛" + string[:] + "᚜")
    """Identifies a list of characters which will not be removed during the conversion to ogham"""
    allowed = ["᚛", " ", "-", "\n", "(", "᚜"]
    for let in oghamdict:
        allowed.append(oghamdict.get(let))
    for item in removables:
        allowed.append(item)
    """Finds and changes letter combinations which represent one ogham letter from latin alphabet to ogham"""
    for combo in lettercombos:
        if combo in oghamdict:
            if combo in string:
                comcount = string.count(combo)
                for i in range(comcount):
                    compos = string.find(combo)
                    string = string[:compos] + oghamdict.get(combo) + string[compos+2:]
    """Changes characters which exist in ogham from latin alphabet to ogham"""
    for character in string:
        charpos = string.find(character)
        if character in oghamdict:
            string = (string[:charpos]+oghamdict.get(character)+string[charpos+1:])
        """Removes select non-letter characters"""
        if character in removables:
            string = (string[:charpos]+string[charpos+1:])
    """Brackets off substrings of characters which cannot be translated to ogham"""
    newstring1 = string
    done1lets = []
    for character in newstring1:
        if character not in allowed:
            done1lets.append(character)
            charitir1 = done1lets.count(character)
            charno1 = charitir1 - 1
            charpos1 = findnth(newstring1, character, charno1)
            if newstring1[charpos1 - 1] in allowed:
                newstring1 = newstring1[:charpos1] + "(" + newstring1[charpos1:]
    newstring2 = newstring1
    done2lets = []
    for character in newstring2:
        if character not in allowed:
            done2lets.append(character)
            charitir2 = done2lets.count(character)
            charno2 = charitir2 - 1
            charpos2 = findnth(newstring2, character, charno2)
            if newstring2[charpos2 + 1] in allowed:
                newstring2 = newstring2[:charpos2 + 1] + ")" + newstring2[charpos2 + 1:]
    finalstring = newstring2
    return finalstring


teststring = "QRIMITIR RONANN MAQ COMOGANN \n QENILOCI MAQI MAQI-AINIA MUC..."
print(deanogham(teststring))
print(deanogham(teststring, "scholastic"))
