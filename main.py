import LogGenerator
import os

num_log = 100
num_total_cs = 100
num_cs = 20
num_com = 40
num_faulty = 4

#LogGenerator.generate_logs(num_log, num_total_cs, num_cs, num_com, num_faulty)

# suspiciousness_dict = {}
# for i in range(num_total_cs):
#     suspiciousness_dict[str(i)] = [0, 0, 0]   # pass, fail, suspiciousness of an entity

suspiciousness_dict = {}
# for i in range(10):
#     suspiciousness_dict["robot"+str(i)] = [0, 0, 0]
# for i in range(10):
#     suspiciousness_dict["drone" + str(i)] = [0, 0, 0]

def read_log(log_file):
    f = open(log_file, 'r')
    lines = f.readlines()
    nodes = lines[0].split(',')
    for e in range(len(nodes)):
        nodes[e] = nodes[e].strip()

    edges = lines[1].split('),')
    for e in range(len(edges)):
        edges[e] = edges[e].strip()
        edges[e] = edges[e].strip('(')
        edges[e] = edges[e].strip(')')

    entities = nodes + edges
    result = float(lines[-1])
    status = True
    if result < 65:
        status = False

    # print(entities)
    return status, entities


def read_log_SMC(log_file):
    f = open(log_file, 'r')
    lines = f.readlines()
    nodes = lines[0].split(',')
    for e in range(len(nodes)):
        nodes[e] = nodes[e].strip()
    entities = nodes

    edges = lines[1].split('),')
    for e in range(len(edges)):
        edges[e] = edges[e].strip()
        edges[e] = edges[e].strip('(')
        edges[e] = edges[e].strip(')')
    entities = entities + edges

    result = float(lines[-1])

    # print(entities)
    return result//1, entities


total_passed = 0
total_failed = 0

logs = os.listdir("logs")
for log in logs:
    ## mode 1
    # status, entities = read_log("logs\\"+log)
    # if status:
    #     total_passed = total_passed + 1
    #     for entity in entities:
    #         if entity in suspiciousness_dict:
    #             suspiciousness_dict[entity][0] = suspiciousness_dict[entity][0] + 1
    #         else:
    #             suspiciousness_dict[entity] = [0, 0, 0]
    #             suspiciousness_dict[entity][0] = suspiciousness_dict[entity][0] + 1
    # else:
    #     total_failed = total_failed + 1
    #     for entity in entities:
    #         if entity in suspiciousness_dict:
    #             suspiciousness_dict[entity][1] = suspiciousness_dict[entity][1] + 1
    #         else:
    #             suspiciousness_dict[entity] = [0, 0, 0]
    #             suspiciousness_dict[entity][1] = suspiciousness_dict[entity][1] + 1

    # mode 2
    result, entities = read_log_SMC("logs\\"+log)
    for entity in entities:
        if entity in suspiciousness_dict:
            suspiciousness_dict[entity][0] = suspiciousness_dict[entity][0] + result
            suspiciousness_dict[entity][1] = suspiciousness_dict[entity][1] + 100 - result
            total_passed = total_passed + result
            total_failed = total_failed + 100 - result
        else:
            suspiciousness_dict[entity] = [0, 0, 0]
            suspiciousness_dict[entity][0] = suspiciousness_dict[entity][0] + result
            suspiciousness_dict[entity][1] = suspiciousness_dict[entity][1] + 100 - result
            total_passed = total_passed + result
            total_failed = total_failed + 100 - result

print("passed: ", total_passed)
print("failed: ", total_failed)
# print(suspiciousness_dict)
for key in suspiciousness_dict.keys():
    passed = suspiciousness_dict[key][0]
    failed = suspiciousness_dict[key][1]
    suspiciousness_dict[key][2] = (failed / total_failed) / ((passed / total_passed) + (failed / total_failed))

print(suspiciousness_dict)


sort_suspiciousness_dict = {}
for key in suspiciousness_dict.keys():
    sort_suspiciousness_dict[key] = suspiciousness_dict[key][2]

k = 0
localized = 0
for key in (reversed(sorted(sort_suspiciousness_dict, key=sort_suspiciousness_dict.__getitem__))):
    print('index:', k, 'name:', key, 'suspiciousness:', sort_suspiciousness_dict[key])
    k = k + 1
    # if k < 10 and int(key) < num_faulty:
    #     localized = localized + 1

# print("localized: ", localized, '/', num_faulty, ' (', (localized/num_faulty)*100, '%)', sep='')