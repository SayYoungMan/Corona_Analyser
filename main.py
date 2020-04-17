import time
from update import update

start_time = time.time()

# Load data
update()



print("--- %s seconds ---" % (time.time() - start_time))