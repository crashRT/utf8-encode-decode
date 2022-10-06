from encode import encodeToUTF8

def decodeFromUTF8(utf8_string):
    '''
        E3 81 AB E3 82 83 E3 83 BC E3 82 93
        -> にゃーん
    '''
    utf8_string=utf8_string.lower()
    hex = utf8_string.strip(' ')
    hex = bytes.fromhex(hex)
    return hex.decode('utf-8')
    

source = 'うわああ'
print(decodeFromUTF8(encodeToUTF8(source)))
print(decodeFromUTF8('E3 81 AB E3 82 83 E3 83 BC E3 82 93'))