import hashlib

class Encryption(object):
    """Encryption data(password or customer data)"""
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def md5_encrytion(arg):
        return hashlib.md5(arg.encode('utf-8')).hexdigest()


