a=int(input("enter the start no"))
b=int(input("enter the end no"))
 
def armstrong(n):
	o=len(str(n))
	sum=0
	temp=n
	while(temp!=0):
		digit=temp%10
		sum+=digit**o
		temp//=10

	if(n==sum):
		print(n,"it is a armstrong")
for i in range(a,b):
	armstrong(i)
 
 