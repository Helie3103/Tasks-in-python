n = int(input("How many elements do you want to enter in list: "))
l = []
even_total = 0
even_avg = 0
odd_total=0
odd_avg = 0
largest_even = 0
smallest_even = 0
largest_odd = 0
smallest_odd = 0
total = 0
avg=0
odd = []
even = []
d = {}
max_count = 0

def freq(value):
    global max_count
    global total
    if value in d:
        d[value] += 1
    else:
        d[value] = 1

    if d[value]>max_count:
        max_count=d[value]
    total = total + value

def odd_check(value):
    global largest_odd
    global smallest_odd
    if value > largest_odd:
        largest_odd = value
    if value < smallest_odd or smallest_odd == 0:
        smallest_odd = value

def even_check(value):
    global largest_even
    global smallest_even
    if value > largest_even:
        largest_even = value
    if value <smallest_even or smallest_even == 0:
        smallest_even = value

def most_repeated_func(d):
    global max_count
    most_repeated = []
    for i in d:
        if d[i] == max_count and max_count != 1:
            most_repeated.append(i)
    if len(most_repeated) == 0:
        most_repeated = None
    return most_repeated
    
for i in range(n):
    value = int(input(f"Enter element {i} of your list: "))
    l.append(value)

    freq(value)

    if value % 2 == 0:
        even.append(value)
        even_total = even_total + value
        even_check(value)
    else:
        odd.append(value)
        odd_total = odd_total + value
        odd_check(value)

if len(even) > 0:
    even_avg = even_total / len(even)
if len(odd) > 0:
    odd_avg = odd_total / len(odd)
avg = total / len(l)

output={
    "orignal_list" : l,
    "odd" : odd,
    "even": even,
    "largest odd": largest_odd,
    "largest even": largest_even,
    "smallest odd": smallest_odd,
    "smallest even": smallest_even,
    "Average": avg,
    "Odd average": odd_avg,
    "Even average": even_avg,
    "most repeated value": most_repeated_func(d=d)
}
print(output)