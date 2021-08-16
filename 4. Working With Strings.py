print("Giraffe Academy")
print("Giraffe\nAcademy")
print("Giraffe\"Academy")

phrase = "giraffe academy"
print(phrase)

#concatination
phrase = "giraffe academy"
print(phrase + " is cool.")

#function
phrase = "giraffe academy"
print(phrase.upper())
print(phrase.lower())
print(phrase.isupper())
print(phrase.upper().isupper())

#length
phrase = "giraffe academy"
print(len(phrase))
print(phrase[11])
print(phrase[0].upper())

phrase = "giraffe academy"
#         01234567891011121314
print(phrase[0])
print(phrase.index("g"))
print(phrase.index("acad"))
print(phrase.replace("giraffe", "elephant"))