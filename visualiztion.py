import matplotlib.pyplot as plt
from detect_alg import z_score_anomaly_detection
from help_func import log_anomaly, alert_anomaly


# Real-time visualization
def visualize_real_time(window_size=50, threshold=3):
    plt.ion()

    fig, ax = plt.subplots()
    x_data, y_data = [], []  # store the data stream
    anomaly_x, anomaly_y = [], []  # store anomalies

    line, = ax.plot(x_data, y_data, label='Data Stream')
    anomaly_points, = ax.plot(anomaly_x, anomaly_y, 'ro', label='Anomalies')  # Red dots for anomalies
    ax.legend()

    ax.set_xlabel("Time")
    ax.set_ylabel("Data Points")
    ax.set_title("Real-Time Data Stream and Anomalies")

    for idx, (data_point, is_anomaly) in enumerate(z_score_anomaly_detection(window_size, threshold)):
        x_data.append(idx)
        y_data.append(data_point)

        if is_anomaly:
            anomaly_x.append(idx)
            anomaly_y.append(data_point)

            # Call the log_anomaly and alert_anomaly functions from help_func.py
            log_anomaly(data_point)  # Log the anomaly to the file
            alert_anomaly(data_point)  # Trigger an alert (print, sound)

        # Update the plot
        line.set_xdata(x_data)
        line.set_ydata(y_data)
        anomaly_points.set_xdata(anomaly_x)
        anomaly_points.set_ydata(anomaly_y)

        ax.relim()
        ax.autoscale_view(True, True, True)

        plt.draw()
        plt.pause(0.01)  # Pause briefly to allow for updates

    plt.ioff()
    plt.show()


# Run the visualization
visualize_real_time(window_size=50, threshold=3)
