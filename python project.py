names = ['sonu','prince','ashi']
marks = [95,40,90]
updates = [6,-6,10]
l1 = []
l2 = []
for i in range(len(names)):
    l1.append([marks[i] , names[i]])
    l2.append([marks[i] + updates[i] , names[i]])
l1.sort(reverse = True)
l2.sort(reverse = True)
ranker = l2[0][1]
jump = 0
for i in range(len(l2)):
    if l2[i][1] == ranker:
         jump = i
         break

print("Ranker: ",ranker)
print("Jump: ",jump)
              
              
              
              
              
