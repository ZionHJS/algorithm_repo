import itertools
a = [1, 2, 3, 4, 5, 6]
print("res:", itertools.product(*a))

a = "e"
s = a.split(",")
print("s:", s)

b = "{a,b}{c,{d,e}}"
print("s:", b.split("},"))

props = []
a = props.pop()
print("a:", a)

stack = [""]
print("len:", len(stack))

stack = [[]]
print("stack:", stack)


a = ["ncaa", "ncaaiawn", "ncaaown", "ncaaxwn", "ncaer", "ncaia", "ncao", "ncaw", "ncax", "ngaa", "ngaaiawn", "ngaaown", "ngaaxwn", "ngaer", "ngaia", "ngao", "ngaw", "ngax", "nhaa", "nhaaiawn", "nhaaown", "nhaaxwn",
     "nhaer", "nhaia", "nhao", "nhaw", "nhax", "njaa", "njaaiawn", "njaaown", "njaaxwn", "njaer", "njaia", "njao", "njaw", "njax", "nlaa", "nlaaiawn", "nlaaown", "nlaaxwn", "nlaer", "nlaia", "nlao", "nlaw", "nlax"]

b = ["ncaaiawn", "ncaan", "ncaaown", "ncaaxwn", "ncaern", "ncaian", "ncaon", "ncawn", "ncaxn", "ngaaiawn", "ngaan", "ngaaown", "ngaaxwn", "ngaern", "ngaian", "ngaon", "ngawn", "ngaxn", "nhaaiawn", "nhaan", "nhaaown", "nhaaxwn",
     "nhaern", "nhaian", "nhaon", "nhawn", "nhaxn", "njaaiawn", "njaan", "njaaown", "njaaxwn", "njaern", "njaian", "njaon", "njawn", "njaxn", "nlaaiawn", "nlaan", "nlaaown", "nlaaxwn", "nlaern", "nlaian", "nlaon", "nlawn", "nlaxn"]
