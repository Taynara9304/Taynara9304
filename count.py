import time
import os

n = os.environ.get("Bom diaa! Digite o valor de sua preferência: ")
n = int(n)

for i in range(1, n):
    print(i, flush=True)
    time.sleep(1)
