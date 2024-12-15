import random
import time
import os
import asyncio
from bleak import BleakScanner

def display_banner():
    """Display a banner with creator information."""
    # Clear the console for aesthetics (Termux does support 'clear')
    os.system('clear')  
    print("=" * 60)
    print(" " * 18 + "ILLUSIVEHACKS BLUETOOTH TOOL")
    print("=" * 60)
    print("Created by: IllusiveHacks")
    print("Purpose: Scans for Bluetooth devices, tests pairing, and performs stress testing.")
    print("=" * 60)
    print()

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

async def main():
    display_banner()
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
        print("2. Perform stress test (Not implemented in bleak)")
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

if __name__ == "__main__":
    asyncio.run(main())
