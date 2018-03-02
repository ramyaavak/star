n=int(raw_input())
k=0
for i in range(2,n):
         if(n%i==0):
              k=k+1
if(k==0):
   print "NO"
else:
    print "YES"
