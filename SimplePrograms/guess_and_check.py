# not handling lots of cases.
ans = 0
neg_flag = False
x = int(input("Enter an integer: "))

if x < 0:
    neg_flag = True

while ans**2 < x:
    ans += 1

if ans**2 == x:
    print("Square root of", x ,"is", ans)

else:
    print(x, "is not a perfect square")
    if neg_flag:
        print("Just checking... id you mean", -x, "?")
