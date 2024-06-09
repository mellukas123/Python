# Assume that you are simulating management of the light
# in house. Implement SIMPLE fasade for controlling lights
# in your rooms (switching off and on lights by simple prints :P)

class Light:
    def __init__(self, name):
        self.name = name
        self.state = 'off'

    def switch_on(self):
        if self.state == 'off':
            self.state = 'on'
            print(f"{self.name} light is now ON.")
        else:
            print(f"{self.name} light is already ON.")

    def switch_off(self):
        if self.state == 'on':
            self.state = 'off'
            print(f"{self.name} light is now OFF.")
        else:
            print(f"{self.name} light is already OFF.")


class LightFacade:
    def __init__(self):
        self.living_room_light = Light('Living Room')
        self.kitchen_light = Light('Kitchen')
        self.bedroom_light = Light('Bedroom')

    def switch_on_living_room_light(self):
        self.living_room_light.switch_on()

    def switch_off_living_room_light(self):
        self.living_room_light.switch_off()

    def switch_on_kitchen_light(self):
        self.kitchen_light.switch_on()

    def switch_off_kitchen_light(self):
        self.kitchen_light.switch_off()

    def switch_on_bedroom_light(self):
        self.bedroom_light.switch_on()

    def switch_off_bedroom_light(self):
        self.bedroom_light.switch_off()


# Example usage
if __name__ == "__main__":
    light_control = LightFacade()
    light_control.switch_on_living_room_light()
    light_control.switch_off_living_room_light()
    light_control.switch_on_kitchen_light()
    light_control.switch_off_kitchen_light()
    light_control.switch_on_bedroom_light()
    light_control.switch_off_bedroom_light()
