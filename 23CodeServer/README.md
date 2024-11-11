# 23CodeServer 

## Introduction
`23CodeServer` is a simple local HTTP server that serves files and generates a QR code for easy access to the server on your network. It includes colorful console output and opens the server URL in your default web browser automatically. Built-in features include handling favicon requests and error handling for missing files.

## Preview

![preview](https://github.com/IHEfty/23CodeServer/blob/main/preview.png)

### Features:
- Serve files from the local directory.
- Show colorful output with local and network URLs.
- Generate a QR code to scan and open the server URL on the network.
- Auto-open the local URL in your browser upon server start.
- Handles 404 errors for missing files.

## Setup

### Requirements
- Python 3.x
- `colorama` for colored terminal output (`pip install colorama`)
- `qrcode` for generating QR codes (`pip install qrcode[pil]`)

### Running the Server
1. Clone or download the script to your local machine.
2. Install dependencies using:
   ```
   pip install colorama qrcode[pil]
   ```
3. Run the script:
   ```
   python 23codeserver.py
   ```

### Changing the Port
The default port is set to `8080`, but you can change it to any desired port by editing the `port` variable in the script:
```python
port = 8080  # Replace with your desired port number
```

### Output Example
After starting the server, you'll see a colorful output similar to the one below:

```
23CodeServer -Don't forget Server on port 7552:
Local: http://localhost:7552
Network: http://192.168.0.106:7552
█████████████████████████████████
█████████████████████████████████
████ ▄▄▄▄▄ █▀ ▄█  ▄ ▀█ ▄▄▄▄▄ ████
████ █   █ █ █ ▄ █ █▄█ █   █ ████
████ █▄▄▄█ ██▀ ▀▀▄ ███ █▄▄▄█ ████
████▄▄▄▄▄▄▄█ ▀ ▀ ▀▄█▄█▄▄▄▄▄▄▄████
████ ███▀█▄▀▄▄█▀██ ▄█  ▀▀   █████
████   ▄█▀▄ █▀▀▄▀█▀██ █▀▄ █▄ ████
████ ▄███▄▄▄█▄██▄▄▄█▀ █▄▄██▀▄████
████ █▄  █▄▄ ▀▄ ▄█▀█▄▀ █ ▄▀▄ ████
████▄███▄█▄▄ ▀▀▄▀▀█▄ ▄▄▄ ▄▄██████
████ ▄▄▄▄▄ ██▀ ▄▀▀█  █▄█ ▄ █ ████
████ █   █ ██▄ █▄█ █▄▄▄ ▄ ▄▄ ████
████ █▄▄▄█ ██▄▄ ▄█▀█ ▄   ▀ █ ████
████▄▄▄▄▄▄▄█▄▄███▄▄█▄█▄█▄▄██▄████
█████████████████████████████████
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Keyboard monitoring script is running. Press 'esc' to exit.
127.0.0.1 - - [24/Oct/2024 23:12:45] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [24/Oct/2024 23:12:45] "GET /favicon.ico HTTP/1.1" 200 -

```

The network URL will also display as a scannable QR code in ASCII format, making it easy to access the server on any device connected to the same network.

### Example Usage
The server is accessible both locally and on your network:
- Local URL: `http://localhost:7552`
- Network URL: `http://192.168.0.106:7552` (accessible from any device on the same local network)

### Keyboard Monitoring
The script includes basic keyboard monitoring to exit the server by pressing 'esc'. You can stop the server anytime by closing the terminal or pressing `Ctrl+C`.

### Customization
You can modify the server behavior or extend it by editing the `MyRequestHandler` class.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
