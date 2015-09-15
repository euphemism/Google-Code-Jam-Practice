with open('A-large-practice.in', 'r') as f:
    with open('A-large-practice.out', 'w') as o:
        number_of_cases = int(f.readline())
        current_case = 0
        while (current_case < number_of_cases):
            current_case = current_case + 1
            credit = int(f.readline())
            number_of_items = int(f.readline())
            items = [int(i) for i in f.readline().split()]
            upper_index = -1
            for i, item_1 in enumerate(items):
                lower_index = i + 1
                for j, item_2 in enumerate(items):
                    if i == j:
                        continue
                    if item_1 + item_2 == credit:
                        upper_index = j + 1
                        break
                if not upper_index == -1:
                    break
                    
                    
            o.write('Case #{}: {} {}\n'.format(current_case, lower_index, upper_index))
