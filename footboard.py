import RPi.GPIO as GPIO
import time

# Initialize GPIO pins
LOCK_PIN = 17  # Example GPIO pin for locking mechanism
SENSOR_PIN = 18  # Example GPIO pin for sensor

GPIO.setmode(GPIO.BCM)
GPIO.setup(LOCK_PIN, GPIO.OUT)
GPIO.setup(SENSOR_PIN, GPIO.IN)

# Function to lock the footboard drive engine
def lock_engine():
    GPIO.output(LOCK_PIN, GPIO.HIGH)
    print("Engine locked")

# Function to unlock the footboard drive engine
def unlock_engine():
    GPIO.output(LOCK_PIN, GPIO.LOW)
    print("Engine unlocked")

# Main function to monitor sensor and lock/unlock engine accordingly
def main():
    while True:
        if GPIO.input(SENSOR_PIN) == GPIO.HIGH:
            lock_engine()
        else:
            unlock_engine()
        time.sleep(0.5)  # Check sensor every 0.5 seconds

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
