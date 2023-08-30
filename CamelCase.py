def camelcase(s):
    if s == "":
        return ""
    else:
        lista = s.split()
        converted = "".join(word[0].upper() + word[1:].lower() for word in lista)
        return converted[0] + converted[1:]

print(camelcase("hola mundo"))