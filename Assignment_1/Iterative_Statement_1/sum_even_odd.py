#Program to calculate sum of all even numbers and odd numbers.
num = int(input("Input number:"))
even_sum = 0
odd_sum = 0
for i in range(0, num+1):
    if i%2==0:
        even_sum += i
    else:
        odd_sum += i
print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")

