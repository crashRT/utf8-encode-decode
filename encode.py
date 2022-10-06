import re
import binascii

def encodeToUTF8(string):
    '''
        文字列をutf8のバイト列に変換し、
        そのまま文字列型にして返す
    ''' 
    hex = string.encode('UTF-8')
    string = repr(hex)
    string = formatUTF8(string)
    return string

def formatUTF8(string):
    string = string.upper() 
    string = re.sub(r'\\X', ' ', string)
    return string[3:-1] # b'' の中身だけ表示

source = 'hogehogeにゃー'
print(encodeToUTF8(source))