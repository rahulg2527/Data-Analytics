#print msg
def printMsg():
	print("Hello! Welcome To Python Programming")

#print calculation
def calc(a: int, b: int):
		sum=a+b
		sub=a-b
		mul=a*b
		div=a/b
		mod=a%b
		print("Sum : "+str(sum))
		print("Difference : "+str(sub))
		print("Product : "+str(mul))
		print("Division : "+str(div)) 
		print("Modulus : "+str(mod))
# str() function is used for converting the value of anytype into string type
#return a value
def findSquare(n: int):
		square=n*n
		return square


printMsg()
calc(23,455)
x=int(input("Enter First Number : "))
y=int(input("Enter second Number : "))
calc(x,y)

result=findSquare(3)
print("Result : "+str(result))