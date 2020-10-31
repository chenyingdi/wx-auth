from Crypto.Cipher import AES

def handler(environ, start_response):
    AES.new(b'', AES.MODE_CBC)
    status = '200 OK'
    response_headers = [('Content-Type', 'application/json')]
    start_response(status, response_headers)
    return [b'hello']
