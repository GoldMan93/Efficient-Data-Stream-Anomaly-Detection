import numpy as np
import random
import time


def generate_data_stream(n_points=10000, anomaly_prob=0.01):
    trend = 0
    seasonal_amplitude = 10
    noise_level = 2

    for i in range(n_points):
        trend += 0.01
        seasonal = seasonal_amplitude * np.sin(2 * np.pi * (i % 100) / 100)
        noise = noise_level * np.random.randn()
        point = trend + seasonal + noise

        # Randomly introduce anomalies
        if random.random() < anomaly_prob:
            point += random.choice([-50, 50])

        yield point

        # Simulate real-time data by adding a slight delay
        # time.sleep(0.01)


# Function usage example: Generate 1000 data points and print them
stream = generate_data_stream(n_points=1000)
for point in stream:
    print(point)
