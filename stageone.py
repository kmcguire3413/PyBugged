'''
    The result should be 6.
'''
def level_notgoodtypes():
    x = 3
    return x + "3"

'''
    We need to create either a string or bytes object.
'''
def level_tryconcating():
    return b'e' + 'f'

'''
    Why does X never equal 100?
'''
def level_mayberangefellshort():
    for x in range(0, 100):
        pass
    if x == 100:
        return True
    return False

'''
    Why is this never true? And, can you fix it?
'''
def level_floatingnumbersnotright():
    v = 0.1 + .02
    return v == .12

'''
    We should return the first letter of the string,
    but do we? The first letter is `h`. Why is it
    not returning `h`.
'''
def level_indexingstringkindaconfusing():
    s = 'hello world'
    return s[1]

'''
    We are trying to set the 8th bit of the
    integer to one.

    This function should return 128 or 0x80.
'''
def level_shiftingisweird():
    return 1 << 8

'''
    This function should return one by doing
    a shifting operation. We need to shift
    the 8th bit to the 1st bit.
'''
def level_shiftingisweirder():
    return 0x80 >> 8

'''
    Can you spot the problem? We should return a
    the value 0x88 after the operation. You can
    easily just modify it to return 0x88, but 
    that would be cheating.
'''
def level_andingforabit():
    return 0x88 & (0x11 << 7)

'''
    Can you make them equal? In both ways...

    Hint.. ord(x) or chr(x)
    Hint.. bytes or decode
'''
def level_bytesbutstrsame():
    # an example
    a = b'hello world'
    b = b.decode('utf8')                # treats bytes as if they are in the UTF8 encoding
    c = chr(65)
    d = ord('A')
    e = bytes('hello world', 'utf8')    # converts unicode string into UTF8 encoding
    print(a, b, c, d)

    # the problem
    b = b'hello world'
    s = 'hello world'
    return b[0] == s[0] and b == s

'''
    Why do these not equal each other? Can it
    be fixed? How do we fix the problem and why
    did we have to fix it?
'''
def level_whydifferentencoding():
    z = 'hello world'
    a = bytes(z, 'utf8')
    b = bytes(z, 'utf16')

    r1 = a[0] + 146 == b
    r2 = a[0] == b[0]

    return r1 and r2 

'''
    We need to combine the strings to produce
    the string `ab` why does it not work?
'''
def level_andsomestrings():
    return 'a' and 'b'

