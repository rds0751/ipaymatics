from hashlib import sha512
from django.conf import settings
KEYS = ('key', 'txnid', 'amount', 'productinfo', 'firstname', 'email',
        'udf1', 'udf2', 'udf3', 'udf4', 'udf5',  'udf6',  'udf7', 'udf8',
        'udf9',  'udf10')

def generate_hash(data):
    keys = ('key', 'txnid', 'amount', 'productinfo', 'firstname', 'email',
            'udf1', 'udf2', 'udf3', 'udf4', 'udf5',  'udf6',  'udf7', 'udf8',
            'udf9',  'udf10')
    sash=''
    for key in keys:
        sash+="%s%s" % (str(data.get(key, '')), '|')
    sash+=settings.PAYU_INFO.get('merchant_salt')
    hash = sha512(sash.encode('utf-8'))
    return hash.hexdigest().lower()

def verify_hash(data, SALT):    
    keys.reverse()
    hash = sha512(settings.PAYU_INFO.get('merchant_salt'))
    hash.update("%s%s" % ('|', str(data.get('status', ''))))
    for key in keys:
        sash+="%s%s" % (str(data.get(key, '')), '|')
        hash = sha512(sash.encode('utf-8'))
    return (hash.hexdigest().lower() == data.get('hash'))