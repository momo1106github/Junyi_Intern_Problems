
def f(str):
	lst = str.split()
	for i in range(len(lst)):
		lst[i] = lst[i][::-1]
	return ' '.join(lst)

print (f("junyiacademy"))
print (f("flipped class room is important"))