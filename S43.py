from datetime import *
from time import *

def time():
    start_time = datetime.now()
    while datetime.now() - start_time < timedelta(seconds=5):
        current_time = datetime.now()
        print(current_time.strftime('%X'))
        sleep(1)

if __name__ == "__main__":
    time()