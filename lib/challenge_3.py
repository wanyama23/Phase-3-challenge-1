# import re
# solve = lambda s : max([sum([ord(letter)-ord('a')+1 for letter in consOnly]) for consOnly in re.split("a|e|i|o|u",s)])

# print(solve("zodiacs")) # output : 26
# print(solve("chruschtschov")) # output : 80
# print(solve("rhythm")) # output : 92





# string = "hello world"

# def get_consonants(string):
#     return string.replace("a", 1).replace("b", 2).replace("c", 3).replace("d", 4).replace("e", 5).replace("f", 6).replace("g", 7).replace("h", 8).replace("i", 9).replace("j", 10).replace("k", 11).replace("l", 12).replace("m", 13).replace("n", 14).replace("o", 15).replace("p", 16).replace("q", 17).replace("r", 18).replace("s", 19).replace("t", 20).replace("u", 21).replace("v", 22).replace("w", 23).replace("x", 24).replace("y", 25).replace("z", 26)

# consonants = get_consonants(string)


# print(get_consonants(string))



def consonants(string):
    consonants = []

    alph=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for char in string:
        if char.lower() not in ['a', 'e', 'i', 'o', 'u',' '," "]:
            # consonants.append(char)

            char2=alph.index(char)+1

            consonants.append(char2)

    return consonants

string1 = 'hello'
string2 = 'hi'
string3 = 'how are you'

print (consonants(string1))
print(consonants(string2))
print(consonants(string3))

