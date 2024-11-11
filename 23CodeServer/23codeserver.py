import http.server
import socketserver
import qrcode
import webbrowser
import socket
import colorama

colorama.init()

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/favicon.ico':
            self.send_response(200)
            self.send_header('Content-type', 'image/x-icon')
            self.end_headers()
            return

        try:
            return super().do_GET()
        except FileNotFoundError:
            self.send_error(404, "File not found")

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.254.254.254', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

local_ip = get_local_ip()

def start_server(port):
    Handler = MyRequestHandler

    with socketserver.TCPServer(("", port), Handler) as httpd:
        local_url = f"http://localhost:{port}"
        network_url = f"http://{local_ip}:{port}"

        network_qr = qrcode.QRCode()
        network_qr.add_data(network_url)
        network_qr.make(fit=True)

        print(f"Sponsored by Straw - Feel the Test")
        print(colorama.Fore.RED + f"23CodeServer - Don't forget Server on port {port}:" + colorama.Style.RESET_ALL)
        print("Local:", colorama.Fore.BLUE + local_url + colorama.Style.RESET_ALL)
        print("Network:", colorama.Fore.BLUE + network_url + colorama.Style.RESET_ALL)
        network_qr.print_ascii(invert=True)

        webbrowser.open(local_url, new=2)

        httpd.serve_forever()

if __name__ == "__main__":
    port = 8080  
    start_server(port)
