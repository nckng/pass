specials = ".?!&#,;:-_*"

def firstone( pw ):
    lowers = [ i for i in pw if i.islower() ]
    uppers = [ i for i in pw if i.isupper() ]
    nums = [ i for i in pw if i.isdigit() ]
    return len(lowers) > 0 and len(uppers) > 0 and len(nums) > 0

def secondone(password):
    lowerlist = [char for char in password if char.islower() ]
    upperlist = [char for char in password if char.isupper() ]
    digitlist = [char for char in password if char.isdigit() ]
    speclist = [char for char in password if char in specials ]

    #calculating weight
    weight = 1
    if( len(password) >= 8 ):
        weight += 1
    if( len( password) >= 16 ):
        weight += 1
    if( len( lowerlist) > 0 ):
        weight += 1
    if( len( upperlist) > 0):
        weight += 1
    if( len( digitlist) > 0):
        weight += 1
    if( len( speclist) > 0 ):
        weight += 2
    if( len( lowerlist) > 0 and len( upperlist) > 0):
        weight += 1
    if( len( digitlist) > 0 and ( len(lowerlist) > 0 or len(upperlist) > 0) ):
        weight += 1
    return weight
    
print "Testing First Task"
print firstone('11111')
print firstone('pen2')
print firstone('tigEr')
print firstone('Hello1')
print " ---------------- "
print "Testing Second Task"
print secondone('11111')
print secondone('pen2')
print secondone('tigEr')
print secondone(':')
print secondone('ThisIsHowYouGeta10:D')
