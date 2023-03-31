from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.icon = "calculator.png"
        self.operators = ["*","/","+","-"]
        self.last_was_operator = None
        self.last_button = None
        
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(background_color="black", foreground_color="white")
        
        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "*"],
            ["4", "5", "6", "/"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"],
        ]
        
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text = label, fontsize = 30, background_color ="grey",
                    pos_hint ={"center_x":0.5, "center_y":0.5},
                )
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        
if __name__ == "__main__":
    app = MainApp()
    app.run()