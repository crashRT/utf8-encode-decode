from encode import *
from decode import *



source = 'hogehogeにゃーん'

# encode
print(encodeToUTF8(source))
    
# decode
print(decodeFromUTF8(encodeToUTF8(source)))
print(decodeFromUTF8('E3 81 AB E3 82 83 E3 83 BC E3 82 93'))