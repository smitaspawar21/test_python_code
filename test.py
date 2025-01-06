import time
import concurrent.futures

iterations = 10000000000

def worker(num_iterations):
    for _ in range(num_iterations):
        pass

if __name__ == "__main__":
    num_cores = concurrent.futures.ProcessPoolExecutor()._max_workers
    iterations_per_core = iterations // num_cores

    start_time = time.time()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(worker, iterations_per_core) for _ in range(num_cores)]
        concurrent.futures.wait(futures)

    end_time = time.time()

    duration = end_time - start_time

    print("Duration: ", duration, " seconds")
