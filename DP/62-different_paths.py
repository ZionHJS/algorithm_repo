import numpy

def uniquePaths(m, n):
        opt = numpy.zeros([m+1,n+1])
        opt[1,1] = 1
        opt[1,2] = 1
        opt[2,1] = 1
        return print(opt)
uniquePaths(10,10)

class Solution(object):
    def uniquePaths(self, m, n):
        opt = numpy.zeros([m+1,n+1])
        opt[1,1] = 1
        opt[1,2] = 1
        opt[2,1] = 1
        return print(opt)
obj = new Solution(10,10)
obj.uniquePaths)()