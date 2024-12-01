class Device:
    """
    Base class for all smart devices.
    """
    def __init__(self, name, power_usage=0):
        self.name = name
        self.is_on = False
        self.power_usage = power_usage

    def turn_on(self):
        self.is_on = True
        print(f"{self.name} is now ON.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} is now OFF.")

    def status(self):
        return f"{self.name} is {'ON' if self.is_on else 'OFF'}."

    def get_power_usage(self):
        return self.power_usage if self.is_on else 0


class Light(Device):
    def dim(self, level):
        if self.is_on:
            print(f"{self.name} is dimmed to {level}%.")
        else:
            print(f"{self.name} is OFF. Turn it ON to dim.")


class Thermostat(Device):
    def __init__(self, name, temperature, power_usage=50):
        super().__init__(name, power_usage)
        self.temperature = temperature

    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"{self.name} is set to {self.temperature}°F.")


class DoorLock(Device):
    def __init__(self, name, power_usage=5):
        super().__init__(name, power_usage)
        self.is_locked = True

    def lock(self):
        self.is_locked = True
        print(f"{self.name} is now LOCKED.")

    def unlock(self):
        self.is_locked = False
        print(f"{self.name} is now UNLOCKED.")

    def status(self):
        lock_status = "LOCKED" if self.is_locked else "UNLOCKED"
        return f"{self.name} is {lock_status} and {'ON' if self.is_on else 'OFF'}."
