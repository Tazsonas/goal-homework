# ეკრანზე გამოიტანეთ თითოეული ცვლადი და კომენტარებით მიუწერეთ რას გამოიტანს და რატომ,
#  შემდეგ მათი კომბინაციები დაბეჭდეთ (მაგალითად a and b ან c or i და ასე შემდეგ) მატაც მიუწერეთ რას გამოიტანს და რატომ 

a = 5 == 5
b = 10 != 20
c = 4 > 3 and 2 < 5
d = 10 > 20 or 5 < 8
e = not (7 > 3)
f = "hello" == "world"
g = 15 >= 10
h = 8 <= 8
i = 3 > 1 and 2 == 2 and 4 != 5
j = not (10 < 5 or 2 == 2)

print(a and b) # True
print(c or d) # True
print(e and f) # False
print(g or h)  # True
print(i and j) # False

