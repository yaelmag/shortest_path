'''
Parse input and run appropriate code.
Don't use this file for the actual work; only minimal code should be here.
We just parse input and call methods from other modules.
'''

# do NOT import ways. This should be done from other files
# simply import your modules and call the appropriate functions
import algorithms


def find_ucs_rout(source, target):
    'call function to find path, and return list of indices'
    return algorithms.find_ucs_route(source, target)


def find_astar_route(source, target):
    'call function to find path, and return list of indices'
    return algorithms.find_astar_route(source, target)


def find_idastar_route(source, target):
    'call function to find path, and return list of indices'
    return algorithms.find_idastar_route(source, target)

def dispatch(argv):
    from sys import argv
    source, target = int(argv[2]), int(argv[3])
    if argv[1] == 'ucs':
        path = find_ucs_rout(source, target)
    elif argv[1] == 'astar':
        path = find_astar_route(source, target)
    elif argv[1] == 'idastar':
        path = find_idastar_route(source, target)
    print(' '.join(str(j) for j in path))


if __name__ == '__main__':
    from sys import argv
    dispatch(argv)


    '''
    f = open("problems.csv", "w+")
    for j in range(100):
        source = random.randint(0, 944800)
        junction = g.get_junction(source)
        length = random.randint(1, 20)
        for i in range(length):
            if (len(junction.links) > 0 ):
                l = random.randint(0, len(junction.links))
                nj = junction.links[l-1].target
                junction = g.get_junction(nj)
            elif(i>0):
                break
            else:
                continue

        f.write(str(source) + ", " + str(junction.index) + "\n")

    f.close()
    '''
    '''
    בפונקציה במיין
    fr = open("problems.csv", "r")
    fw = open("UCSRuns.txt", "w+")
    g = graph.load_map_from_csv()
    for i in range(100):
        sen = fr.readline()
        l = sen.split(", ")
        s = int(l[0])
        t = int(l[1])
        print(s, t)
        r = algorithms.find_ucs_rou(s, t, g)
        fw.write(str(r) + "\n")
        return {'bb': 11}
        
        במקום החזרת הסולושיין
            print(node.solution())
            return node.path_cost
    '''