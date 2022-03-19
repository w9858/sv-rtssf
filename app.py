from sanic import Sanic, Blueprint
from sanic.response import raw, html, empty
import os, base64, ssl, time, datetime
from api import api

os.chdir(os.path.dirname(os.path.abspath(__file__)))

app = Sanic("Spyce")
app.blueprint(api)

@app.on_response
async def add_header(request, response):
    unixtime = int(datetime.datetime.now().timestamp())
    #response.headers['Server'] = ''
    if ((request.host == "api.relefra.jp") & (request.method == 'POST')):
        response.headers['Content-Type'] = 'application/x-google-protobuf'
        response.headers['X_SQLITE_VER'] = 81
        response.headers['X_RES_STATUS'] = 0
        response.headers['X_TIMESTAMP'] = unixtime
        # Edit time if you want see old events. UNIX timestamp will needed.

app.static('/assets', './img/assets', name="img-assets")
app.static('/sqlites', './img/sqlites', name="img-sqlites")
app.static('/images', './img/images', name="img-images")
app.static('/cert', './cert', name="certification")

@app.get("/")
async def root(request):
    return html('<a href="./cert/cert.crt">download cert.crt</a>\
             <br><a href="./cert/cert.pfx">download cert.pfx</a>')

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile='./cert/cert.crt', keyfile='./cert/cert.key')
# app.run(host="0.0.0.0", port=443, ssl=ssl_context, debug=True)
app.run(host="0.0.0.0", port=443, ssl=ssl_context, auto_reload=True)