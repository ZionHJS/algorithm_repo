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
