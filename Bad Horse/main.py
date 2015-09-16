#from https://code.google.com/codejam/contest/6234486/dashboard

PROBLEM = 'A-'
SMALL = 'small-practice-1'
LARGE = 'small-practice-2' 
IN = '.in'
OUT = '.out'
SIZE = SMALL

def can_split(graph):
    group_a = set()
    group_b = set()
    inserted = set()
    members = set(graph.keys())
    while not inserted == members:
        for member in graph:
            if len(group_a) == 0:
                group_a.add(member)
                inserted.add(member)
            if member in group_a:
                inserted.add(member)
                group_b.update(graph[member])
            if member in group_b:
                inserted.add(member)
                group_a.update(graph[member])
    return 'Yes' if group_a.isdisjoint(group_b) else 'No'
                            
with open(PROBLEM + SIZE + IN, 'r') as f:
    with open(PROBLEM + SIZE + OUT, 'w') as o:
        number_of_cases = int(f.readline())
        current_case = 0
        while (current_case < number_of_cases):
            current_case = current_case + 1
            number_of_pairs = int(f.readline())
            if number_of_pairs == 1:
                f.readline()
                o.write('Case #{}: {}\n'.format(current_case, 'Yes'))
            else:
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
                o.write('Case #{}: {}\n'.format(current_case, can_split(graph)))
