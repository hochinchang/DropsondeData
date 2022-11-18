def readDrop(file):
    f = open(file)
    line = True
    m=0
    while line:
        line=f.readline()
        if line[0:1] == '*' :
            lat,lon,yy,mm,dd,size=readHead(line)
            for ii in range()


def readHead(line):
    head=line.split(' ')
    drop_size=int(line[-3:-1])
    drop_lat=int(head[1][0:4])
    drop_lon=int(head[1][4:])
    drop_yy=int(head[2][0:3])+2000
    drop_mm=int(head[2][3:5])
    drop_dd=int(head[2][5:])
    return drop_lat,drop_lon,drop_yy,drop_mm,drop_dd,drop_size
    
if __name__ == '__main__':
    dropsonde_file="ux2022111700.dat"
    readDrop(dropsonde_file)