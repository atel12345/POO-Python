def F7(n1,s):
	s+=n1
	if (s>2):
		n1=n1+1
	print(f"{s}")
	if (n1<10):
		F7(n1,s)
		
F7(1,0)
