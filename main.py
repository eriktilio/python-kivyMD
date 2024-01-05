from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView

from app.constants import Config


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class MainApp(MDApp):
    APP_NAME = Config.APP_NAME
    APP_VERSION = Config.APP_VERSION

    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Light"
        return Builder.load_file("app/screens/main_screen.kv")

    def on_start(self):
        self.title = self.APP_NAME


if __name__ == "__main__":
    MainApp().run()
