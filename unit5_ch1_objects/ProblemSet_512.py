def main():
    counter = Counter()
    num = 0
    for x in range(0, 100):
        incrementor(counter, num)
    return (counter.count, num)

def incrementor(c, num):
    c.count = c.count + 1
    num = num + 1

class Counter:
    def __init__(self):
        self.count = 0

aTuple = main()
print(aTuple)
