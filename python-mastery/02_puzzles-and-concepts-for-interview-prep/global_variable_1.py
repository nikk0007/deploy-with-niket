global_var = 10

def my_function():
    global global_var
    print("Inside my_function:", global_var)
    global_var = 20

print("Before calling my_function:", global_var)
my_function()
print("After calling my_function:", global_var)
