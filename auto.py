def autobypy():
    import pywhatkit as user
    num=input("Enter Reciver number With Counrty code with +:")
    if len(num)>13:
        print('------------------------------')
        print("Enter A Valid Number")
        print('------------------------------')
    else:
        msg=input("Enter your msg:")
       # print()
        t_hr=int(input("Enter time in hours:"))
        if t_hr>24:
            print('------------------------------')
            print("Enter Correct Time")
            print('------------------------------')
           # print()
        else:
            t_min=int(input("Enter time in min:"))
            if t_min>60:
                print('------------------------------')
                print("Enter Valid mins")
                print('------------------------------')
            else:
                user.sendwhatmsg(num,msg,t_hr,t_min)
autobypy()
print()
print("Made by Rajesh Korlapati")
