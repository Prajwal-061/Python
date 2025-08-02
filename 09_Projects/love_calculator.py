name_1 = input("enter your name")
name = name_1.lower()
name_2 = input("enter your partner name")
partner_name = name_2.lower()
combine_name = name + partner_name
lower_combine_name = combine_name.lower()
t = lower_combine_name.count("t")
r = lower_combine_name.count("r")
u = lower_combine_name.count("u")
e = lower_combine_name.count("e")
true = t + r + u + e

l = lower_combine_name.count("l")
o = lower_combine_name.count("o")
v = lower_combine_name.count("v")
e = lower_combine_name.count("e")
love = l + o + v + e

love_score = str(true) + str(love)
print("Your love score is "+love_score)
