def duplicate_encode(word):
    letra = 0
    palabr= ""
    wrd = word.lower()
    for x in wrd:
        letra = wrd.count(x)
        if letra > 1:
            palabr += ")"
        else:
            palabr += "("
    return palabr

#transformar las palabras a "()" por ejemplo: din = (((, success = )())())