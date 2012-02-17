import qrcode
import base64

class QuickerCode(object):
    """ Class representing a QuickerAuth QRCode """
    def __init__(self,token,protocol="qrauth",hostname="invalid"):
        self._protocol = protocol
        self._hostname = hostname
        self._token = token
        self._img = None

    def _generate_url(self):

        token_id = base64.urlsafe_b64encode(self._token.token_id)
        signature = base64.urlsafe_b64encode(self._token.signature)

        return "{}://{}/{}/{}".format(
            self._protocol,
            self._hostname,
            token_id,
            signature
            )
        
        
    def _create_image(self):
        code = qrcode.QRCode(
            #error_correction=qrcode.constants.ERROR_CORRECT_H
            )
        code.add_data(self._generate_url())

        code.make(fit=True)

        self._img = code.make_image()

    def get_image(self):
        if self._img is None:
            self._create_image()
        return self._img
