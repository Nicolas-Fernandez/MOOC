var = [1, 2]
def f():
    global var
    var.append(10)
f()

print var
