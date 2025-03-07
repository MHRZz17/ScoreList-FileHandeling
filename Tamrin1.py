import sys
def creatFile():
    f=open("ScoreList.txt","x")
    f.close()
def readFile():
    f=open("ScoreList.txt","r")
    list=f.read()
    f.close()
    return list
def addNameScore():
    name = input("Enter a name: ")
    name = name.lower()
    if name.isalpha()==False:
        print("Invalid Name!Please try again(just use alphabet)")
        return addNameScore()
    score = input("Enter a score(0-100): ")
    if score.isdigit()==False:
        print("Invalid Score!Please try again(just use digit)")
        return addNameScore()
    if int(score)>100 or int(score)<0:
        print("Inputed score out of range!Please try again")
        return addNameScore()
    f=open("ScoreList.txt","a")
    f.write(f"{name},{score}\n")
    f.close()
    print("Name and score successfully Added!")
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

try:
    creatFile()
    print("Text file created successfully!")
    addNameScore()
except:
    pass

while True:
    name_lst = []
    score_lst = []
    list = readFile()
    list_ = list.split("\n")
    list_.pop()
    for i in list_:
        name_score = i.split(",")
        name_lst.append(name_score[0])
        score_lst.append(int(name_score[1]))

    print("1.ShowList|2.AddName&Score|3.MaxScore|4.MinScore|5.AverageScore|0.Exit")
    try:
        num=int(input("Enter Number of your choice:"))
    except:
        print("Invalid Input!\nPlease try again!")
        continue
    if num==1:
            list=readFile()
            list_=list.split("\n")
            list_.pop()
            for i in list_:
                name_score=i.split(",")
                print("name:",name_score[0],"|","score:",name_score[1])
    elif num==2:
            addNameScore()
    elif num==3:
        max_score,max_name=maxScore(score_lst,name_lst)
        print("Max score :",max_score,"|","Name :",max_name)
    elif num==4:
        min_score,min_name=minScore(score_lst,name_lst)
        print("Min score :",min_score,"|","Name :",min_name)
    elif num==5:
        avg=averageScore(score_lst)
        print("average score:",avg)
    elif num==0:
        sys.exit()
    else:
        print("Invalid Input!\nPlease try again!")


