#From https://code.google.com/codejam/contest/4284486/dashboard

import math

def switch(string):
    return ''.join([str(int(c) ^ True) for c in string])
    
def reverse(string):
    return string[::-1]

def generate(size, string):
    if size == 0:
        return string
    return generate(size - 1, string + '0' + switch(reverse(string)))

s = '001001100011011000100111001101100010011000110111001001110011011000' + \
    '1001100011011000100111001101110010011000110111001001110011011' # = generate(7, '')

def calculate_value(k):
    inverse = True
    prev_k = -1
    while (not k == prev_k):
        nearest_power = math.floor(math.log(k, 2))
        two_to_the_np = 2 ** nearest_power
        if k == two_to_the_np and prev_k == -1:
            return 0
        inverse = not inverse
        prev_k = k
        k = two_to_the_np - (k - two_to_the_np)
    return int(s[k - 1]) ^ inverse

with open('A-small-practice.in', 'r') as f:
    with open('A-small-practice.out', 'w') as o:
        number_of_cases = int(f.readline())
        current_case = 0
        while current_case < number_of_cases:
            current_case = current_case + 1
            o.write('Case #{}: {}\n'.format(current_case, calculate_value(int(f.readline()))))
