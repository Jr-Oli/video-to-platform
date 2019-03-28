import socketserver
import threading


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while 1:
            self.data = self.request.recv(1024)
            if not self.data:
                break
            self.data = self.data.strip()
            print (str(self.client_address[0]) + " wrote: ")
            print (self.data)
            self.request.send(self.data.upper())


if __name__ == "__main__":
    HOST, PORT = "localhost", 3288
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()