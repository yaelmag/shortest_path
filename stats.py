'''
This file should be runnable to print map_statistics using 
$ python stats.py
'''

from collections import namedtuple
from ways import load_map_from_csv
from collections import Counter


def map_statistics(roads):
    '''return a dictionary containing the desired information
    You can edit this function as you wish'''
    Stat = namedtuple('Stat', ['max', 'min', 'avg'])
    minb, maxb = minmax_out_branching(roads)
    minl, maxl = minmax_link_distance(links_lst(roads))
    return {
        'Number of junctions' : len(roads.junctions()),
        'Number of links' : len(links_lst(roads)),
        'Outgoing branching factor' : Stat(max=maxb, min=minb, avg=avg_out_branching(roads)),
        'Link distance' : Stat(max=maxl, min=minl, avg=avg_link_distance(links_lst(roads))),
        # value should be a dictionary
        # mapping each road_info.TYPE to the no' of links of this type
        'Link type histogram' : make_histogram(links_lst(roads)),  # tip: use collections.Counter
    }


def print_stats():
    for k, v in map_statistics(load_map_from_csv()).items():
        print('{}: {}'.format(k, v))


def minmax_out_branching(roads):
    min_ = len(roads.junctions().__getitem__(0).links)
    max_ = len(roads.junctions().__getitem__(0).links)

    for j in roads.junctions():
        if len(j.links) < min_:
            min_ = len(j.links)
        elif len(j.links) > max_:
            max_ = len(j.links)

    return min_, max_


def avg_out_branching(roads):
    return sum(len(j.links) for j in roads.junctions())/len(roads.junctions())


def links_lst(roads):
    return [l for j in roads.junctions() for l in j.links]


def minmax_link_distance(links):
    min_ = links[0].distance
    max_ = links[0].distance

    for i in range(len(links)):
        if links[i].distance < min_:
            min_ = links[i].distance
        elif links[i].distance > max_:
            max_ = links[i].distance

    return min_, max_


def avg_link_distance(links):
    return sum(link.distance for link in links) / len(links)


def make_histogram(links):
    cnt = Counter()
    for link in links:
        cnt[link.highway_type] +=1
    return dict(cnt)


if __name__ == '__main__':
    from sys import argv
    assert len(argv) == 1
    print_stats()