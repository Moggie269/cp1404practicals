"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometers
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
CONVERSION_RATE = 1.60934
ZERO = 0


class MilesToKmConverterApp(App):
    """ MilesToKmConverterApp is a Kivy App for converting miles to kilometers """
    message = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Convert Miles to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = f"{int(self.root.ids.input_number.text) * 1.60934}"
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = float(value) * CONVERSION_RATE
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = f'{ZERO}'


    def handle_increment(self, value, increment):
        try:
            result = int(value) + int(increment)
        except ValueError:
            result = ZERO + int(increment)
        self.root.ids.input_number.text = str(result)


MilesToKmConverterApp().run()
