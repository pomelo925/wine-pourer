import serial
import json
import time

def main():
    # Adjust the below line to match your serial port and baud rate
    ser = serial.Serial('/dev/ttyACM0', 9600)
    time.sleep(2)  # give the connection a second to settle

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            try:
                data = json.loads(line)  # parse JSON
                weight = data.get('weight', None)
                count = data.get('count', None)
                print(f'Weight: {weight}, Count: {count}')
            except json.JSONDecodeError as e:
                print(f'Error: {e}')

if __name__ == "__main__":
    main()
