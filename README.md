# File Transfer TCP Module

This module allows you to send and receive files between two machines over a TCP connection.

## Requirements
- Python 3.x

## Installation

You can install the module by cloning the repository:

```bash
git clone https://github.com/techshinigami/file-transfer-tcp.git
cd file-transfer-tcp
```

## Usage

### Sending a File

To send a file, use the `send_file` function from the `file_transfer` module. You need to provide the file path and the receiver's IP address.

```python
from file_transfer import send_file

file_path = "path/to/your/file.txt"
receiver_ip = "192.168.1.2"
send_file(file_path, receiver_ip)
```

### Receiving a File

To receive a file, use the `receive_file` function from the `file_transfer` module. This will start a server that listens for incoming file transfers.

```python
from file_transfer import receive_file

receive_file()
```

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
