import os
import csv
#import pandas as pd

#key = ('robot0/drone0', 'robot9/drone9') #오류가 삽입된 Interactions id
key =('robot1', 'robot4') # 오류가 삽입된 Robots or Drones id
#key=('drone1', 'drone5')

type = ["Robot", "Drone", "Interaction"]
index = ["80", "100", "120"]
ums = ["EXP", "1Q", "2Q", "3Q", "Mean", "Cluster"]
algs = ["TARANTULA", "D2", "Och2"]

keys = {'Robot 80': ('robot2', 'robot6'), 'Robot 100': ('robot1', 'robot4'), 'Robot 120': ('robot4', 'robot9'),
        'Drone 80': ('drone1', 'drone4'), 'Drone 100': ('drone1', 'drone5'), 'Drone 120': ('drone2', 'drone8'),
        'Interaction 80': ('robot1/drone1', 'robot5/drone5'), 'Interaction 100': ('robot0/drone0', 'robot9/drone9'),
        'Interaction 120': ('robot3/drone3', 'robot6/drone6')}

for alg in algs:
    for um in ums:
        for tp in type:
            print(tp)
            faulty = []
            normal = []
            faulty.append(("Faulty Ranking", "Faulty Suspiciousness"))
            normal.append(("Normal Ranking", "Normal Suspiciousness"))
            for id in index:
                print(id)
                key = keys[tp + " " + id]
                print(key)
                path = alg + " " + um + " " + tp + " " + id
                logs = os.listdir(path)
                #faulty.append((path, str(-1)))
                #normal.append((path, str(-1)))
                for log in logs:
                    if log == "configuration.csv":
                        continue
                    f = open(path+"\\" + log, 'r')
                    reader = csv.reader(f)
                    results = list(reader)

                    for result in results:
                        if result[0] == key[0] or result[0] == key[1]:
                            faulty.append((result[1], result[2]))
                        else:
                            normal.append((result[1], result[2]))
                #results.clear()

            f = open(alg + " " + um + " " + tp +".csv", 'w')
            for i in range(len(normal)):
                if i < len(faulty):
                    f.write(faulty[i][0] + "," + faulty[i][1] + "," + normal[i][0] + "," + normal[i][1]+"\n")
                else:
                    f.write(", ," + normal[i][0] + "," + normal[i][1]+"\n")
'''
#ls = ["80", "100", "120"]
fw = open("Robot SMC Result 100.csv", 'w')
#for i in range(0,3):
logs = os.listdir("Robot fault 100")
for log in logs:
    if log == "configuration.csv":
        continue
    f = open("Robot fault 100\\" + log, 'r')
    reader = csv.reader(f)
    results = list(reader)
    fw.write(results[2][0] + "\n")'''