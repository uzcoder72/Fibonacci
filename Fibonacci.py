class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > self.n:
            raise StopIteration
        else:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return result

fibonacci = Fibonacci(6)
for num in fibonacci:
    print(num)