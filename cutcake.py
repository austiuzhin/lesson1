def cut_cake(parts):
	try:
		return 1/int(parts)
	except (ZeroDivisionError, TypeError, ValueError):
		return "Вы что с ума посходили?!"

cake = cut_cake('you')
print(cake)
