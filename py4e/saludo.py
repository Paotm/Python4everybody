def great(lang):
    if lang == "es":
        return "hola"
    elif lang == "en" :
        return "Hello"
    else :
        return "Bonjour"
name= input("Name: ")
lang = input("Choose one: en, es fr :")
print(great(lang), name)
