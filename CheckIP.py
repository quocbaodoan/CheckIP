from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi, cgitb
from cgi import *
import subprocess
import requests


list_ip = []
list_url = []
class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            output = ''
            output += '<html><head>'
            output += '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
            output += '<title>Check IP</title>'
            output += '<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:400,600,800" >'
            output += '<link rel="stylesheet" href="vendors/css/grid.css">'
            output += '<link rel="stylesheet" href="resources/css/style.css">'
            output += '<link rel="stylesheet" href="resources/css/queries.css">'
            output += '<style>'
            output += '*{margin:0;padding:0;box-sizing:border-box}.clearfix::after{content:"";display:table;clear:both}html{font-family:Montserrat,"Helvetica Neue",Helvetica,Arial,sans-serif;font-size:30px;text-rendering:optimizeLegibility;height:100%}body{margin:0}.bg{animation:slide 6s ease-in-out infinite alternate;background-image:linear-gradient(-60deg,#6c3 50%,#09f 50%);bottom:0;left:-50%;opacity:.5;position:fixed;right:-50%;top:0;z-index:-1}.bg2{animation-direction:alternate-reverse;animation-duration:8s}.bg3{animation-duration:10s}.content{border-radius:20px;box-shadow:0 0 .25em rgba(0,0,0,.25);box-sizing:border-box;left:50%;padding:3vmin 9vmin;position:fixed;text-align:center;top:50%;transform:translate(-50%,-50%)}@keyframes slide{0%{transform:translateX(-25%)}100%{transform:translateX(25%)}}h2{margin-bottom:40px;font-weight:900;font-size:160%;color:#e4f9f5}input[type=text]{border-style:none;background-color:#e4f9f5;border-radius:10px;width:260px;padding:9px 10px;margin-bottom:40px;font-size:20px;font-family:Montserrat,"Helvetica Neue",Helvetica,Arial,sans-serif}input[type=submit]{background-color:#e4f9f5;color:#71c9ce;padding:11px 22px;border-style:solid;border-radius:20px;border-style:none;font-size:18px;font-weight:700;font-family:Montserrat,"Helvetica Neue",Helvetica,Arial,sans-serif}'
            output += '</style></head>'
            output += '<body>'
            output += '<div class="bg"></div>'
            output += '<div class="bg bg2"></div>'
            output += '<div class="bg bg3"></div>'
            output += '<div class="content">'
            output += '<form action="/view" method="POST" enctype="multipart/form-data">'
            output += '<div class="row"><h2>Check IP</h2></div>'
            output += '<div class="row"><input type="text" name="url"></div>'
            output += '<div class="row"><input type="submit" value="Enter"></div>'
            output += '</form>'
            output += '</div>'
            output += '</body>'
            output += '</html>'

            self.wfile.write(output.encode())

        if self.path.endswith('/view'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            output = ''
            output += '<html><head>'
            output += '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
            output += '<title>View IP</title>'
            output += '<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:400,600,800" >'
            output += '<link rel="stylesheet" href="vendors/css/grid.css">'
            output += '<link rel="stylesheet" href="resources/css/style.css">'
            output += '<link rel="stylesheet" href="resources/css/queries.css">'
            output += '<style>'
            output += '*{margin:0;padding:0;box-sizing:border-box}.clearfix::after{content:"";display:table;clear:both}html{font-family:Montserrat,"Helvetica Neue",Helvetica,Arial,sans-serif;font-size:30px;text-rendering:optimizeLegibility;height:100%;color:#e4f9f5}body{margin:0}.bg{animation:slide 6s ease-in-out infinite alternate;background-image:linear-gradient(-60deg,#6c3 50%,#09f 50%);bottom:0;left:-50%;opacity:.5;position:fixed;right:-50%;top:0;z-index:-1}.bg2{animation-direction:alternate-reverse;animation-duration:8s}.bg3{animation-duration:10s}.content{border-radius:20px;box-shadow:0 0 .25em rgba(0,0,0,.25);box-sizing:border-box;left:50%;padding:7vmin 8vmin;position:fixed;text-align:center;top:50%;transform:translate(-50%,-50%)}@keyframes slide{0%{transform:translateX(-25%)}100%{transform:translateX(25%)}}h3{margin-bottom:40px}input[type=text]{border-style:none;border-radius:10px;width:260px;padding:9px 10px;margin-bottom:40px;font-size:20px;font-family:Montserrat,"Helvetica Neue",Helvetica,Arial,sans-serif}input[type=submit]{background-color:#000;color:#fff;padding:11px 22px;border-style:solid;border-radius:20px;border-style:none;font-size:18px;font-weight:700;font-family:Montserrat,"Helvetica Neue",Helvetica,Arial,sans-serif}'
            output += '</style></head>'
            output += '<body>'
            output += '<div class="bg"></div>'
            output += '<div class="bg bg2"></div>'
            output += '<div class="bg bg3"></div>'
            output += '<div class="content">'
            output += '<div class="row"><h3>'
            output += 'IP ' + list_url[len(list_url)-1]
            output += '</h3></div>'
            output += list_ip[len(list_ip)-1]
            output += '</div>'
            output += '</body>'
            output += '</html>'

            self.wfile.write(output.encode())


    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
        pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
        content_len = int(self.headers.get('Content-length'))
        pdict['CONTENT-LENGTH'] = content_len
        if ctype =='multipart/form-data':
            fields = cgi.parse_multipart(self.rfile, pdict)
            url = fields.get('url')
            response = requests.get("http://ip-api.com/json/" + url[0])
            ip = response.json()["query"]
            list_url.append(url[0])
            list_ip.append(ip)
            #cmd_result = subprocess.check_output('ping ' +url[0])
            #cmd_result = cmd_result.decode("utf-8")
            #ip = cmd_result[cmd_result.find("[")+1 : cmd_result.find("]")]
            #list_url.append(url[0])
            #list_ip.append(ip)

        self.send_response(301)
        self.send_header('content-type', 'text/html')
        self.send_header('Location', '/view')
        self.end_headers()


def main():
    PORT = 8080
    server_address = ('localhost', PORT)
    server = HTTPServer(server_address, requestHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()