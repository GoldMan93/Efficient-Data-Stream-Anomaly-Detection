import logging
import winsound  # For sound alert on Windows (use other libraries for Linux or MacOS)
import subprocess # For sound alert on MacOS and Linux

# Setup logging to file
logging.basicConfig(filename='anomaly_log.txt', level=logging.INFO,
                    format='%(asctime)s - Anomaly detected: %(message)s')


def log_anomaly(data_point):
    """Logs anomaly data points to a file."""
    logging.info(f'{data_point}')


def alert_anomaly(data_point):
    """Alerts the user when an anomaly is detected. This example plays a sound."""
    print(f"ALERT! Anomaly detected: {data_point}")
    # Optional: Play a beep sound
    # winsound.Beep(1000, 500)  # Windows
    # subprocess.run(["afplay", "/System/Library/Sounds/Glass.aiff"]) # MacOS
    # subprocess.run(["aplay", "/usr/share/sounds/alsa/Front_Center.wav"]) # Linux
