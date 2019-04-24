import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random


def check_speed(time_gap, speed_gap, total_time, min_speed, max_speed):
    times = (int)(total_time / time_gap)

    data_array = np.empty(times)
    weights_array = np.empty(times)
    weights_array.fill(1/times)

    for i in range(0, times):
        if speed_gap < 1:
            data_array[i] = random.random() * max_speed
        else:
            data_array[i] = random.randint(0, max_speed / speed_gap) * speed_gap

    data_frame = pd.DataFrame(data_array)
    bin_range = np.arange(0, 200, speed_gap)
    data_frame.plot(kind='hist', bins=bin_range, legend=False, weights=weights_array)
    plt.show()


check_speed(0.1,1,60, 0, 200)