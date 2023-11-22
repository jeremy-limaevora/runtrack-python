min_number = 1  
max_number = 1000  

print("Nombres premiers entre", min_number, "et", max_number, ":")

for num in range(min_number, max_number + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num)
