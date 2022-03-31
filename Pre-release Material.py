midday=[]
midnight=[]
count=0
temp=0
count1=0
total=0
total2=0
#this sectioon for input valid temperatures in 5 day
for count in range(0,5):
    midday.append(0)
    midnight.append(0)
    print(("Please input temperature of midday in"),int(count+1),("day"))
    temp=int(input())
    while temp<-30 or temp>60:
            print("Input valid number")
            temp=int(input())
    print(("Please input temperature of midnight in"),int(count+1),("day"))
    midday[count]=temp
    print("Your number accepted")
    temp=int(input())
    while temp<(-30) or temp>60:
        print("Input valid number")
        temp=int(input())
    midnight[count]=temp
    print("Your number accepted")
print(("This is midday temperature which are entered"),midday)
print(("This is midnight temperature which are entered"),midnight)
#this section for find avarage of temperature of midday and midnight
for count1 in range(0,4):
    total=total+midday[count1]
    total2=total2+midnight[count1]
print(("This is avarage temperature of middays in 5 days:"),total/4)
print(("This is avarage temperature of midnights in 5 days:"),total2/4)
#this section for find highest temperature of midday and midnight
highday=midday[0]
highnight=midnight[0]
for count in range(0,4):
    if highday<midday[count]:
        highday=midday[count]
    if highnight<midnight[count]:
        highnight=midnight[count]
print(highday, highnight)
print(("This is highest temperature of midday in 5 days"),highday)
print(("This is highest temperature of midnight in 5 days"),highnight)
