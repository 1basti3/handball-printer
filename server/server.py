import socket
import threading

def handle_client(conn, addr):
    print(f"[+] Connection from {addr}")
    with open(f"/tmp/job_from_{addr[0]}.escpos", "wb") as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode('utf-8', errors='replace'))  # optionally show it
            f.write(data)
    conn.close()
    print(f"[-] Connection closed from {addr}")

def start_server(host="0.0.0.0", port=9100):
    print(f"[~] Starting fake ESC/POS printer on {host}:{port}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()
