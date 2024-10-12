import socket
import time

NUM_CLIENTS = 100  # Jumlah klien yang akan mengirim permintaan
coordinator_host = '127.0.0.1'
coordinator_port = 8000

# Variabel untuk menghitung waktu
start_times = []
end_times = []

# Fungsi untuk mengukur waktu rata-rata, latensi, dan throughput
def calculate_metrics():
    total_time = sum([end - start for start, end in zip(start_times, end_times)])
    avg_response_time = total_time / NUM_CLIENTS
    throughput = NUM_CLIENTS / total_time
    latency = total_time / NUM_CLIENTS  # Latency kira-kira sama dengan waktu respons rata-rata dalam hal ini

    print(f"\n==== Single-threading Test Results ====")
    print(f"Average Response Time: {avg_response_time:.5f} seconds")
    print(f"Throughput: {throughput:.5f} requests per second")
    print(f"Latency: {latency:.5f} seconds\n")

# Fungsi untuk mengirim permintaan secara berurutan (single-thread)
def single_thread_test():
    for i in range(1, NUM_CLIENTS + 1):
        start_time = time.time()
        
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((coordinator_host, coordinator_port))

        message = f"Test message from client {i}"
        print(f"Sending: {message}")
        client_socket.send(message.encode('utf-8'))

        response = client_socket.recv(1024).decode('utf-8')
        print(f"Received: {response}")

        client_socket.close()
        end_time = time.time()

        start_times.append(start_time)
        end_times.append(end_time)

    calculate_metrics()

if __name__ == "__main__":
    single_thread_test()
