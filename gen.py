def sq_gen(n):
    for i in range(1, n + 1):
        yield i * i

# gen = sq_gen(5)
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())

def print_even():
    n = int(input('n = '))
    def ev_gen(n):
        for i in range(0, n + 1, 2):
            yield i

    ev_nums = ', '.join(str(num) for num in ev_gen(n))
    print(ev_nums)

# print_even()
    
def div_3_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for i in div_3_4(25):
    print(i)

# for num in div_3_4(30):
#     print(num)

def sq_a_b(a, b):
    for i in range(a, b + 1):
        yield i * i

# for num in sq_a_b(3, 6):
#     print(num)

def from_n_0(n):
    for i in range(n, -1, -1):
        yield i

# for i in from_n_0(4):
#     print(i)
