import socket

def send_number_to_server(number, from_base, to_base):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        message = f"{number},{from_base},{to_base}"
        server_address = ("127.0.0.1", 65432)
        client_socket.sendto(message.encode("utf-8"), server_address)
        result, _ = client_socket.recvfrom(1024)
        return result.decode("utf-8")
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        client_socket.close()
