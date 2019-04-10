import socketserver
import threading
import videoPlayer

position = []

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("|   X   |   Y   |   Z   |   X0   |   Y0   |   Z   |")
        videoPlayer.playVideo()
        while True:
            self.data = self.request.recv(1024)
            if not self.data:
                break
            self.data = self.data.strip()
            #Print incoming data points
            print(self.data.decode('utf_8'))
            self.request.send(self.data.upper())

            #Fill position array with incoming data
            position.append(self.data)

if __name__ == "__main__":
    HOST, PORT = "localhost", 3288
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()


