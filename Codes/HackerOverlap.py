# This is the THIRD algorithm
exmp = ((4, 26), (15, 20), (22, 38), (49, 49), (49, 50), (49, 70), (62, 77), (78, 83), (92,94))
m = 100
flattened = set([val for sublist in exmp for val in sublist])
mn, mx = min(flattened), max(flattened)
# m=5
free_before = mn - 1
free_after = m - mx
continious = {}
merged = {}
first_tuple = exmp[0]
#continious[first_tuple] = [first_tuple]
# see which one totally or partially included
rem = exmp[1:]
iter_list = range(len(rem))
delete = []
new_list = []
final_list = []
while len(rem)>0:
    for tup in rem:

        # It is a must for sorted tuples list that tup[0]>=first_tuple[0]
        if tup[0] <= first_tuple[1]+1:
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
                    continious[first_tuple] =  [first_tuple]
                    continious[first_tuple].append(tup)
    #print(continious)
    fltd = set([val for sublist in continious[first_tuple] for val in sublist])
    merged[first_tuple] = (min(fltd), max(fltd))
    if first_tuple not in continious.keys():
        new_list.append(first_tuple)
    for tup in rem:
        if tup in continious[first_tuple]:
            if merged[first_tuple] not in new_list:
                new_list.append(merged[first_tuple])
        elif tup not in delete:
            new_list.append(tup)
    # print(new_list)
    if new_list[1][0]>=new_list[0][0] and new_list[1][0]<=new_list[0][1]+1:
        first_tuple = new_list[0]
        rem = new_list[1:]
    else:
        if len(rem)>2:
            first_tuple = new_list[1]
            rem = new_list[2:]
            final_list.append(new_list[0])
        else:
            for el in new_list:
                final_list.append(el)
            # print('**FINAL LIST**', final_list)
            print(final_list)
            break
    # if len(rem)==0:
    #     final_list.append(first_tuple)
    #     break
    # print('FINAL', final_list)
    # delete =[]
    new_list = []
else:
    final_list.append(first_tuple)
    # print('*FINAL LIST*', final_list)
    print(final_list)
