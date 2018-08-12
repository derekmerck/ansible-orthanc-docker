from cryptography.fernet import Fernet
import logging

def encrypt(s, key):
    f = Fernet(key.encode('UTF8'))
    ret = f.encrypt(s.encode('UTF8'))
    logging.info(ret)
    return ret


def decrypt(token, key):
    f = Fernet(key.encode('UTF8'))
    return f.decrypt(token.encode('UTF8'))


def gen_key():
    return Fernet.generate_key()


class FilterModule(object):
    '''
    custom jinja2 filters for fernet encryption
    '''

    def filters(self):
        return {
            'encrypt': encrypt,
            'decrypt': decrypt,
            'gen_key': gen_key
        }