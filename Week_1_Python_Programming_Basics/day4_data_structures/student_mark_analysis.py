
marks = [78, 45, 90, 67, 88, 34, 56, 91, 73, 60]

total_marks = 0;

for m in marks:
    total_marks += m;

highest = marks[0]
lowest = marks[0]

for m in marks:
    if m > highest:
        highest = m

for n in marks:
    if n < lowest:
        lowest = n

passed = 0;
failed = 0;

for m in marks:
    if m >= 50:
        passed += 1;
    elif m < 50:
        failed +=1;


average = total_marks/len(marks)

print(total_marks)
print(average)
print(highest)
print(lowest)
print(passed)
print(failed)