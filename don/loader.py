from don.server.Server import server

http_server = server

if __name__ == '__main__':
    http_server()
else:
    http_server = server
