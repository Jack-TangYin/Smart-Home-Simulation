class AutomationRule:
    """
    Represents an automation rule for the smart home.
    """
    def __init__(self, trigger, action, description):
        self.trigger = trigger  # Function that checks the condition
        self.action = action    # Function that performs the action
        self.description = description

    def execute(self):
        """
        Checks the trigger and executes the action if the trigger condition is met.
        """
        if self.trigger():  # Dynamically evaluates the trigger condition
            print(f"Automation triggered: {self.description}")
            self.action()
            return True
        return False


def run_automation_rules(self):
    """
    Runs all automation rules and displays feedback for triggered rules.
    """
    print("\nRunning Automation Rules...")
    triggered_any = False
    for rule in self.automation_rules:
        if rule.execute():
            triggered_any = True
    if not triggered_any:
        print("No automation rules were triggered.")
