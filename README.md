# Efficient Data Stream Anomaly Detection

This project is a real-time anomaly detection system implemented in Python. It uses the Z-score method to detect anomalies in a simulated data stream and provides real-time visualization of the data and flagged anomalies. Additionally, the system logs anomalies and can trigger alerts when they occur.

## Project Structure

- **data_gen.py**: This module generates a continuous data stream, simulating real-world patterns like trends, seasonal elements, and random noise, with occasional anomalies introduced.
- **detect_alg.py**: Contains the anomaly detection algorithm based on the Z-score method. It processes the data stream and flags anomalies based on a defined threshold.
- **help_func.py**: Provides utility functions to log anomalies to a file and trigger alerts (e.g., console output or sounds depending on the system).
- **visualization.py**: Visualizes the data stream in real-time using Matplotlib. Detected anomalies are plotted in red, and both logging and alert functions are triggered when anomalies are found.

## Requirements

### Python Version:

- Python 3.x

### Dependencies:

Install the required libraries using pip:

```bash
pip install numpy matplotlib
```

For sound alerts:

- **Windows**: The winsound library is used (included by default).
- **macOS**: Uses the afplay command for sound.
- **Linux**: Uses the aplay command from the ALSA sound library.

Make sure to install alsa-utils if it's not already installed on Linux:

```bash
sudo apt-get install alsa-utils
```

## Usage

### 1. Data Generation

data_gen.py generates the data stream. The generate_data_stream() function creates a stream of data points with a small probability of anomalies. You can adjust the number of points and the anomaly probability by modifying the function parameters.

### 2. Anomaly Detection

detect_alg.py contains the Z-score anomaly detection logic. The Z-score method is applied to a rolling window of data points. If a point's Z-score exceeds the given threshold, it is flagged as an anomaly.

### 3. Logging and Alerts

help_func.py provides the log_anomaly() and alert_anomaly() functions. Each time an anomaly is detected, the following actions occur:

- **Logging**: The anomaly is logged to anomaly_log.txt.
- **Alerts**: An alert is printed to the console. On some systems, a sound alert can also be triggered.

### 4. Real-Time Visualization

visualization.py visualizes the data stream in real-time. Detected anomalies are marked in red, and the plot updates dynamically as new data points arrive.

#### Example Output:

The real-time plot will display two lines:

- **Blue line**: Represents the real-time data stream.
- **Red dots**: Represent anomalies detected by the system.
  Simultaneously, the system will log anomalies in the anomaly_log.txt file and trigger alerts.

## Customization

You can adjust the parameters of the anomaly detection and data generation functions:

- **Window Size**: Adjust the size of the rolling window for anomaly detection.
- **Threshold**: Modify the Z-score threshold to control the sensitivity of anomaly detection.
- **Anomaly Probability**: Change the probability of anomalies in the data stream by modifying the anomaly_prob parameter in generate_data_stream().

## Platform-Specific Sound Alerts

- **Windows**: Sound alerts are played using the winsound.Beep() method.
- **macOS**: Use the afplay command to play a sound.
- **Linux**: Use the aplay command for sound alerts.
  To activate the sound alerts, uncomment the relevant section in the alert_anomaly() function in help_func.py.

## Future Improvements

- Implement more sophisticated anomaly detection algorithms.
- Allow users to configure alerting mechanisms (e.g., email or SMS alerts).
- Enhance visualization with interactive controls to adjust the detection threshold in real-time.

## License

This project is licensed under the MIT License.
