import time
import asyncio
import curses
from bleak import BleakScanner

def display_hacker_ui(stdscr):
    """Display a hacker-style UI with options before showing the banner."""
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()  # Clear the screen
    stdscr.refresh()
    
    # Create a simple animation to simulate the 'hacker' feel
    stdscr.addstr(0, 0, "Initializing system...\n", curses.A_BOLD)
    stdscr.addstr(1, 0, "---------------------------------------\n")
    stdscr.addstr(2, 0, ">>> Hacking Interface Booting Up...\n")
    stdscr.addstr(3, 0, "---------------------------------------\n")
    stdscr.addstr(5, 0, "Please wait...\n")
    
    stdscr.refresh()
    time.sleep(2)

    # Show the actions to the user
    stdscr.clear()
    stdscr.addstr(0, 0, "ACTION MENU:", curses.A_BOLD)
    stdscr.addstr(1, 0, "1. Scan Bluetooth Devices")
    stdscr.addstr(2, 0, "2. Perform Stress Test (Not Supported in Bleak)")
    stdscr.addstr(3, 0, "3. Exit")
    stdscr.addstr(5, 0, "Select an action (1/2/3): ")

    stdscr.refresh()
    
    # Wait for user input
    action = stdscr.getstr(6, 0, 3).decode("utf-8").strip()
    return action

async def scan_bluetooth_devices():
    """Scan for nearby Bluetooth devices and display their details."""
    print("Scanning for Bluetooth devices...\n")
    devices = await BleakScanner.discover()

    if not devices:
        print("No Bluetooth devices found.")
        return None

    print(f"Found {len(devices)} devices:")
    device_list = []
    for idx, device in enumerate(devices):
        print(f"{idx + 1}: {device.name or 'Unknown Device'} | MAC: {device.address}")
        device_list.append((device.address, device.name))
    
    print("=" * 60)
    return device_list

def stress_test_device(target_mac):
    """Stress testing functionality is not directly supported by bleak."""
    print(f"\nStress test functionality is not implemented in bleak as it doesn't support arbitrary packet sending.")
    print(f"Use other tools for stress testing, or interact with Bluetooth Low Energy (BLE) devices.")

async def main(stdscr):
    action = display_hacker_ui(stdscr)

    if action == '1':
        devices = await scan_bluetooth_devices()
        if not devices:
            return

        try:
            choice = int(input("Select a device to interact with (enter the number): ")) - 1
            if choice < 0 or choice >= len(devices):
                print("Invalid choice.")
                return

            target_mac, target_name = devices[choice]
            print(f"\nSelected device: {target_name or 'Unknown Device'} | MAC: {target_mac}")
            
            print("\nActions Available:")
            print("1. Pair with the device")
            print("2. Perform stress test (Not supported in bleak)")
            print("3. Exit")
            action = input("\nChoose an action (1/2/3): ").strip()

            if action == '1':
                print("\nPairing functionality is not implemented yet.")
            elif action == '2':
                stress_test_device(target_mac)
            elif action == '3':
                print("Exiting the script.")
            else:
                print("Invalid action selected.")
        except ValueError:
            print("Invalid input.")
    
    elif action == '2':
        target_mac = input("Enter the MAC address of the target device: ")
        stress_test_device(target_mac)
    
    elif action == '3':
        print("Exiting the script.")
    else:
        print("Invalid input selected.")

if __name__ == "__main__":
    curses.wrapper(lambda stdscr: asyncio.run(main(stdscr)))
