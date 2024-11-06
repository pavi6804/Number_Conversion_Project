import socket

def send_number_to_server(number, from_base, to_base):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 65432))

    message = f"{number},{from_base},{to_base}"
    client_socket.send(message.encode("utf-8"))

    result = client_socket.recv(1024).decode("utf-8")
    client_socket.close()
    return result
