def readDrop(file):
    f = open(file)
    line=f.readline()
    file_number=1
    m=0
    while line:
        if line[:1] == '*' :
            f_out=open('drop_'+str(file_number)+'.txt','w')
            lat,lon,yy,mm,dd,size=readHead(line)
            f_out.write('{0} {1}\n'.format(lat,lon))
            readBody(f,f_out,size)
            f_out.close()
            file_number+=1
        line=f.readline()


def readHead(line):
    head=line.split(' ')
    drop_size=int(line[-3:].strip())
    drop_lat=float(head[1][0:4])/100.
    drop_lon=float(head[1][4:])/100.
    drop_yy=int(head[2][0:3])+2000
    drop_mm=int(head[2][3:5])
    drop_dd=int(head[2][5:])
    return drop_lat,drop_lon,drop_yy,drop_mm,drop_dd,drop_size

def readBody(f,f_out,size):
    line=f.readline()
    status=True
    while int(line[-3:]) < int(size):
        if line[:2] == '25':
            status=False
            line=f.readline()
            continue
        if status :
            press=float(line[2:7])/10.
            v1=line[7:12]
            v2=line[14:18]
            v3=line[20:24]
            v4=line[26:29]
            v5=line[29:32]
            f_out.write('{0} {1} {2} {3} {4} {5}\n'.format(press,v1,v2,v3,v4,v5))
            line=f.readline()
        else:
            line=f.readline()
            
        

if __name__ == '__main__':
    dropsonde_file="ux2022111700.dat"
    readDrop(dropsonde_file)