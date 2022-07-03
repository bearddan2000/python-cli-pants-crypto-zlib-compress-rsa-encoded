import zlib
import sys
class PasswordCompress:

    def compress(self, password):
        # password = bytes(password, encoding='utf-8')
        print("[COMPRESS] decompress size: ", sys.getsizeof(password))
        return zlib.compress(password)

    def decompress(self, password):
        #password = bytes(password, encoding='utf-8')
        print("[COMPRESS] compress size: ", sys.getsizeof(password))
        return zlib.decompress(password)
