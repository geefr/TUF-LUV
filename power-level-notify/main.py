import subprocess
import time


def print_mode(mode):
    mode_str = None
    if mode == '2':
        mode_str = 'Silent'
    elif mode == '0':
        mode_str = 'Balanced'
    elif mode == '1':
        mode_str = 'Turbo'

    if mode_str:
        subprocess.run(["notify-send", "-u", "low", f"Power Mode: {mode_str}"])

if __name__ == '__main__':
    power_mode = None

    while True:
        try:
            with open("/sys/devices/platform/asus-nb-wmi/throttle_thermal_policy", 'r') as f:
                new_power_mode = f.read(1)
            if new_power_mode != power_mode:
                print_mode(new_power_mode)
                power_mode = new_power_mode
            time.sleep(1)
        except FileNotFoundError:
            subprocess.run(["notify-send", "Error: thermal_policy not found. Is this a supported laptop?"])

