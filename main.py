from kivy.app import App
from kivy.uix.video import Video
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor=(0,0,0,1)


class VideoButtonLayout(BoxLayout):

    def play_video(self):
        
        self.ids.video.state="play"
        
class Videoplay(App):
    def build(self):
        return VideoButtonLayout()

if __name__ == '__main__':
    Videoplay().run()
