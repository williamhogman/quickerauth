import os
import hmac
import time
import collections

PubToken = collections.namedtuple("PublicTokenPortion",["token_id","signature"])
PrivToken = collections.namedtuple("PrivateTokenPortion",["token_id","expires"])

def _create_token(secret):
    """ creates a new token given a secret """
    token_id = os.urandom(16) # 128bits should do
    expires = int(time.time()) + 60*5 # five minutes
    signature = hmac.new(secret,token_id).digest()

    return (PubToken(token_id,signature),PrivToken(token_id,expires))

def from_url_fragment(fragment):
    import base64
    pair = map(base64.urlsafe_b64decode,fragment.split("/"))
    return PubToken(*pair)

class QAManager(object):
    def __init__(self):
        raise RuntimeError("QAManager is abstract")

    def generate_token(self):
        pub,priv =  _create_token(self.secret)
        self._store_token(priv)
        return pub

    def verify_token(self,token):
        valid_sign = hmac.new(self.secret,token.token_id).digest()
        # we got an invalid signature
        if valid_sign != token.signature:
            return False
        
        priv = self._get_token(token.token_id)
        return priv is not None and time.time() < priv.expires

        
        
    
