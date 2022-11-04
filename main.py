"""
import http.server
import socketserver
PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

def main():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.allow_reuse_address = True
        print("serving at port", PORT)
        httpd.serve_forever()


if __name__ == "__main__":
    main()
    
"""

from flask import Flask

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def galaxy():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
