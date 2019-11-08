a=100000000
sum=0
b=0
laba = [int(0), int(0), int(a)*.1, int(a)*.1, int(a)*.5, int(a)*.5, int(a)*.5,
        int(a) *.2]
print ("Modal awal pengusaha:",a)
for i in laba :
    sum = sum+i
    b+=1
    print("Laba bulan ke-",b,"sebesar:", i)
print("Total Laba adalah:", sum)
