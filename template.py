PROBLEM = 'C-'
SMALL = 'small-practice'
LARGE = 'large-practice' 
IN = '.in'
OUT = '.out'
SIZE = SMALL

with open(PROBLEM + SIZE + IN, 'r') as f:
    with open(PROBLEM + SIZE + OUT, 'w') as o:
        number_of_cases = int(f.readline())
        current_case = 0
        while (current_case < number_of_cases):
            current_case = current_case + 1
            o.write('Case #{}: {}\n'.format(current_case, ''))
            
