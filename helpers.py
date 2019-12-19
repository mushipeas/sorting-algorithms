import time

class clock_maker:

    def __init__(self, runs=0):
        self.runs = int(runs)
        self.total_time = 0
        self.total_runs = 0

    def __call__(self, func):

        _name = func.__name__ if hasattr(func, '__name__') else type(func).__name__ 

        def clocked(*_args):
            t0 = time.time()
            _result = func(*_args)
            elapsed_t = time.time() - t0
            self.total_time += elapsed_t
            self.total_runs += 1
            msg = "{} runs of {}(): {:1.4f}s on average."
            if self.runs == self.total_runs: print(msg.format(self.runs, _name, self.total_time / self.total_runs))
            return _result

        return clocked

    def avgtime(self):
        return self.total_time / self.total_runs 


if __name__ == "__main__":
    
    @clock_maker(runs=5)
    def testrun1(n):
        print("TR1: I've run {} times.".format(n))
    
    @clock_maker(runs=6)
    def testrun2(n):
        print("TR2: I've run {} times.".format(n))

    for n in range(1,8):
        testrun1(n)
        testrun2(n)
