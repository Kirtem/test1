# Задача 2.2 Военкомат 
age= int(input("Введите свой возраст:"))
study = input("Вы сейчас учитесь?(да/нет):")
children = int(input("Введите кол-во детей:"))
height = int(input("Введите свой рост(см)"))

if 18 <= age < 30:
	if study.lower() == "да":
		print("Отсрочка от армии до конца обучения.")
	elif study.lower() == "нет":
		if children >= 2:
			print("Отсрочки от армии по семейным обстоятельствам.")
		elif children <= 1:
			if height < 170:
				print("В танкисты.")
			elif height < 185:
				print("На флот.")
			elif height < 200:
				print("В десантники.")
			else:
				print("В другие войска.")		
	else:
		print("Некорректное значение.")
else:
	print("Непризывной возраст.")

print("Приветики")

a =  4 + 2
print(a)
