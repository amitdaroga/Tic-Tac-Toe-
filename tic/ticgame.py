import datetime

lst=['0','1','2','3','4','5','6','7','8','9']
def datastore(player1,player2,win):
    file=open("ticscore","a")
    date=datetime.datetime.now()
    file.write(str(date)+"\n"+"player1 :"+player1+" "+"player2 :"+player2+"\n"+"winer : "+win+"\n")
    file.close()
def startcoin(*players):
    ck=[]
    file=open("ticcoin","r")
    read=file.readlines()
    for i in read:
        k=i.split("=")
        ck.append(k[0])
    file.close()
    for j in players:
        if j not in ck:
            print("welcome you play first time "+j)
            file2=open("ticcoin","a")
            file2.write(j+"="+"5000\n")
            file2.close()
    file.close()

def increment(name,coin,win):

    file=open("ticcoin","r")
    read=file.readlines()
    file.close()
    file2=open("ticcoin","w")
    for i in read:
       data=i.split("=")
       if name in data[0]:
           if win==1:
               coin=int(data[1])+coin
               file2.write(name+"="+str(coin)+"\n")
           else:
               coin=int(data[1])-coin
               file2.write(name+"="+str(coin)+"\n")
       else:
           file2.write(i+"\n")

def display_board():
    print("      |      |      ")
    print(f"  {lst[1]}   |  {lst[2]}   |  {lst[3]}    ")
    print("______|______|______")
    print("      |      |      ")
    print(f"  {lst[4]}   |  {lst[5]}   |  {lst[6]}    ")
    print("______|______|______")
    print("      |      |      ")
    print(f"  {lst[7]}   |  {lst[8]}   |  {lst[9]}    ")
    print("      |      |      ")

def check_win():
    if lst[1]==lst[2]==lst[3]:
        return 1
    elif lst[4]==lst[5]==lst[6]:
        return 1
    elif lst[7]==lst[8]==lst[9]:
        return 1
    elif lst[1]==lst[4]==lst[7]:
        return 1
    elif lst[2]==lst[5]==lst[8]:
        return 1
    elif lst[3]==lst[6]==lst[9]:
        return 1
    elif lst[1]==lst[5]==lst[9]:
        return 1
    elif lst[3]==lst[5]==lst[7]:
        return 1
    else :
        if lst[1]=='1' or lst[2]=='2' or lst[3]=='3' or lst[4]=='4' or lst[5]=='5' or lst[6]=='6' or lst[7]=='7' or lst[8]=='8' or lst[9]=='9':
            return -1
        else:
            return 0
pl_name=input("Enter player 1 name : ")
pl_name2=input("enter player 2 name :")
print("welcome players if you are play first time you give to 5000\ncoin and you are play second time play game your last time  coins give you")
rsp1=int(input(pl_name+" please enter how many coin want you play :"))
rsp2=int(input(pl_name2+" please enter how many coin want you play :"))
startcoin(pl_name,pl_name2)
if rsp1 ==rsp2:
    i=-1
    player=1
    while(i==-1):
        display_board()
        player=player%2
        if player==0:
            player=2
            name=pl_name2
            mark='X'
        else:
            player=1
            mark='O'
            name=pl_name
        print(" Player ",name)
        choice=int(input("Enter choice :: "))
        if choice==1 and lst[1]=='1':
            lst[1]=mark
        elif choice==2 and lst[2]=='2':
            lst[2]=mark   
        elif choice==3 and lst[3]=='3':
            lst[3]=mark    
        elif choice==4 and lst[4]=='4':
            lst[4]=mark    
        elif choice==5 and lst[5]=='5':
            lst[5]=mark
        elif choice==6 and lst[6]=='6':
            lst[6]=mark
        elif choice==7 and lst[7]=='7':
            lst[7]=mark
        elif choice==8 and lst[8]=='8':
            lst[8]=mark
        elif choice==9 and lst[9]=='9':
            lst[9]=mark
        else:
            print("Invalid input ")
            player = player-1    
        i=check_win()
        player = player +1
        if i==1:
            display_board()
            player = player -1
            if player==1:
                
                datastore(pl_name,pl_name2,pl_name)
                increment(pl_name,rsp1,1)
                increment(pl_name2,rsp2,0)
                print(f"{pl_name}  player win")
                print(f"{pl_name}  win coin {rsp1}")
                print(f"{pl_name2}  loss coin {rsp1}")
            else:
                datastore(pl_name,pl_name2,pl_name2)
                increment(pl_name,rsp1,0)
                increment(pl_name2,rsp2,1)
                print(f"{pl_name}  loss coin {rsp2}")
                print(f"{pl_name2}  win coin {rsp1}")
                print(f"{pl_name2}  player win")
        else:
            print("No result")
else:
    print("please enter simler coin for another player again play game :")
