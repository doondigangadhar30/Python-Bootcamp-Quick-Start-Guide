student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
#type1
minimum = student_scores[0]
for ele in student_scores:
    if ele<minimum:
        minimum=ele
print(f"minimum element is: {minimum}")
maximum = 0
for ele in student_scores:
    if ele>maximum:
        maximum=ele
print(f"maximum element is: {maximum}")
print(f"length of list is: {len(student_scores)}")
s=0
for elem in student_scores:
    s+=elem
print(f"sum of elements is: {s}")
#type2
a1=max(student_scores)
a2=min(student_scores)
a3=sum(student_scores)
print(f"minimum element is: {a2}")
print(f"maximium element is: {a1}")
print(f"sum of all elements is: {a3}")
