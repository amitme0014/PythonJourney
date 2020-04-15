import re

file=open('/Users/amitsingh/PycharmProjects/replacePattern/list.txt','r')
fileCreate=open('/Users/amitsingh/PycharmProjects/replacePattern/listOutput','w+')
fileWithoutRep=open('/Users/amitsingh/PycharmProjects/replacePattern/listOutputWithoutRep','w+')

for i in file:
    x=re.findall("[|][0-9]{6}[|][0-9][|][0-9]", i)
    x = re.sub("[|][0-9]{6}[|][0-9][|][0-9]", "", i)
    fileCreate.write(x)


fileCreate.close()
lines_seen = set()

for k in open('/Users/amitsingh/PycharmProjects/replacePattern/listOutput','r'):
        print(k)
        if k not in lines_seen:
            fileWithoutRep.write(k)
            lines_seen.add(k)
fileWithoutRep.close()

        #print lines_seen





    # if x:
    #     print("Got Matched")
    # else:
    #     print("No Match")
    #

    #print i
    #print(i.replace("[|][0-9][|][0-9][|][0-9]",""))
