# TCP UDP Echo

A simple implementation of an echo server and client using both TCP and UDP protocols. 
The client sends messages to the server, which echoes them back. 
The client also measures the round-trip latency, similar to the real `ping` utility.

## Project Structure

```
.
├── README.md          
├── tcp/                # TCP 
│   ├── server.py       # TCP server 
│   └── client.py       # TCP client
└── udp/                # UDP 
    ├── server.py       # UDP server
    └── client.py       # UDP client 
```

## Features

- Echo server implementation using both TCP and UDP protocols
- Client implementation for both protocols
- Latency measurement (round-trip time)
- Simple command-line interface
- Configurable server address and port

## Requirements

- Python 3.6 or higher

## Usage

### TCP Implementation

1. Start the TCP server:

```bash
python tcp/server.py [--host HOST] [--port PORT]
```

2. Run the TCP client:

```bash
python tcp/client.py [--host HOST] [--port PORT] [--count COUNT] [--interval INTERVAL]
```

### UDP Implementation

1. Start the UDP server:

```bash
python udp/server.py [--host HOST] [--port PORT]
```

2. Run the UDP client:

```bash
python udp/client.py [--host HOST] [--port PORT] [--count COUNT] [--interval INTERVAL]
```

### Command-line Arguments

- `--host`: Server hostname or IP address (default: 127.0.0.1)
- `--port`: Server port (default: 8888)
- `--count`: Number of ping messages to send (default: 4)
- `--interval`: Interval between ping messages in seconds (default: 1)

## Details

### TCP 

The TCP uses Python's `socket` module with SOCK_STREAM socket type. 
The server accepts connections from clients and echoes back any received messages. 
The client measures the round-trip time for each message.

### UDP 

The UDP uses Python's `socket` module with SOCK_DGRAM socket type. 
The server listens for datagrams and echoes them back to the sender. 
The client sends datagrams and measures the round-trip time.
