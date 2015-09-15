PROBLEM = 'A-'
SMALL = 'small-practice-1'
LARGE = 'large-practice-2' 
IN = '.in'
OUT = '.out'
SIZE = SMALL

with open(PROBLEM + SIZE + IN, 'r') as f:
    with open(PROBLEM + SIZE + OUT, 'w') as o:
        number_of_cases = int(f.readline())
        current_case = 0
        while (current_case < number_of_cases):
            current_case = current_case + 1
            number_of_pairs = int(f.readline())
            pairs = []
            for i in range(number_of_pairs):
                pairs.append(f.readline().rstrip('\n').split(' '))
                #o.write('Case #{}: {}\n'.format(current_case, ''))
            print(pairs)
