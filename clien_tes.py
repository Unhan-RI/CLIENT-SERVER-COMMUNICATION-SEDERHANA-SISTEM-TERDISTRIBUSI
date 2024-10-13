import socket
import threading
import time

# Konfigurasi host dan port server coordinator
coordinator_host = '127.0.0.1'
coordinator_port = 8000
NUM_CLIENTS = 5  # Jumlah klien yang diuji

# Variabel untuk mencatat waktu mulai dan selesai setiap klien
start_times = []
end_times = []

# Fungsi untuk menghitung metrik pengujian
def calculate_metrics(start_times, end_times):
    total_time = sum([end - start for start, end in zip(start_times, end_times)])
    
    if total_time == 0:
        print("Total time is zero, skipping calculations.")
        return

    avg_response_time = total_time / NUM_CLIENTS
    throughput = NUM_CLIENTS / total_time  # Requests per second
    latency = avg_response_time  # Latensi kira-kira sama dengan rata-rata waktu respons

    print("\n==== Test Results ====")
    print(f"Average Response Time: {avg_response_time:.5f} seconds")
    print(f"Throughput: {throughput:.5f} requests per second")
    print(f"Latency: {latency:.5f} seconds\n")

# Fungsi untuk setiap klien yang mengirim permintaan ke server
def client_task(client_id):
    start_time = time.time()  # Waktu mulai
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((coordinator_host, coordinator_port))

        # Kirim pesan ke server
        message = f"Test message from client {client_id}"
        client_socket.send(message.encode('utf-8'))

        # Terima balasan dari server
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Client {client_id} received: {response}")

    except Exception as e:
        print(f"Client {client_id}: Error occurred - {e}")

    finally:
        client_socket.close()
        end_time = time.time()  # Waktu selesai
        start_times.append(start_time)
        end_times.append(end_time)

# Fungsi utama untuk menjalankan 100 klien secara paralel
def run_test_100_clients():
    threads = []

    # Membuat dan memulai thread untuk setiap klien
    for i in range(1, NUM_CLIENTS + 1):
        t = threading.Thread(target=client_task, args=(i,))
        threads.append(t)

    print(f"Starting test with {NUM_CLIENTS} clients...\n")

    # Memulai semua thread klien
    for t in threads:
        t.start()

    # Menunggu semua klien selesai
    for t in threads:
        t.join()

    # Hitung dan tampilkan metrik setelah semua klien selesai
    calculate_metrics(start_times, end_times)

if __name__ == "__main__":
    run_test_100_clients()
