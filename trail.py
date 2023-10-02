from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.camera import Camera
import cv2
from utils import object_recognition, ocr_detection

class OCRDetectionScreen(Screen):
    def __init__(self, **kwargs):
        super(OCRDetectionScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.camera = Camera(play=True)
        self.layout.add_widget(self.camera)
        self.capture_button = Button(text="Capture Image")
        self.capture_button.bind(on_press=self.capture_image)
        self.layout.add_widget(self.capture_button)
        self.add_widget(self.layout)
        self.double_tap_count = 0
        self.double_tap_time = 0.3  # Adjust as needed
        self.last_tap_time = 0

    def on_touch_down(self, touch):
        if touch.is_double_tap:
            current_time = Clock.get_time()
            if current_time - self.last_tap_time <= self.double_tap_time:
                self.capture_image()
            self.last_tap_time = current_time

    def capture_image(self, *args):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cv2.imwrite('captured_image.png', frame)
        cap.release()
        self.image.source = 'captured_image.png'
        self.image.reload()
        result = object_recognition('captured_image.png')
        print("Object Recognition Result:", result)

class ObjectRecognitionScreen(Screen):
    def __init__(self, **kwargs):
        super(ObjectRecognitionScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.camera = Camera(play=True)
        self.layout.add_widget(self.camera)
        self.capture_button = Button(text="Capture Image")
        self.capture_button.bind(on_press=self.capture_image)
        self.layout.add_widget(self.capture_button)
        self.add_widget(self.layout)
        self.double_tap_count = 0
        self.double_tap_time = 0.3  # Adjust as needed
        self.last_tap_time = 0

    def on_touch_down(self, touch):
        if touch.is_double_tap:
            current_time = Clock.get_time()
            if current_time - self.last_tap_time <= self.double_tap_time:
                self.capture_image()
            self.last_tap_time = current_time

    def capture_image(self, *args):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cv2.imwrite('captured_image.png', frame)
        cap.release()
        self.image.source = 'captured_image.png'
        self.image.reload()
        result = object_recognition('captured_image.png')
        print("Object Recognition Result:", result)

class CustomScreenManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        sm = CustomScreenManager()
        sm.add_widget(OCRDetectionScreen(name='ocr'))
        sm.add_widget(ObjectRecognitionScreen(name='object_recognition'))
        return sm

if __name__ == '__main__':
    MyApp().run()
