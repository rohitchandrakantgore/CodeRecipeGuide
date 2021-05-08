import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)


#output

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 5
# ABCDE
# FGHIJ
# KLIMN
# OQRST
# UVWXY
# Z