import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.uix.boxlayout import BoxLayout
class MyApp(App):

    def build(self):
        btn = Button(text ="НЕ НАТИСКАЙ", size_hint = (0.2  ,None), height='40sp',
                    pos_hint={'center_x': 0.5})
        btn.on_press = self.btn_click
        text = Label(text='Hello world')
        col = BoxLayout(orientation='vertical' ,
                    pos_hint={'center_x': 0.5, 'center_y': 0.5})
        col.add_widget(text)
        col.add_widget(btn)
        return col

    def btn_click(self):
        print("Я КАЗАВ НЕ НАТИСКАЙ!!!")
        exit()



if __name__ == '__main__':
    MyApp().run()