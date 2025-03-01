name_lst=[]
score_lst=[]
def inputName(name_lst):
    name_lst.append(input("Enter a name : "))
    return name_lst
def inputScore(score_lst):
    score_lst.append(input("Enter a score : "))
    return score_lst

def creatFile():
    file_name = input("Enter a file name : ")
    file_name+=".txt"
    f=open(file_name,"x")
    f.close()
def readFile():
    f=open("Tamrin1.txt","r")
    list=f.read()
    f.close()
    return list
def updateFile():
    f=open("Tamrin1.txt","a")
    list=f.write()
    f.close()
    return list
def deleteFile():
    pass
def maxScore():
    pass
def minScore():
    pass
def averageScore():
    pass

while():
    print("1.addName\n2.addScore\n3.creatFile\n4.readFile\n5.updateFile\n6.deleteFile\n7.maxScore\n8.minScore\n9.averageScore\n0.exit")
    num=int(input("Enter Number:"))
    if num==1:
        name_lst=inputName(name_lst)
    if num==2:
        score_lst=inputScore(score_lst)
    if num==3:
        pass
    if num==4:
        pass
    if num==5:
        pass
    if num==6:
        pass
    if num==7:
        pass
    if num==8:
        pass
    if num==9:
        pass
    if num==0:
        pass


