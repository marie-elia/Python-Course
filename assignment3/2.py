# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 23:05:49 2019

@author: marie
"""

dicti={0:'me',1:'Rick',2:'Jamie',3:'Heather',4:'Bryan',5:'Ray',6:'Bas',7:'Patrick',8:'Derek',9:'Joshua'}
Relations=[[0,2,4],[0,1,2],[0,4,0],[0,5,0],[0,7,2],[0,8,0],[0,6,0],[0,9,0],[0,3,8],[1,4,3],[1,6,3],
           [4,6,0],[4,5,0],[5,6,3],[5,7,5],[7,6,7],[6,9,0],[6,3,4],[6,2,0],[8,3,2],[9,3,6],[3,2,9]]
friends={}
#filling the 'friends' dictionary so that each person is a key and his friends are the vlues
for i in range(len(dicti)):
    for friend in Relations: #looping over every list to search for the friends in relation with i which represent the person
        if i in friend and i== friend[0]:#if i is found in any tuple whether 1st element or 2nd the other element will be put in his list of friends
            friends.setdefault(dicti[i], []).append(dicti[friend[1]])
        if i in friend and i== friend[1]:
            friends.setdefault(dicti[i], []).append(dicti[friend[0]])

print("list of all friends of friends: ")
mylist=[]
friendsoffriends=set()  #set to remove any duplicate values
for friend in friends : # for every key in the dictionary
    print("friends of friends of "+str(friend)) #output  the person that we want to get every friend of his friends
    for i in friends[friend]:# iterate over all the friends in the list of friends of friend
        for k in friends[i]: #iterate over every friend in the list of friends of friends of friend
          if friend not in friends[k]:        #checking that every friend in the list of friends of friends is not a direct friend with a friend
            mylist.append(k)    #creating list and inserting the list of friends of the first friend of friend
        for j in  range(len(mylist)):    #adding the elements of the list in a set to avoid duplication when adding the friends of the next friend
            friendsoffriends.add(mylist[j])
        mylist.clear()         #clearing the list 
    friendsoffriends.remove(friend)     # removing the person himself from the list
    
    if len(friendsoffriends) == 0:
        print(str(friend)+ " doesn't have friends of friends because he is a friend of everyone ")# for people who are friends with everyone like me
    else:
        print(friendsoffriends) #else i print my friend of friends
    friendsoffriends.clear()  #clearing the set for the next person
