import numpy as np
from collections import deque
from data_gen import generate_data_stream


def z_score_anomaly_detection(window_size=50, threshold=3):
    """Detects anomalies in a data stream using the Z-score method."""
    data_window = deque(maxlen=window_size)  # Rolling window for data points

    for data_point in generate_data_stream(n_points=10000):  # Using the data gen from before
        data_window.append(data_point)

        if len(data_window) == window_size:
            mean = np.mean(data_window)
            std_dev = np.std(data_window)
            # Avoid division by zero
            if std_dev == 0:
                std_dev = 1

            # Calculate the Z-score
            z_score = (data_point - mean) / std_dev
            # Check if the Z-score exceeds the threshold
            if abs(z_score) > threshold:
                yield data_point, True  # Flag as anomaly
            else:
                yield data_point, False
        else:
            # If not enough points yet, assume no anomaly
            yield data_point, False


# Function usage example: Print out detected anomalies from the stream
for data_point, is_anomaly in z_score_anomaly_detection(window_size=50, threshold=3):
    if is_anomaly:
        print(f"Anomaly detected: {data_point}")
    else:
        print(f"Data point: {data_point}")
