# string = "hello world"

# def get_consonants(string):
#     return string.replace("a", 1).replace("b", 2).replace("c", 3).replace("d", 4).replace("e", 5).replace("f", 6).replace("g", 7).replace("h", 8).replace("i", 9).replace("j", 10).replace("k", 11).replace("l", 12).replace("m", 13).replace("n", 14).replace("o", 15).replace("p", 16).replace("q", 17).replace("r", 18).replace("s", 19).replace("t", 20).replace("u", 21).replace("v", 22).replace("w", 23).replace("x", 24).replace("y", 25).replace("z", 26)

# consonants = get_consonants(string)


# print(get_consonants(string))



def consonants(string):
    consonants = []
    for char in string:
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            consonants.append(char)
    return consonants

string1 = 'hello'
string2 = 'hi'
string3 = 'how are you'

print(consonants(string1))
print(consonants(string2))
print(consonants(string3))