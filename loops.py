i = 10
num = int(input("Num: "))
while i>0:
    print(i)
    i -=1

    if i == num:
        print("Break")
        break #перывает while
else:
    print("Else")


print(--------------)

try:
    1/0 #(исключение, условие)
except ZeroDivisionError: #название ичключения,
                          # можно несколько в ()
    print("Exception")
else:
    print("Try else") #если вообще нет ошибок
finally:


# ключем в дикте могут быть только неизменяемые

# new line