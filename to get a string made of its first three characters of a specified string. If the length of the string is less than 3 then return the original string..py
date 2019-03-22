'''
def character_strings(char):
    word=char[0:3]
    if  len(word)<3:
        print(char)
    else:
        character=word
        return character
print(character_strings('python'))
print(character_strings('on'))
'''
def first_three(str):
    return str[:3] if len(str)>3 else str
print(first_three('python'))
print(first_three('py'))