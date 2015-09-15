with open('B-large-practice.in', 'r') as f:
    with open('B-large-practice.out', 'w') as o:
        number_of_cases = int(f.readline())
        current_case = 0
        while (current_case < number_of_cases):
            current_case = current_case + 1
            o.write('Case #{}: {}\n'.format(current_case, ' '.join([x for x in f.readline().split()][::-1])))
