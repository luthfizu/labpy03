print("menentukan bilangan terbesar ")
print("jika muncul bilangan 0 maka program selesai")
print(" ")

max=0
while True:
	a=int(input("masukkan bilangan="))
	if max < a:
		max = a
	if a==0:
		break
print("\nbilangan terbesar=",max)
