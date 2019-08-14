import os
import math

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

thresholds = {'Robot 80 1Q': 16, 'Robot 80 2Q': 32, 'Robot 80 3Q': 77, 'Robot 80 Mean': 45.59, 'Robot 80 Cl': 39,
              'Robot 100 1Q': 3, 'Robot 100 2Q': 10, 'Robot 100 3Q': 49, 'Robot 100 Mean': 25.73, 'Robot 100 Cl': 27,
              'Robot 120 1Q': 1, 'Robot 120 2Q': 2, 'Robot 120 3Q': 15, 'Robot 120 Mean': 8.38, 'Robot 120 Cl': 11,
              'Drone 80 1Q': 71, 'Drone 80 2Q': 78, 'Drone 80 3Q': 85, 'Drone 80 Mean': 77, 'Drone 80 Cl': 72,
              'Drone 100 1Q': 34, 'Drone 100 2Q': 42, 'Drone 100 3Q': 49, 'Drone 100 Mean': 41.72, 'Drone 100 Cl': 40,
              'Drone 120 1Q': 9, 'Drone 120 2Q': 13, 'Drone 120 3Q': 19, 'Drone 120 Mean': 14.12, 'Drone 120 Cl': 16,
              'Interaction 80 1Q': 66, 'Interaction 80 2Q': 73, 'Interaction 80 3Q': 80, 'Interaction 80 Mean': 70.83, 'Interaction 80 Cl': 60,
              'Interaction 100 1Q': 45, 'Interaction 100 2Q': 52, 'Interaction 100 3Q': 60, 'Interaction 100 Mean': 50.14, 'Interaction 100 Cl': 45,
              'Interaction 120 1Q': 18, 'Interaction 120 2Q': 24, 'Interaction 120 3Q': 30, 'Interaction 120 Mean': 23.19, 'Interaction 120 Cl': 23,
              }

total_passed = 0
total_failed = 0
type=["Robot", "Drone", "Interaction"]
index=["80", "100", "120"]
for i in range(0,3):
    for j in range(0,3):
        #logs = os.listdir("Drone fault 100")
        logs = os.listdir(type[i] + " fault " + index[j])
        file_count = 0
        #results = []
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
            #result, entities = read_log_SMC("Drone fault 100\\"+log)
            if log != "configuration.csv":
                result, entities = read_log_SMC(type[i] + " fault " + index[j] + "\\" + log)
                #results.append(result)
            #total_passed = total_passed + result # 용준이가 제안한 방법
            #total_failed = total_failed + 100 - result
            print(thresholds[type[i] + " " + index[j] + " 1Q"])
            if result <= thresholds[type[i] + " " + index[j] + " 1Q"]: # 나머지 기법들
                total_failed = total_failed + 1
            else:
                total_passed = total_passed + 1
            for entity in entities:
                #if entity == 'robot0,drone0' or entity == 'robot9,drone9':
                #    print(result)
                # 용준이가 제안한 방법 (논문에서는 1번 기법)
                #if entity in suspiciousness_dict:
                #    suspiciousness_dict[entity][0] = suspiciousness_dict[entity][0] + result
                #    suspiciousness_dict[entity][1] = suspiciousness_dict[entity][1] + 100 - result
                #else:
                #    suspiciousness_dict[entity] = [0, 0, 0]
                #    suspiciousness_dict[entity][0] = suspiciousness_dict[entity][0] + result
                #    suspiciousness_dict[entity][1] = suspiciousness_dict[entity][1] + 100 - result

                # 나머지 기법들 할때 result 값만 특정 값들, 1Q, 2Q, 3Q, Mean, Clustering 값, 입력해서 각각 실행
                if entity not in suspiciousness_dict:
                    suspiciousness_dict[entity] = [0, 0, 0]
                if result <= thresholds[type[i] + " " + index[j] + " 1Q"]: #Regarded as Failure
                    suspiciousness_dict[entity][1] = suspiciousness_dict[entity][1] + 1
                    total_failed = total_failed + 1
                else: #Regarded as Success
                    suspiciousness_dict[entity][0] = suspiciousness_dict[entity][0] + 1
                    total_passed = total_passed + 1

            file_count += 1
            if file_count % 100 == 0:
                print("passed: ", total_passed)
                print("failed: ", total_failed)
                # print(suspiciousness_dict)

                for key in suspiciousness_dict.keys():
                    passed = suspiciousness_dict[key][0] #Ncs
                    failed = suspiciousness_dict[key][1] #Ncf
                    suspiciousness_dict[key][2] = (failed / total_failed) / ((passed / total_passed) + (failed / total_failed)) #Tarantula
                    #suspiciousness_dict[key][2] = (failed * (total_passed - passed)) / math.sqrt((failed+passed) * (total_passed - passed + total_failed - failed) *total_failed* total_passed) #Ochiai2
                    #suspiciousness_dict[key][2] = pow(failed,2) / (total_failed-failed + passed) #Dstar with 2

                print(suspiciousness_dict)
                sort_suspiciousness_dict = {}
                for key in suspiciousness_dict.keys():
                    sort_suspiciousness_dict[key] = suspiciousness_dict[key][2]

                k = 0
                localized = 0
                path = "TARANTULA" + " " + "EXP" + " " + type[i] + " " + index[j]
                if not os.path.isdir(path):
                    os.mkdir(path)
                f = open(path + "\LocalizationResult" + str(file_count/100) + ".csv", 'w')
                for key in (reversed(sorted(sort_suspiciousness_dict, key=sort_suspiciousness_dict.__getitem__))):
                    print('index:', k, 'name:', key, 'suspiciousness:', sort_suspiciousness_dict[key])
                    list = str(key).split(",")

                    if len(list) == 2:
                        f.write(list[0] + "/" + list[1] + ", " + str(k) + ", " + str(sort_suspiciousness_dict[key]) +"\n")
                    else:
                        f.write(list[0] + ", " + str(k) + ", " + str(sort_suspiciousness_dict[key]) + "\n")
                    k = k + 1
                    list.clear()

                f.close()
                #print(suspiciousness_dict)
                total_passed = 0
                total_failed = 0
                suspiciousness_dict.clear()
        #f = open(type[i] + " " + index[j] + ".csv", 'w')
        #for num in results:
        #    f.write(str(num) + "\n")
        #f.close()
    # if k < 10 and int(key) < num_faulty:
    #     localized = localized + 1

# print("localized: ", localized, '/', num_faulty, ' (', (localized/num_faulty)*100, '%)', sep='')