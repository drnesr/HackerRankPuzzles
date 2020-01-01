def stations(commuters):
    m = len(commuters)
    station_info = {}
    # Calculating waiting time for all stations
    for com in commuters:
        # adding a list of [Num of coms, minimum arival, max arrival]
        if com[1] in station_info:
            target = station_info[com[1]]
            target[0] +=1
            target[1] =min(target[1], com[0])
            target[2] =max(target[2], com[0])
        else:
            station_info[com[1]] = [1, com[0], com[0]]
    return station_info

# commuters = [[1, 1, 3], [2, 1, 2], [5, 2, 3]]
# n, m, k = 3,3,2
# d=[1,4]
# sts= stations(commuters)
# print (sts)
# times = []
#
# for each in commuters:
#     prop = k
#     waiting=0
#     init_time=each[0]
#     elapsed_time=0
#     for sta in range(each[1], each[2]):
#         print(sta, end=', ')
#         max_wait = sts[sta][2]
#         # waiting = max_wait-elapsed_time-init_time
#         # if elapsed_time>0:
#         #     waiting-=init_time
#         distance= d[sta-1]
#         max_speeding = max(0, min(prop, distance))
#         prop_scenario=prop
#         elapsed_scenario=[]
#         prop_scenarios=[]
#         for scenario in range(max_speeding+1):
#             prop_scenario = prop-scenario
#             prop_scenarios.append(prop_scenario)
#             waiting = max_wait - elapsed_time - init_time
#             reduced_distance=max(0,(prop-prop_scenario))
#             elapsed_scenario.append(waiting+distance-reduced_distance)
#         print(scenario, elapsed_scenario, end=', ')
#         for i, elp_tim in enumerate(elapsed_scenario):
#             for sta2 in range(sta+1, each[2]):
#                 max_wait2 = sts[sta2][2]
#                 distance2 = d[sta2 - 1]
#                 max_speeding2 = max(0, min(prop, distance2))
#                 prop_scenario2 = prop_scenarios[i]
#                 elapsed_scenario2 = []
#                 for scenario2 in range(max_speeding2 + 1):
#                     prop_scenario2 = prop_scenarios[i] - scenario2
#                     waiting2 = max_wait2 - elp_tim - init_time
#                     reduced_distance2 = max(0, (prop_scenarios[i] - prop_scenario2))
#                     elapsed_scenario2.append(waiting2 + distance2 - reduced_distance2)
#                 print(i, sta2, elapsed_scenario2, end='; ')

        # prop-=speeded
        # elapsed_time+=waiting+distance-speeded
        # print(each, sta, elapsed_scenario, elapsed_scenario2)
    # print(elapsed_time)



    # distance = sum(d[each[1]-1: each[2]])
    # speeded = max(0, distance-k)
    # com_time=waiting+speeded
    # times.append(com_time)
# print(times)
def kangaroo(x1, v1, x2, v2):
    steps = 0
    pos1 = x1
    pos2 = x2
    x1_first = x1 < x2
    while steps < 10000:
        if pos1 == pos2:
            return 'YES'
        steps += 1
        pos1 += v1
        pos2 += v2
        if (x1_first and pos1 > pos2) or (not (x1_first) and pos2 > pos1):
            return 'NO'
            break
    else:
        return 'NO'

print(kangaroo(0, 3, 4, 2))
