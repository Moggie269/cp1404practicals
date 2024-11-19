"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometers
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty


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
        result = float(value) * 1.60934
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, value, increment):
        result = int(value) + int(increment)
        self.root.ids.input_number.text = str(result)


MilesToKmConverterApp().run()
