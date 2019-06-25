import os

def replace_char(s, idx, ch):
    import ctypes
    OFFSET = ctypes.sizeof(ctypes.c_size_t) * 5
    a = ctypes.c_char.from_address(id(s) + OFFSET)
    pi = ctypes.pointer(a)
    pi[idx] = ch



inputfile='../labeledImg/'
outputfile='./data/my_data/train.txt'

nameList=os.listdir(inputfile)
txtFiles=[]
imageFiles=[]

for name in nameList:
    if name.endswith('.txt'):
       # print(name)
        txtFiles.append(inputfile+name)
        tempName=os.path.splitext(name)[0]
        imageFiles.append('../image/'+tempName+'.png')

i=0
imgInfs=[]
for txtfile in txtFiles:
    imgInf=str(i)+' '+imageFiles[i]
    i=i+1
    fp=open(txtfile,'r')
    lines=fp.readlines()
    for line in lines:
        lineInf=line.split()
        #print(lineInf)
        imgInf=imgInf+' '+'32'+' '+lineInf[3]+' '+lineInf[4]+' '+lineInf[1]+' '+lineInf[2]
    imgInfs.append(imgInf)
    fp.close()

fw=open(outputfile,'w')
for imgInf in imgInfs:
    fw.write(imgInf+'\n')
fw.close()







