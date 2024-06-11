#First solution
def rgb(r, g, b):
    r = max(0,min(r,255))
    g = max(0,min(g,255))
    b = max(0,min(b,255))
    return "{:02X}{:02X}{:02X}".format(r,g,b)

print(rgb(255, 255, 255))

#lambda solution
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))