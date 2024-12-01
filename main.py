from models.device import Light, Thermostat, DoorLock
from models.smart_home import SmartHome
from models.automation import AutomationRule
from models.user import User
from utilities.command import run_simulation

def main():
    """
    Main function to run the enhanced Smart Home simulation.
    """
    # Initialize a smart home
    home = SmartHome("My Smart Home")

    # Create a user with access control
    admin = User("admin", "password", is_admin=True)
    home.add_user(admin)

    # Add devices to the smart home
    living_room_light = Light("Living Room Light", power_usage=10)
    hall_thermostat = Thermostat("Hall Thermostat", 72, power_usage=50)
    front_door_lock = DoorLock("Front Door", power_usage=5)

    home.add_device(living_room_light, "Lighting")
    home.add_device(hall_thermostat, "Climate Control")
    home.add_device(front_door_lock, "Security")

    # Create automation rules
    unlock_lights_rule = AutomationRule(
        trigger=lambda: not front_door_lock.is_locked,
        action=lambda: living_room_light.turn_on(),
        description="Turn on the Living Room Light when the Front Door is unlocked."
    )
    home.add_automation_rule(unlock_lights_rule)

    # Run the simulation
    run_simulation(home, admin)


if __name__ == "__main__":
    main()
