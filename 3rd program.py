numbers = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    num = int(input("Enter the value: "))
    numbers.append(num)
element = int(input("Enter the element to be found: "))
occurrences = numbers.count(element)
print(f"Element {element} occurs {occurrences} times in the list.")
positive = []
negative = []
for i in range(len(numbers)):
    if numbers[i] == element:
        positive.append(i)
        negative.append(i - len(numbers))
print("Positive Index:", positive)
print("Negative Index:", negative)
is_ascending = all(numbers[i] <= numbers[i+1]for i in range(len(numbers)-1))
if is_ascending:
    print("Yes, the list is in ascending order.")
else:
    print("No, the list is not in ascending order.")
