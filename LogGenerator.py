import random
import numpy as np


def generate_logs(num_log, num_total_cs, num_cs, num_com, num_faulty):
    CS = [i for i in range(num_total_cs)]

    for f_num in range(num_log):
        f_name = 'logs\\log'+str(f_num)+'.csv'
        f = open(f_name, 'w')

        chosen_CS = random.sample(CS, num_cs)

        for i in range(len(chosen_CS)):
            f.write(str(chosen_CS[i]))
            if i < len(chosen_CS)-1:
                f.write(", ")
            else:
                f.write("\n")

        communication_pool = []
        for i in range(len(chosen_CS)):
            for j in range(1, len(chosen_CS)):
                communication_pool.append((chosen_CS[i], chosen_CS[j]))

        chosen_communication = random.sample(communication_pool, num_com)

        for i in range(len(chosen_communication)):
            f.write(str(chosen_communication[i]))
            if i < len(chosen_communication)-1:
                f.write(", ")
            else:
                f.write("\n")

        goal = 0
        for cs in chosen_CS:
            # goal = goal + np.random.normal(5, 2)
            if cs < num_faulty:
                goal = goal + np.random.normal(0, 1)
            else:
                goal = goal + np.random.normal(5, 1)

        f.write(str(goal))

        f.close()
