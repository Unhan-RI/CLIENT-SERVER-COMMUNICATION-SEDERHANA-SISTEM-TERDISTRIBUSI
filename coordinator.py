import socket
import threading

# Daftar server backend yang terdistribusi
servers = [
    ('127.0.0.1', 9001),
    # ('127.0.0.1', 9002),
    # ('127.0.0.1', 9003)
]

# Variabel untuk round-robin balancing
current_server = 0
lock = threading.Lock()

# Fungsi untuk memilih server backend secara round-robin
def get_next_server():
    global current_server
    with lock:  # Menggunakan lock untuk memastikan thread-safe
        server = servers[current_server]
        current_server = (current_server + 1) % len(servers)
    return server

# Fungsi untuk meneruskan permintaan ke salah satu server backend
def forward_request(client_socket):
    server_host, server_port = get_next_server()
    
    try:
        # Koneksi ke server backend
        backend_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        backend_socket.connect((server_host, server_port))

        # Terima data dari klien
        client_data = client_socket.recv(1024)
        
        # Kirim data ke server backend
        backend_socket.send(client_data)
        
        # Terima balasan dari server backend
        backend_response = backend_socket.recv(1024)
        
        # Kirim balasan ke klien
        client_socket.send(backend_response)
        
        backend_socket.close()
    except Exception as e:
        print(f"Failed to forward request to {server_host}:{server_port}: {e}")
        client_socket.send(f"Error contacting server {server_host}:{server_port}".encode())

# Fungsi server coordinator
def coordinator_server():
    coordinator_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    coordinator_socket.bind(('0.0.0.0', 8000))
    coordinator_socket.listen(5)
    print("Coordinator is running on port 8000")

    while True:
        client_socket, addr = coordinator_socket.accept()
        print(f"Received connection from {addr}")
        
        # Gunakan threading untuk menangani klien secara paralel
        client_thread = threading.Thread(target=forward_request, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    coordinator_server()
