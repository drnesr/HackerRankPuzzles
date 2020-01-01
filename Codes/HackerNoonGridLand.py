import math
import os
import random
import re
import sys
import pandas as pd

# Complete the gridlandMetro function below.
def gridlandMetro(n, m, k, track):
    def reduce_pairs_in_a_row(exmp):
        continious = {}
        merged = {}
        first_tuple = exmp[0]
        # see which one totally or partially included
        rem = exmp[1:]
        iter_list = range(len(rem))
        delete = []
        new_list = []
        final_list = []
        while len(rem) > 0:
            for tup in rem:
                # It is a must for sorted tuples list that tup[0]>=first_tuple[0]
                if tup[0] <= first_tuple[1] + 1:
                    # the first element is included, see the second
                    if tup[1] <= first_tuple[1]:
                        # the second element is also included (complete overlap)
                        delete.append(tup)
                    else:
                        # the end bound of the current tuple should be the end of the
                        #       first one.
                        if first_tuple in continious:
                            continious[first_tuple].append(tup)
                        else:
                            continious[first_tuple] = [first_tuple]
                            continious[first_tuple].append(tup)
            # print(continious)
            if first_tuple in continious.keys():
                fltd = set([val for sublist in continious[first_tuple] for val in sublist])
                merged[first_tuple] = (min(fltd), max(fltd))
            else:
                new_list.append(first_tuple)
            for tup in rem:
                if first_tuple in continious.keys():
                    if tup in continious[first_tuple]:
                        if merged[first_tuple] not in new_list:
                            new_list.append(merged[first_tuple])
                if tup not in delete:
                    new_list.append(tup)
            # print(new_list)
            if len(new_list) > 1:
                if new_list[1][0] >= new_list[0][0] and new_list[1][0] <= new_list[0][1] + 1:
                    first_tuple = new_list[0]
                    rem = new_list[1:]
                else:
                    if len(rem) > 2:
                        first_tuple = new_list[1]
                        rem = new_list[2:]
                        final_list.append(new_list[0])
                    else:
                        for el in new_list:
                            final_list.append(el)
                        # print('**FINAL LIST**', final_list)
                        # print(final_list)
                        break
                new_list = []
            else:
                final_list.append(new_list[0])
                break
        else:
            final_list.append(first_tuple)
            # print(final_list)
        return final_list

    def merge(times):

        '''https: // stackoverflow.com / a / 5679899 / 5820024'''

        saved = list(times[0])
        for st, en in sorted([sorted(t) for t in times]):
            if st <= saved[1] + 1:
                saved[1] = max(saved[1], en)
            else:
                yield tuple(saved)
                saved[0] = st
                saved[1] = en
        yield tuple(saved)

    def get_occupied_slots_in_a_row(m, exmp):
        # flattened = set([val for sublist in exmp for val in sublist])
        # mn, mx = min(flattened), max(flattened)
        # # m=5
        # free_before = mn - 1
        # free_after = m - mx
        # may_be_occupied = mx - mn + 1
        reduced_pairs = merge(exmp)
        occupied_paths = [en - st + 1 for (st, en) in reduced_pairs]
        really_occupied = sum(occupied_paths)
        # free_inside = may_be_occupied - really_occupied
        # total_free = free_before + free_inside + free_after
        # return total_free
        return really_occupied

    lanes = {}
    lanes_len = {}

    for trk in track:
        row, strt, end = trk
        if row in lanes:
            lanes[row].append((strt, end))
        else:
            lanes[row] = [(strt, end)]
    lanes_keys = sorted(list(lanes.keys()))
    for lane in lanes_keys:
        # if lane==43581696:
        #     print('Now')
        # print(lane)

        if len(lanes[lane]) > 1:
            lanes[lane] = sorted(lanes[lane], key=lambda tup: (tup[0], tup[1]))
            lanes_len[lane] = get_occupied_slots_in_a_row(m, lanes[lane])
        else:
            dist_s, dist_e = lanes[lane][0]
            lanes_len[lane] = dist_e - dist_s + 1

    occupied = sum(list(lanes_len.values()))
    free_len = m * n - occupied
    return free_len

# Trial 1
# fil = pd.read_csv('../Data/HackerData.txt', sep=' ', dtype=int)
# track6= fil.values.tolist()
# n, m, k =list(map(int, list(fil)))

#Trial 2
n,m, k=1, 5, 3
trials=((1,1,2), (1,2,4), (1,3,5))
print(gridlandMetro(n, m, k, trials))