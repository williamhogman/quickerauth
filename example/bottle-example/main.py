import StringIO
import socket
import sys
sys.path.append("./")


from bottle import route, run, response, request
from quickerauth import QuickerCode,from_url_fragment
from qa_impl import HashQAManager



qa = HashQAManager()

@route('/')
def index():
    return "<img src='/qrcode' />"

@route("/qrcode")
def qrcode():

    response.content_type = "image/png"
    code = QuickerCode(qa.generate_token(),"http",socket.gethostname()+":8080/qauth")
    bfr = StringIO.StringIO()
    code.get_image().save(bfr,kind="png")
    return bfr.getvalue()

@route("/qauth/<cred:path>")
def qauth(cred):
    token = from_url_fragment(cred)
    if qa.verify_token(token):
        return "Authentication successful "+token.token_id.encode("hex")
    else:
        return "Authentication failed!"

    return cred

run(host='0.0.0.0', port=8080)
