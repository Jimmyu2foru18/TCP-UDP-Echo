#!/usr/bin/env python3

import socket
import argparse
import sys

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='TCP Echo Server')
    parser.add_argument('--host', default='127.0.0.1', help='Server hostname or IP address')
    parser.add_argument('--port', type=int, default=8888, help='Server port')
    return parser.parse_args()

def run_server(host, port):
    """Run the TCP echo server."""
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set socket option to reuse address
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        # Bind the socket to the address
        server_socket.bind((host, port))
        
        # Listen for incoming connections
        server_socket.listen(5)
        print(f"TCP Echo Server listening on {host}:{port}")
        
        while True:
            # Accept a connection
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")
            
            try:
                while True:
                    # Receive data from the client
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    
                    # Print received data
                    print(f"Received: {data.decode('utf-8')}")
                    
                    # Echo the data back to the client
                    client_socket.sendall(data)
            except Exception as e:
                print(f"Error handling client: {e}")
            finally:
                # Close the client socket
                client_socket.close()
                print(f"Connection from {client_address} closed")
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the server socket
        server_socket.close()
        print("Server socket closed")

def main():
    args = parse_arguments()
    run_server(args.host, args.port)

if __name__ == "__main__":
    main()