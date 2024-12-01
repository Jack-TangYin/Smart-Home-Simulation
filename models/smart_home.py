class SmartHome:
    """
    Represents a smart home that manages multiple devices.
    """
    def __init__(self, name):
        self.name = name
        self.devices = []
        self.device_groups = {}
        self.automation_rules = []
        self.users = []

    def add_device(self, device, group_name):
        """
        Adds a device to the smart home and assigns it to a group.
        """
        self.devices.append(device)
        if group_name not in self.device_groups:
            self.device_groups[group_name] = []
        self.device_groups[group_name].append(device)
        print(f"Added {device.name} to group '{group_name}' in {self.name}.")

    def list_devices(self):
        """
        Lists all devices in the smart home.
        """
        print(f"\nDevices in {self.name}:")
        for i, device in enumerate(self.devices, start=1):
            print(f"{i}. {device.status()}")

    def list_groups(self):
        """
        Lists all device groups and their devices.
        """
        print("\nDevice Groups:")
        for group, devices in self.device_groups.items():
            print(f"{group}: {[device.name for device in devices]}")

    def get_device(self, index):
        """
        Retrieves a device by its index in the device list.
        """
        if 0 <= index < len(self.devices):
            return self.devices[index]
        else:
            print("Invalid device index!")
            return None

    def add_automation_rule(self, rule):
        """
        Adds an automation rule to the smart home.
        """
        self.automation_rules.append(rule)
        print(f"Automation rule added: {rule.description}")

    def run_automation_rules(self):
        """
        Runs all automation rules and displays feedback for triggered rules.
        """
        print("\nRunning Automation Rules...")
        triggered_any = False
        for rule in self.automation_rules:
            if rule.execute():  # Executes and evaluates the trigger
                triggered_any = True
        if not triggered_any:
            print("No automation rules were triggered.")


    def add_user(self, user):
        """
        Adds a user to the smart home system.
        """
        self.users.append(user)
        print(f"User '{user.username}' added to {self.name}.")
