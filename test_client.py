import socket
import threading
import time

# Konfigurasi host dan port server coordinator
coordinator_host = '127.0.0.1'
coordinator_port = 8000

# Daftar skenario jumlah klien yang akan diuji
client_scenarios = [5, 10, 20]  # Jumlah klien bervariasi

# Variabel untuk menyimpan hasil pengujian
results = []

# Fungsi untuk mengukur waktu rata-rata, latensi, dan throughput
def calculate_metrics(start_times, end_times, num_clients):
    if not start_times or not end_times:
        print(f"Warning: No data collected for {num_clients} clients.")
        return 0, 0, 0

    total_time = sum([end - start for start, end in zip(start_times, end_times)])
    
    # Menghindari pembagian dengan nol
    if total_time == 0:
        print(f"Warning: Total time is zero for {num_clients} clients. Skipping this scenario.")
        return 0, 0, 0
    
    avg_response_time = total_time / num_clients
    throughput = num_clients / total_time
    latency = avg_response_time

    return avg_response_time, latency, throughput

# Fungsi untuk setiap klien yang mengirim permintaan ke server
def client_task(client_id, start_times, end_times):
    start_time = time.time()
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((coordinator_host, coordinator_port))

        message = f"Test message from client {client_id}"
        client_socket.send(message.encode('utf-8'))

        response = client_socket.recv(1024).decode('utf-8')
        print(f"Client {client_id} received: {response}")

    except Exception as e:
        print(f"Client {client_id}: Error occurred - {e}")

    finally:
        client_socket.close()
        end_time = time.time()

        # Catat waktu mulai dan selesai untuk setiap klien hanya jika koneksi berhasil
        start_times.append(start_time)
        end_times.append(end_time)

# Fungsi untuk menjalankan pengujian skenario dengan sejumlah klien
def run_test_scenario(num_clients):
    start_times = []
    end_times = []
    threads = []

    print(f"\nRunning test with {num_clients} clients...\n")

    # Buat dan mulai thread untuk setiap klien
    for i in range(1, num_clients + 1):
        t = threading.Thread(target=client_task, args=(i, start_times, end_times))
        threads.append(t)

    # Memulai semua klien
    for t in threads:
        t.start()

    # Menunggu semua klien selesai
    for t in threads:
        t.join()

    # Hitung metrik setelah semua klien selesai
    avg_response_time, latency, throughput = calculate_metrics(start_times, end_times, num_clients)
    
    # Simpan hasil hanya jika total time valid
    if avg_response_time > 0:
        result = {
            "clients": num_clients,
            "avg_response_time": avg_response_time,
            "latency": latency,
            "throughput": throughput
        }
        results.append(result)
    
    print(f"Test with {num_clients} clients complete.")
    print(f"Average Response Time: {avg_response_time:.5f} seconds")
    print(f"Latency: {latency:.5f} seconds")
    print(f"Throughput: {throughput:.5f} requests per second\n")

# Fungsi utama untuk menjalankan semua skenario pengujian
def run_all_tests():
    for scenario in client_scenarios:
        run_test_scenario(scenario)
    
    # Tampilkan hasil akhir setelah semua skenario
    print("\n==== Final Results ====\n")
    for result in results:
        print(f"Clients: {result['clients']}")
        print(f"Average Response Time: {result['avg_response_time']:.5f} seconds")
        print(f"Latency: {result['latency']:.5f} seconds")
        print(f"Throughput: {result['throughput']:.5f} requests per second\n")

if __name__ == "__main__":
    run_all_tests()
