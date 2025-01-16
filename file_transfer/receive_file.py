import socket

HEADER = 64 # The number of bytes to represent the length of the message
PORT = 5050 # The port to connect to
FORMAT = "utf-8" # The format to encode/decode messages

def receive_file() -> None:
    # Create a socket object and bind it to the server's IP address and port
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((socket.gethostbyname(socket.gethostname()), PORT))

    # Listen for incoming connections
    server.listen()
    print(f"[LISTENING] Receiver is listening on {socket.gethostbyname(socket.gethostname())}")
    conn, addr = server.accept()
    print(f"[NEW CONNECTION] {addr} connected.")
    
    try:
        # Receive the length of the file name
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            # Receive the file name
            file_name = conn.recv(msg_length).decode(FORMAT).strip()
            # Receive the file size
            file_size = int(conn.recv(HEADER).decode(FORMAT))
            print(f"[FILE TRANSFER] Receiving file: {file_name} ({file_size} bytes)")
            
            # Open a file to write the received data
            with open(file_name, "wb") as f:
                bytes_received = 0
                while bytes_received < file_size:
                    # Receive the file data in chunks
                    bytes_read = conn.recv(min(file_size - bytes_received, 1024))
                    if not bytes_read:
                        break
                    f.write(bytes_read)
                    bytes_received += len(bytes_read)
            print(f"[FILE RECEIVED] {file_name} ({file_size} bytes)")
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")
    finally:
        # Close the connection and the server
        conn.close()
        server.close()

if __name__ == "__main__":
    receive_file()