import sys
def creatFile():
    # file_name = input("Enter a file name : ")
    # file_name+=".txt"
    f=open("ScoreList.txt","x")
    f.close()
def readFile():
    f=open("ScoreList.txt","r")
    list=f.read()
    f.close()
    return list
def addNameScore(name,score):
    f=open("ScoreList.txt","a")
    f.write(f"{name},{score}\n")
    f.close()
def editNameScore():
    pass
def deleteNameScore():
    pass
def maxScore(score_lst,name_lst):
    max_score=0
    for i in range(len(score_lst)):
        if score_lst[i]>max_score:
            max_score=score_lst[i]
            max_name=name_lst[i]
    return max_score,max_name
def minScore(score_lst,name_lst):
    min_score=100
    for i in range(len(score_lst)):
        if score_lst[i]<min_score:
            min_score=score_lst[i]
            min_name=name_lst[i]
    return min_score,min_name
def averageScore(score_lst):
    sum=0
    n=len(score_lst)
    for i in score_lst:
        sum+=i
    avg=sum/n
    return avg


while True:
    name_lst = []
    score_lst = []
    list_dic = {}
    list = readFile()
    list_ = list.split("\n")
    list_.pop()
    for i in list_:
        name_score = i.split(",")
        name_lst.append(name_score[0])
        score_lst.append(int(name_score[1]))
    # print("Menu:")
    print("1.creatFile|2.readFile|3.addNameScore|4.editNameScore|5.deleteNameScore|6.maxScore|7.minScore|8.averageScore|0.exit")
    # print(100*"*")
    num=int(input("Enter Number:"))
    if num==1:
        try:
            creatFile()
            print("Secsesfull!")
            # print(100 * "*")
        except:
            print("File was existed!")
            # print(100 * "*")
    if num==2:
        try:
            list=readFile()
            list_=list.split("\n")
            list_.pop()
            for i in list_:
                name_score=i.split(",")
                print("name:",name_score[0],"|","score:",name_score[1])
            # print(100 * "*")
        except:
            print("File not found or your file is empty!\nPlease creat file or add note to file!")
            # print(100 * "*")
    if num==3:
        try:
            name=input("Enter a name : ")
            score=input("Enter a score : ")
            # name_lst.append(name)
            # score_lst.append(int(score))
            addNameScore(name,score)
            print("Successfully added!")
            # print(100 * "*")
        except:
            print("Error")
            # print(100 * "*")
    if num==4:
        pass
    if num==5:
        pass
    if num==6:
        max_score,max_name=maxScore(score_lst,name_lst)
        print("Max score :",max_score,"|","Name :",max_name)
        # print(100 * "*")
    if num==7:
        min_score,min_name=minScore(score_lst,name_lst)
        print("Min score :",min_score,"|","Name :",min_name)
        # print(100 * "*")
    if num==8:
        try:
            list = readFile()
            list_ = list.split("\n")
            list_.pop()
            for i in list_:
                name_score = i.split(",")
                score_lst.append(int(name_score[1]))

            avg=averageScore(score_lst)
            print("average score:",avg)
            # print(100 * "*")
        except:
            print("Error")
            # print(100 * "*")
    if num==0:
        sys.exit()


