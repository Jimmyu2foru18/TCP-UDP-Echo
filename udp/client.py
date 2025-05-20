#!/usr/bin/env python3

import socket
import argparse
import time
import statistics
import sys

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='UDP Echo Client')
    parser.add_argument('--host', default='127.0.0.1', help='Server hostname or IP address')
    parser.add_argument('--port', type=int, default=8888, help='Server port')
    parser.add_argument('--count', type=int, default=4, help='Number of ping messages to send')
    parser.add_argument('--interval', type=float, default=1.0, help='Interval between ping messages in seconds')
    parser.add_argument('--timeout', type=float, default=1.0, help='Timeout for receiving response in seconds')
    return parser.parse_args()

def run_client(host, port, count, interval, timeout):
    """Run the UDP echo client with latency measurement."""
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Set socket timeout
    client_socket.settimeout(timeout)
    
    try:
        print(f"UDP Ping to {host}:{port}")
        
        # Statistics variables
        rtts = []
        sent = 0
        received = 0
        
        for i in range(count):
            # Create message
            message = f"PING {i} {time.time()}"
            
            try:
                # Record start time
                start_time = time.time()
                
                # Send the message
                client_socket.sendto(message.encode('utf-8'), (host, port))
                sent += 1
                
                # Receive the echo
                try:
                    data, server = client_socket.recvfrom(1024)
                    
                    # Record end time and calculate RTT
                    end_time = time.time()
                    rtt = (end_time - start_time) * 1000  # Convert to milliseconds
                    rtts.append(rtt)
                    received += 1
                    
                    # Print the result
                    print(f"Reply from {host}: seq={i} time={rtt:.2f} ms")
                except socket.timeout:
                    print(f"Request timeout for seq={i}")
            except Exception as e:
                print(f"Error sending/receiving: {e}")
            
            # Wait for the specified interval before sending the next message
            if i < count - 1:
                time.sleep(interval)
        
        # Print statistics
        print("\n--- Ping statistics ---")
        print(f"Sent = {sent}, Received = {received}, Lost = {sent - received} ({(sent - received) / sent * 100 if sent > 0 else 0:.1f}% loss)")
        
        if rtts:
            print("\n--- RTT statistics ---")
            print(f"Min = {min(rtts):.2f} ms, Max = {max(rtts):.2f} ms, Avg = {statistics.mean(rtts):.2f} ms")
            if len(rtts) > 1:
                print(f"StdDev = {statistics.stdev(rtts):.2f} ms")
    
    except KeyboardInterrupt:
        print("\nClient shutting down...")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the client socket
        client_socket.close()
        print("Client socket closed")

def main():
    args = parse_arguments()
    run_client(args.host, args.port, args.count, args.interval, args.timeout)

if __name__ == "__main__":
    main()