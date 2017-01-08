# encoding: utf-8
import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

kivy.require("1.9.1")
from kivy.config import Config

Config.set('graphics', 'width', '280')
Config.set('graphics', 'height', '490')
from kivy.garden.androidtabs import *


class Aba(BoxLayout, AndroidTabsBase):
    pass


# carrega o som da contagem da serie inteira
serie = SoundLoader.load('sounds/serie.wav')

# variaveis globais
contador = 0
series = 10
intervalo = 60


# tela principal
class TelaP(Screen):
    pass


# tela dos exercicios
class TelaE(Screen):
    pass


class MyGrid(GridLayout):
    pass


# classe principal
class ScreenManagement(ScreenManager):
    def troca_TelaP(self):
        self.current = 'TelaP'

    def troca_TelaE(self):
        self.current = 'TelaE'

    def add_button(self):
        # mygrid.add_widget(Button)
        print("NOVO TREINO")

    # chamada qdo aperta o botao, essa chama a func_temp que so toca uma vez e
    # por sua vez chama a funcao toca que toca as series com o intervalo
    def comeca(self):
        # aqui deverá ser criado um trigger()???
        Clock.schedule_once(self.temp_func, 0)

    def temp_func(self, dt):
        serie.play()
        Clock.schedule_interval(self.toca, intervalo + 35)

    def toca(self, dt):
        global contador
        contador += 1
        if contador == series:
            contador = 0
            return False
        serie.play()

    def para(self):
        serie.stop()
        Clock.unschedule(self.temp_func)


class MPTApp(App):
    def build(self):
        self.root = ScreenManagement()
        return self.root


if __name__ == '__main__':
    MPTApp().run()

