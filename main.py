import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
import os
import socket
Window.title = 'Поисковик'

class SearcherApp(App):
    def build(self):
        def on_text(self, *args):
            data = textinput.text
            self.data2 = mes.text
            if data.isnumeric():
                if data == '111':
                    mes.text = 't.me/Chalr_bot'
                if data == '789':
                    mes.text = f'{os.getpid()}\n{os.name}\n{socket.gethostname()}'
                if data == '987':
                    mes.text = f'{os.name}'
                if data == '2947':
                    mes.text = 'Rufinds - разработчик программы\n Rufinds ==> Привет, я создатель программы. Она будет расширятся со временем будут обновление и т.д,\nпока что это только бета так что надеюсь ты найдёшь баги и скажешь их мне!'
            elif data == 'h':
                mes.text = '111 - telegrambot\n789 - all about your ps(phone)\n987 - название ос\n2947 - Rufinds\nh - помощь\n'
            else:
              textinput.text = ''
        lable = GridLayout(cols = 1)
        textinput = TextInput(text='Search....')
        mes = TextInput(text='Здесь будет то что вы ищите....')
        textinput.bind(text = on_text)
        lable.add_widget(textinput)
        lable.add_widget(mes)
        return lable
SearcherApp().run()