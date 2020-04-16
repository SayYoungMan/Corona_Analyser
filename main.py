import time
from load import load

start_time = time.time()

load()

print("--- %s seconds ---" % (time.time() - start_time))