import numpy
nums = [1, 5, 1, 1, 6, 4]
key = numpy.median(nums)
print("key:", key)

a = 1 & 1 == 1
b = 0 | 0 == 1
print("a-TorF:", a, "b-TorF:", b)

a = int(0b110)
b = int(0b011)
print("a:", a, "b:", b)
h = a | b
c = int(0b111)
q = a & b
d = int(0b010)
print("h:", h, "q:", q, "c:", c, "q:", q)

print("0 to binary:", bin(0))
print("1 to binary:", bin(1))
print("2 to binary:", bin(2))
print("3 to binary:", bin(3))
print("4 to binary:", bin(4))
print("5 to binary:", bin(5))
print("6 to binary:", bin(6))

res = 11 & (1 << 2) == 0

print("&:", bin(11 & (1 << 2)))
print("res:", res)
print("11 to binary:", bin(11))
print("bin-1<<2:", bin(1 << 2))
print("bin-1<<2|0:", bin((1 << 2) | 0))

print("TorF:", 0b100 == 0b0)
#n = bin(0b100 & 0b000)
n = 0b100 & 0b000
print("n:", n, "TorF:", n == 0)

k = 0b100 | 0b10001
print("k:", bin(k), "k:", k)

mask = 0b10
print("afterMask:", bin(0b111111 & mask))

print("num:", int(0b00000))


k = 0b0 | 0b1000000000
print("k:", bin(k), "k:", k)

k = 0b00 | 0b1000000000
print("k:", bin(k), "k:", k)

k = 0b10 & 0b100
print("k:", bin(k), "k:", k)
