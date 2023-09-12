#1
print("\n\n1#1:");

length = float(input("Введите длину комнаты в метрах: "));
width = float(input("Введите ширину комнаты в метрах: "));
height = float(input("Введите высоту комнаты в метрах: "));

if length <= 0 or width <= 0 or height <= 0:
    print("Неверный ввод. Размеры должны быть положительными числами.");

else:
    volume = length * width * height;
    print(f"«Объем комнаты = {volume} кубических метров».");

    if volume < 48:
        print("Комната маленькая");
    elif volume < 96:
        print("Комната средняя");
    else:
        print("Комната большая");



#2
print("\n\n#2:");

length = int(input("Введите длину последовательности Фибоначчи: "));

if length <= 0:
    print("Неверный ввод. Число должно быть положительным.");

else:
    even = 0;
    subsequence = []
    if length >= 1:
        subsequence.append(0)
    if length >= 2:
        subsequence.append(1)
        even += 1 # А инкремент где? Хочу обратно в С++ или С#.

    while len(subsequence) < length:
        subsequence.append(subsequence[-1] + subsequence[-2])
        if subsequence[-1] % 2 == 0:
            even += 1

    print(subsequence)

    evenPercentage = float(100 / length * even)
    print(f"Процент четных = {evenPercentage}%")