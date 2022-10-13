def encodeToUTF8(string):
    '''
        文字列をutf8のバイト列に変換し、
        そのまま文字列型にして返す
    ''' 
    hex = string.encode('UTF-8')
    return " ".join(list(map(lambda x: "%02X" % x, list(hex))))