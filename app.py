from sanic import Sanic, Blueprint
from sanic.response import raw, html, empty
import os, base64, ssl, time
from api import api

app = Sanic("Spyce")
app.blueprint(api)

@app.on_response
async def add_header(request, response):
    try:
        with open("./server_settings/time.txt", "r") as timef:
            settime = timef.readline()
            if(settime == "now"): now = int(time.time())
            elif(settime.isnumeric()):
                if(int(settime) > 2147483647):
                    raise ValueError("Timestamp value is too large. Check ./server_settings/time.txt")
                else: now = int(settime)
            else: raise ValueError("Invaild timestamp value. Check ./server_settings/time.txt")
    except(FileNotFoundError):
        os.makedirs("./server_settings/", exist_ok=True)
        with open("./server_settings/time.txt", "w") as timef:
            timef.write("now")
        now = int(time.time())
    #response.headers['Server'] = ''
    if ((request.host == "api.relefra.jp") & (request.method == 'POST')):
        response.headers['Content-Type'] = 'application/x-google-protobuf'
        response.headers['X_SQLITE_VER'] = 81
        try: response.headers['X_RES_STATUS'] = request.ctx.errorcode
        except(AttributeError): response.headers['X_RES_STATUS'] = 0
        response.headers['X_TIMESTAMP'] = now
        # Edit ./server_settings/time.txt if you want see old events, or campaigns.
        # Unix Timestamp will needed.
        # ex. yyyi collabo timestamp is 1560146340

app.static('/assets', './img/assets', name="img-assets")
app.static('/sqlites', './img/sqlites', name="img-sqlites")
app.static('/images', './img/images', name="img-images")
app.static('/cert', './cert', name="certification")

@app.get("/")
async def root(request):
    return html('<h1>Download Self-signed Certification</h1>\
    <br><a href="./cert/cert.crt">Download cert.crt (Recommended on average devices.)</a>\
    <br><a href="./cert/cert.pfx">Download cert.pfx (Try it if crt file doesn\'t work.)</a>')


if __name__ == "__main__":
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    try:
        ssl_context.load_cert_chain(certfile='./cert/cert.crt', keyfile='./cert/cert.key')
    except:
        input("Unable to load certificate file! Two files are required. (./cert/cert.crt and ./cert/cert.key)")
        exit()
    # app.run(host="0.0.0.0", port=443, ssl=ssl_context, debug=True)
    app.run(host="0.0.0.0", port=443, ssl=ssl_context, auto_reload=True)