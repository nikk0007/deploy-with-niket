def outer_function():
    global num
    num = 20
 
    def inner_function():
        global num
        num = 30
        print('num =', num)
 
    inner_function()
    print('num =', num)
 
num = 10
outer_function()
print('num =', num)