from models.device import DoorLock
def run_simulation(home, user):
    """
    Runs the smart home simulation.
    """
    while True:
        print("\n=== Smart Home Simulation ===")
        print("1. List Devices")
        print("2. List Device Groups")
        print("3. Control Devices")
        print("4. Run Automations")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            home.list_devices()
        elif choice == "2":
            home.list_groups()
        elif choice == "3":
            home.list_devices()
            index = int(input("\nEnter the device number to control: ")) - 1
            device = home.get_device(index)

            if device:
                print(f"\nControlling {device.name}:")
                print("1. Turn ON")
                print("2. Turn OFF")
                if isinstance(device, DoorLock):
                    print("3. Lock/Unlock")

                action = input("Choose an action: ")
                if action == "1":
                    device.turn_on()
                elif action == "2":
                    device.turn_off()
                elif action == "3" and isinstance(device, DoorLock):
                    if device.is_locked:
                        device.unlock()
                    else:
                        device.lock()
                else:
                    print("Invalid action!")
        elif choice == "4":
            home.run_automation_rules()
        elif choice == "5":
            print("Exiting the simulation. Goodbye!")
            break
        else:
            print("Invalid choice!")
