def fibo(n):
	a,b=0,1
	print(a)
	print(b)
	i=2	
	for no in range(2,n):
		c=a+b
		print(c)
		a,b=b,c

