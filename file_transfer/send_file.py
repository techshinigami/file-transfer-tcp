import socket
from os import path

HEADER = 64 # The number of bytes to represent the length of the message
PORT = 5050 # The port to connect to
FORMAT = "utf-8" # The format to encode/decode messages

def send_file(file_path: str, receiver_ip: str) -> None:
    # Create a socket object and connect to the server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((receiver_ip, PORT))
    
    # Check if the file exists
    if path.exists(file_path):
        # Get the file name and size
        file_name = path.basename(file_path)
        file_size = path.getsize(file_path)
        
        # Send the file name and size to the server
        client.send(f"{len(file_name):<{HEADER}}".encode(FORMAT) + file_name.encode(FORMAT))
        client.send(f"{file_size:<{HEADER}}".encode(FORMAT))
        
        # Open the file and send its contents
        with open(file_path, "rb") as f:
            while (bytes_read := f.read(1024)):
                client.send(bytes_read)
        print(f"[FILE SENT] {file_name} ({file_size} bytes)")
    else:
        print("[ERROR] File not found.")
    
    # Close the connection
    client.close()

if __name__ == "__main__":
    # Get the server IP address and file path from the user
    receiver_ip = input("Enter the server IP address: ").strip()
    file_path = input("Enter the file path to send: ").strip()
    send_file(file_path, receiver_ip)