from concurrent.futures import ThreadPoolExecutor
import time

def task(id):
    print(f"Task {id} is starting")
    time.sleep(1)  # Simula um trabalho que leva tempo
    print(f"Task {id} is completed")
    return id

num_threads = 4  # Ajuste o número de threads para 4

with ThreadPoolExecutor(max_workers=num_threads) as executor:
    results = list(executor.map(task, range(10)))

print("All tasks completed:", results)
