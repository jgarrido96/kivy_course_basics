# pip install kivy
# installed kivy extension for easier to read '.kv' file
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout

from kivy.uix.widget import Widget


class CanvasExample7(Widget):
    pass

class CanvasExample6(Widget):
    pass



class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(20)
        self.vy = dp(20)
        with self.canvas:
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1/15)

    def on_size(self, *args):
        print("On size : " + str(self.width) + ", " + str(self.height))
        self.ball.pos = (self.center_x-self.ball_size/2, self.center_y-self.ball_size/2)    # Now that's a center ball (circle)

    def update(self, dt):           # dt = delta time # essentially this is making a timed movement depending on the Clock.schedule_interval, updating the position of the ball
        # print("update")
        x, y, = self.ball.pos

        x += self.vx
        y += self.vy

        # self.ball_size / self.width
        # self.vx = - self.vx
        if y + self.ball_size > self.height:
            y = self.height - self.ball_size
            self.vy = -self.vy
        if x + self.ball_size > self.width:
            x = self.width - self.ball_size
            self.vx = -self.vx
        if y < 0:
            y = 0
            self.vy = -self.vy
        if x < 0:
            x = 0
            self.vx = -self.vx

        self.ball.pos = (x+10, y)



class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 100, 400, 500), width=2)
            Color(0, 1, 0)                              # Color() only applies to things AFTER it's been defined
            Line(circle=(400, 200, 80), width=2)
            Line(rectangle=(700, 500, 150, 100), width=5)
            self.rect = Rectangle(pos=(700, 200), size=(150, 100))
            #         pos is ^ x, y location of bottom left corner, size is width, height
    
    def on_button_a_click(self):
        # print("foo")
        x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)

        diff = self.width - (x+w)               # Using this you can make the box move to the right until it touches the edge of the window, and will work even when you change the size of the screen
        if diff < inc:
            inc = diff


        x += inc                                 # This is saying we're moving the button over by 10dp every button click. can also be y instead, or both on another line
        self.rect.pos = (x, y)                      # self.rect.pos allows us to change the location of self.rect. pretty cool stuff


class CanvasExample3(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample1(Widget):
    pass

class WidgetsExample(GridLayout):
    count = 1
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("1")
    # slider_value_txt = StringProperty("Value")    # One way to show slider info
    text_input_str = StringProperty("foo")

    def on_button_click(self):              # Counts on button click
        print("Button Clicked")
        if self.count_enabled:                  # if count_enabled == True, then count, else, don't count
            self.count +=1                      # Won't work if it's just count. needs to be self.count
            self.my_text = str(self.count)
    
    def on_toggle_button_state(self, widget):
        print("toggle state: " + widget.state)      # 'widget.state' has two states for toggle. 'down' = activated, 'normal' = de-activated
        if widget.state == "normal":                # This if/else changes the text of the toggle button from 'OFF' to 'ON' depending on widget.state
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True

    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))

    # def on_slider_value(self, widget):                    # One way to show slider info. more work but it works
    #     print("Slider: " + str(int(widget.value)))
    #     self.slider_value_txt = str(int(widget.value))

    def on_text_validate(self, widget):                     # Saves text on enter
        self.text_input_str = widget.text

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-bt"                # Same as in the .kv file. just setting orientation of the buttons. which comes first etc.
        for i in range(0, 100):                      # for loop to create multiple buttons. '(0, 10)' means you're creating 10 buttons
            # size = dp(100) + i*10                 # incriment the size with this weird trick!
            size = dp(100)
            b = Button(text=str(i+1), size_hint=(None, None), size=(size, size)) # str(i+1) is incrementing by one
#                                                   # size_hint can be in % out of 1 or you can use None, and use size to specify using dp. dp has to be imported
        
            self.add_widget(b)                      # adds button

# class GridLayoutExample(GridLayout):
#     pass

class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):                  # This is for formatting/displaying for adaptive screen sizes
    pass
"""    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical' # unless otherwise specified, the buttons will automatically orient horizontally (left to right)
        b1 = Button(text="A") # Declare what you want (Button), what text you want it to display (text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")

        self.add_widget(b1) # Creates a button widget that will take up the whole size of the screen. 
        self.add_widget(b2) # If you add more buttons it will adjust so all buttons fit by default, while taking up all the entire screen
        self.add_widget(b3) # buttons will appear in the order you call them. Buttons will appear "B", "C", "A" if you call them in that order
        # Not: Had to change "TheLab.kv" to reference "BoxLayoutExample" instead of "MainWidget" at the top of the .kv file. filename stays the same"""

class MainWidget(Widget):                           # Houses the Widget functions, can be called anythin at all
#                                                   # Widgets are buttons that can be put anywhere on the screen
    pass

class TheLabApp(App):                               # This is the base app
    pass




TheLabApp().run()                                   # Calls and runs the app