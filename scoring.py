filename='Worlds2017_teams'
textfile='participants.txt'
with open(filename+".csv","r") as f:
    input_array = f.readlines()
    input_array = [x.strip("\n") for x in input_array]

with open(textfile,"r") as f:
    array=f.readlines()
    array=[x.strip("\n") for x in array]

scoring_array=[]
for i in input_array:
    scoring_array.append(i.split(','))
scoring_array=scoring_array[1:]

country_array=[]
for i in array:
    country_array.append(i.split(' '))

countries=[]
points=[0]*500
gold=[0]*500
silver=[0]*500
bronze=[0]*500
participants=[]
for i in range(0,len(country_array)-1):
    countries.append(country_array[i][0])
    participants.append(int(country_array[i][1]))
countries.append('ANA')
participants.append(12)

for i in range(0,len(scoring_array)-1):
    for j in range(1,len(scoring_array[i])-1):
        if(scoring_array[i][j] != ''):
            temp=scoring_array[i][j]
            index=countries.index(temp)
            points[index]+=9-j
            if(j == 1):
                gold[index]+=1
            if(j == 2):
                silver[index]+=1
            if(j == 3):
                bronze[index]+=1

sort_array=sorted(zip(points,countries,participants,gold,silver,bronze))
points=[i[0] for i in sort_array]
countries=[i[1] for i in sort_array]
participants=[i[2] for i in sort_array]
gold=[i[3] for i in sort_array]
silver=[i[4] for i in sort_array]
bronze=[i[5] for i in sort_array]

print("Country | Points | Points per athlete sent | Gold Medals | Silver Medals | Bronze Medals")
print("-- | -- | -- | -- | -- | --")
for i in range(len(points)-1,0,-1):
    if(points[i] != 0):
        pointsper=round(points[i]/participants[i],2)
        print(countries[i]+" | "+str(points[i])+" | "+str(pointsper)+" | "+str(gold[i])+" | "+str(silver[i])+" | "+str(bronze[i]))
