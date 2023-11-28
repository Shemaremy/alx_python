
z = []
p=0
q=1
for i in range(0,7,1):
        if i<=1 :
            for j in range(0,1,1):
                z[j]=i

            
        else:
            c=p+q
            for l in range(2,7):
                 z[l]= i
            
            p=q
            p=c


print(", ".join("{}".format(v) 

for i in range(7)
 
               ),end="")
