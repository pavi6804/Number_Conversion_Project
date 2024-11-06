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
        
        # Conversion to target base
        if to_base == "binary":
            return bin(number)[2:]  # Convert to binary
        elif to_base == "octal":
            return oct(number)[2:]  # Convert to octal
        elif to_base == "decimal":
            return str(number)  # Convert to decimal
        elif to_base == "hexadecimal":
            return hex(number)[2:].upper()  # Convert to hexadecimal
        else:
            return "Invalid target base"
    except ValueError:
        return "Invalid number input"

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("127.0.0.1", 65432))
    print("UDP Server is listening on port 65432...")

    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Received data from {addr}")

        number, from_base, to_base = data.decode("utf-8").split(",")  # Receive number and conversion details
        result = convert_number(number, from_base, to_base)

        server_socket.sendto(result.encode("utf-8"), addr)

if __name__ == "__main__":
    start_server()
