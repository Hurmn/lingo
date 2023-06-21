import time

class Timer:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0

    def get_elapsed_s(self):
        sec = time.time() - int(self.start_time)
        return int(sec)

    def get_elapsed_time(self):
        #in principe hetzelfde als hierboven maar ipv alleen seconden ook minuten
        self.end_time = time.time()

        sec = self.end_time - self.start_time

        mins = sec // 60
        sec = sec % 60
        mins = mins % 60
        print("Time Lapsed = {0}:{1}".format(int(mins),sec))
        return "totale tijd = {0}:{1}".format(int(mins),int(sec))

    def reset(self):
        self.start_time = time.time()
        print(self.start_time)