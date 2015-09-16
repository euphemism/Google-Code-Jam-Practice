PROBLEM = 'A-'
SMALL = 'small-practice-1'
LARGE = 'large-practice-2' 
IN = '.in'
OUT = '.out'
SIZE = SMALL

def test_member(member, graph, group_a, group_b):

    group_a_intersect = [memb for memb in graph[member] if memb in group_a]
    group_b_intersect = [memb for memb in graph[member] if memb in group_b]
    a_intersect_length = len(group_a_intersect)
    b_intersect_length = len(group_b_intersect)
    if a_intersect_length == 0:
        group_a.append(member)
    else:
        if b_intersect_length == 0:
            group_b.append(member)
        else:
            print('No')
    print('Yes')

def can_split(graph):
    group_a = []
    group_b = []
    for member in graph:
        group_a_intersect = [memb for memb in graph[member] if memb in group_a]
        group_b_intersect = [memb for memb in graph[member] if memb in group_b]
        a_intersect_length = len(group_a_intersect)
        b_intersect_length = len(group_b_intersect)
        if a_intersect_length == 0:
            group_a.append(member)
        else:
            if b_intersect_length == 0:
                group_b.append(member)
            else:
                for memb in group_b_intersect:
                    group_b.remove(memb)
                    test_member(memb, graph, group_a, group_b)
                
                    
                print('No', graph, group_a, group_b)
                return 'No'
    print('Yes', graph, group_a, group_b)
    return 'Yes'

with open(PROBLEM + SIZE + IN, 'r') as f:
    with open(PROBLEM + SIZE + OUT, 'w') as o:
        number_of_cases = int(f.readline())
        current_case = 0
        while (current_case < number_of_cases):
            current_case = current_case + 1
            number_of_pairs = int(f.readline())
            if number_of_pairs == 1:
                print('Case #{}: {}\n'.format(current_case, 'Yes'))       
            graph = {}
            for i in range(number_of_pairs):
                a, b = f.readline().rstrip('\n').split(' ')
                if not a in graph:
                    graph[a] = [b]
                else:
                    graph[a].append(b)
                if not b in graph:
                    graph[b] = [a]
                else:
                    graph[b].append(a)
            result = can_split(graph)
            print('Case #{}: {}\n'.format(current_case, result))
            o.write('Case #{}: {}\n'.format(current_case, result))
