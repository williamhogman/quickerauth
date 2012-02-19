import quickerauth as qa

class HashQAManager(qa.QAManager):
    """ Simple quickauth implementation using a dict for example purposes """
    def __init__(self,secret="foobar"):
        self.secret = secret
        self._token_store = dict()
        self._get_token = self._token_store.get

    def _store_token(self,token):
        # hacky, but this is just for the demo
        self._token_store[token.token_id] = token
