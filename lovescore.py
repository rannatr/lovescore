# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


name1_lower = name1.lower()
name2_lower = name2.lower()
t1=name1_lower.count("t")
t2=name2_lower.count("t")
total_t = t1 + t2
r1 =name1_lower.count("r")
r2 = name2_lower.count("r")
total_r = r1 + r2
u1 =name1_lower.count("u")
u2 = name2_lower.count("u")
total_u = u1 + u2
e1 =name1_lower.count("e")
e2 = name2_lower.count("e")
total_e = e1 + e2
first_digit = total_t + total_r + total_u + total_e

l1 =name1_lower.count("l")
l2 = name2_lower.count("l")
total_l = l1 + l2
o1 =name1_lower.count("o")
o2 = name2_lower.count("o")
total_o = o1 + o2
v1 =name1_lower.count("v")
v2 = name2_lower.count("v")
total_v = v1 + v2
e1 =name1_lower.count("e")
e2 = name2_lower.count("e")
total_e = e1 + e2
second_digit = total_l + total_o + total_v + total_e

lovescore =(first_digit + second_digit )

if lovescore < 10 or lovescore > 90:
    print("your score is ",lovescore,"you go together like coke and mentos")
elif lovescore > 40 and lovescore < 50:
    print("your score is",lovescore,"you are alright together")
else:
    print("your score is",lovescore)