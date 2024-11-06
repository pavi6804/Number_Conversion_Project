import socket

def convert_number(number, from_base, to_base):
    try:
        if from_base == "decimal":
            number = int(number)
        elif from_base == "binary":
            number = int(number, 2)
        elif from_base == "octal":
            number = int(number, 8)
        elif from_base == "hexadecimal":
            number = int(number, 16)
        else:
            return "Invalid base"
        
        if to_base == "binary":
            return bin(number)[2:]  
        elif to_base == "octal":
            return oct(number)[2:]  
        elif to_base == "decimal":
            return str(number)  
        elif to_base == "hexadecimal":
            return hex(number)[2:].upper() 
        else:
            return "Invalid target base"
    except ValueError:
        return "Invalid number input"

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 65432))
    server_socket.listen(1)
    print("Server is listening on port 65432...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        data = client_socket.recv(1024).decode("utf-8")
        number, from_base, to_base = data.split(",")  

        result = convert_number(number, from_base, to_base)

        client_socket.send(result.encode("utf-8"))
        client_socket.close()

if __name__ == "__main__":
    start_server()
