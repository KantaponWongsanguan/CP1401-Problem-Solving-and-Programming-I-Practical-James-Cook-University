"""
Miles to Kilometers converter
Estimate: 30 min
Actual: 50 min
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Kantapong Wong'

from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesToKmConverterApp(App):
    """ MilesToKmConverterApp is a Kivy app for converting Miles to Km """
    output_km = StringProperty()

    def build(self):
        """ build app from Kv file """
        Window.size = (500, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """ handle calculate when called for """
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """ Function for Up and Down, update input and call for converter function """
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """ convert input to float or return 0 when it is invalid """
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesToKmConverterApp().run()
