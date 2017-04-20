specials = ". ? ! & # , ; : - _ *".strip(" ")

def firstone(password):
    lower = False
    upper = False
    num = False
    chars = [i for i in password]
    for element in chars:
        if ord(element) <= 57 and ord(element) >= 48:
            num = True
        if ord(element) <= 122 and ord(element) >= 97:
            lower = True
        if ord(element) <= 90 and ord(element) >= 65:
            upper = True
    return lower and upper and num

print firstone('11111')
print firstone('pen2')
print firstone('tigEr')
print firstone('Hello1')

def secondone(password):
    chars = [i for i in password]
    lowerlist = [char for char in chars if char.islower() ]
    upperlist = [char for char in chars if char.isupper() ]
    digitlist = [char for char in chars if char.isdigit() ]
    speclist = [char for char in chars if char in specials]
    
    
