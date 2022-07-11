from TikTokApi import TikTokApi
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from random import randint
from pytube import YouTube



class application(App):
    def build(self):
        main_layout = BoxLayout(orientation="horizontal")
        self.link = TextInput(
            multiline=False, 
                        readonly=False, 
                        halign="left", 
                        font_size=14, 
                        size_hint=(.2, .1),
                        pos_hint={'center_x': .05, 'center_y': .4},
        )
        self.link.bind(text=self.on_text)
        self.button = Button(text='Download',
                        size_hint=(.2, .1),
                        pos_hint={'center_x': .5, 'center_y': .4})
        self.button.bind(on_press=self.on_press_button)

        main_layout.add_widget(self.link)
        main_layout.add_widget(self.button)
        return main_layout
    
    def on_press_button(self, idk):
        self.download(self.value)

    def on_text(self, instance, value):
        self.value = str(value)
        print(value)

    def download(self, id):
        link = id
        if "https://www.youtube.com/" in link:
            try:
                YouTube(id).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(f"/storage/emulated/0/Downloads/tiktok{randint(0, 100)}.mp4")
            except:
              YouTube(id).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(f"/storage/emulated/0/Download/tiktok{randint(0, 100)}.mp4")  
        try:
            start = "video/"
            end = "?is_copy_url="
            id = id[id.find(start)+len(start):id.rfind(end)]
            print(id)
            api = TikTokApi()
            data = api.video(id=f"{id}").bytes()
            try:
                with open(f"/storage/emulated/0/Downloads/tiktok{randint(0, 100)}.mp4", 'wb') as output:
                    output.write(data)
            except:
                with open(f"/storage/emulated/0/Download/tiktok{randint(0, 100)}.mp4", 'wb') as output:
                    output.write(data)
        except Exception as e:
            print(e)

app = application()
app.run()