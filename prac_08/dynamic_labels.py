"""
Dynamic Label
Estimate: 30min
Actual: 25min
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """ Simple Dynamic labels app that has a list of names (strings) and dynamically
    creates a separate Label for each one. """
    names = StringProperty()

    def build(self):
        """ build app from Kv file """
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.list_of_names = ["Name 1", "Name 2", "Name 3", "Name 4"]

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.list_of_names:
            label_name = Label(text=name)
            self.root.ids.main.add_widget(label_name)


DynamicLabelsApp().run()
