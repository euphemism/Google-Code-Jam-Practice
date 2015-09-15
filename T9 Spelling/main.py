import sys

PROBLEM = 'C-'
SMALL = 'small-practice'
LARGE = 'large-practice' 
IN = '.in'
OUT = '.out'
SIZE = SMALL

MAP = {' ': 0, 'abc': 2, 'def': 3, 'ghi': 4, 'jkl': 5, 'mno': 6, 'pqrs': 7, 'tuv': 8, 'wxyz': 9}

def convert(output, pos, line):
    if pos == 0:
        return output
    char = line[pos - 1:pos]
    result = ''
    for key in MAP:
        index = key.find(char)
        if not index == -1:
            if str(MAP[key]) == output[:1]:
                result = ' '
            return convert(''.join([str(MAP[key]) for x in range(index + 1)]) \
                           + result + output, pos - 1, line)
    return

def convert(line):
    length = len(line)
    result = ''
    while length >= 0:
        char = line[length - 1:length]
        for key in MAP:
            index = key.find(char)
            if not index == -1:
                if str(MAP[key]) == result[:1]:
                    result = ' ' + result
                result = ''.join([str(MAP[key]) for x in range(index + 1)]) \
                         + result
                length = length - 1
    return result

with open(PROBLEM + SIZE + IN, 'r') as f:
    with open(PROBLEM + SIZE + OUT, 'w') as o:
        number_of_cases = int(f.readline())
        current_case = 0
        while (current_case < number_of_cases):
            current_case = current_case + 1
            line = f.readline().rstrip('\n')
            print('Case #{}: {}\n'.format(current_case, convert(line)))
            #print('Case #{}: {}\n'.format(current_case, convert('', len(line), line)))
            o.write('Case #{}: {}\n'.format(current_case, convert(line)))
            
