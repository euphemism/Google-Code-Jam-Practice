import math

def switch(string):
    return ''.join([str(int(c) ^ True) for c in string])
    
def reverse(string):
    return string[::-1]

def generate(size, string):
    if size == 0:
        return string
    return generate(size - 1, string + '0' + switch(reverse(string)))

def calculate_value(k):
    inverse = False
    prev_k = -1
    while (not k == prev_k):
        inverse = not inverse
        nearest_power = (math.floor(math.log(k, 2)))
        if ((k == (2 ** nearest_power)) and (prev_k == -1)):
            k = -1
            break
        prev_k = k
        two_to_the_np = 2 ** nearest_power
        k = two_to_the_np - (k - two_to_the_np)
    return (k, inverse)
    
s = generate(20, '')
ls = [1, 2, 3, 10]

for i in ls:
    k, inverse = calculate_value(i)
    if (k == -1):
        print(0)
    else:
        print(int(s[k]) ^ inverse)

print(generate(10, ''))
