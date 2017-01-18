""" Sample controller """
from kervi.controller import Controller, ControllerNumberInput, ControllerButton


class PowerOffButton(ControllerButton):
    def __init__(self, controller):
        ControllerButton.__init__(
            self,
            controller.component_id+".powerDown",
            "Power off",
            controller
        )
        self.add_to_dashboard("system", "power")

    def click(self):
        print ("stop kervi")
        self.controller.spine.send_command("stopKervi")


class RebootButton(ControllerButton):
    def __init__(self, controller):
        ControllerButton.__init__(
            self,
            controller.component_id+".reebotDown",
            "Reboot",
            controller
        )
        self.add_to_dashboard("system", "power")

    def click(self):
        print ("restart kervi")
        self.controller.spine.send_command("restartKervi")



class SystemController(Controller):
    def __init__(self):
        Controller.__init__(self, "systemController", "System")
        self.type = "controller_category"

        self.add_components(PowerOffButton(self), RebootButton(self))
        self.parameters = {}


MY_CONTROLLER = SystemController()
