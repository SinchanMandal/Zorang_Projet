from urllib.request import urlopen
import json
url = "https://zorang-recrutment.s3.ap-south-1.amazonaws.com/addresses.json"
response = urlopen(url)
arr = json.loads(response.read())

store_lat= 28.9428
store_long=77.2276

# for custom user input
# store_lat=float(input())
# store_long=float(input())


def comp(ele):
    val1=ele['latitude']-store_lat
    val1*=val1
    val2=ele['longitude']-store_long
    val2*=val2
    return val1+val2

arr.sort(key=comp)

tot_dist=0

for i in range(99):
    val1=arr[i]['latitude']-arr[i+1]['latitude']
    val1*=val1
    val2=arr[i]['longitude']-arr[i+1]['longitude']
    val2*=val2
    tot_dist+=val1+val2

each_dist=tot_dist/10

result=[]
ind =0

for i in range(9):
    temp=[ind]
    temp_dist=0
    while True:
        val1=arr[ind+1]['latitude']-arr[ind]['latitude']
        val1*=val1
        val2=arr[ind+1]['longitude']-arr[ind]['longitude']
        val2*=val2
        next_dist=val1+val2

        if temp_dist+next_dist<each_dist and ind+1<=100-i:
            # print(temp_dist, i, ind)
            temp_dist+=next_dist
            ind+=1
            temp.append(ind)
        else:
            break
    
    result.append(temp)
    ind+=1

temp=[]
while ind <100:
    temp.append(ind)
    ind+=1
result.append(temp)


def comp1(ele):
    return ele[1]


for i in result:
    temp=[]
    for j in i:
        temp2=[j]
        val1=arr[j]['latitude']-arr[i[0]]['latitude']
        val1*=val1
        val2=arr[j]['longitude']-arr[i[0]]['longitude']
        val2*=val2
        temp2.append(val1+val2)
        temp.append(temp2)
    temp.sort(key=comp1)

    for j in range(len(i)):
        i[j]=arr[temp[j][0]]['_id']

    
print(result)

