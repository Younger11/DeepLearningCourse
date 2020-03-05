import math
a=int(input("请输入a的值"))
b=int(input("请输入b的值"))
c=int(input("请输入c的值"))
if b*b-4*a*c>0:
    print("有两个实数解，分别为:")
    x = (-b-math.pow(b*b-4*a*c,0.5))/(2.0*a)
    y = (-b+math.pow(b*b-4*a*c,0.5))/(2.0*a)
    print("%f,%f"%(x,y))
elif b*b-4*a*c==0:
    print("有一个实数解:")
    x = (-b-math.pow(b*b-4*a*c,0.5))/(2.0*a)
    print("%f"%(x))
else:
    print("没有实数解")