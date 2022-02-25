#palindrome
x=int(input("enter a number: "))
def pals(x):
    temp=x
	rev=0
	   while(x>0):
       d=x%10
       rev=rev*10+d
       x=x//10
    if(rev==temp):
        print("palindrome")
	else:
    	print("not palindrome")
orint("This is vamshi")
print("These are my prends:Seswitha, Chadana, Pasyanthi")
