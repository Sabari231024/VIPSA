from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
import cv2
from utils import object_recognition, ocr_detection
from kivy.core.window import Window

class OCRDetectionScreen(Screen):
    def __init__(self, **kwargs):
        super(OCRDetectionScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.image = Image()
        self.layout.add_widget(self.image)
        self.add_widget(self.layout)
        self.space_pressed = False  # Track if space is pressed

        # Bind the spacebar key to self.on_key_down function
        Window.bind(on_key_down=self.on_key_down)

    def on_touch_down(self, touch):
        if touch.is_double_tap:
            self.capture_image()

    def on_key_down(self, window, keycode, *args):
        if keycode == 32:  # Spacebar key code
            self.space_pressed = True

    def on_key_up(self, window, keycode):
        if keycode == 32:  # Spacebar key code
            self.space_pressed = False

    def capture_image(self, *args):
        if self.space_pressed:
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            cv2.imwrite('captured_image.png', frame)
            cap.release()
            self.image.source = 'captured_image.png'
            self.image.reload()
            print("Image Captured!")

            # Perform OCR detection
            result = ocr_detection('captured_image.png')
            print("OCR Detection Result:", result)

class ObjectRecognitionScreen(Screen):
    def __init__(self, **kwargs):
        super(ObjectRecognitionScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.image = Image()
        self.layout.add_widget(self.image)
        self.add_widget(self.layout)
        self.space_pressed = False  # Track if space is pressed

        # Bind the spacebar key to self.on_key_down function
        Window.bind(on_key_down=self.on_key_down)

    def on_touch_down(self, touch):
        if touch.is_double_tap:
            self.capture_image()

    def on_key_down(self, window, keycode, *args):
        if keycode == 32:  # Spacebar key code
            self.space_pressed = True

    def on_key_up(self, window, keycode):
        if keycode == 32:  # Spacebar key code
            self.space_pressed = False

    def capture_image(self, *args):
        if self.space_pressed:
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            cv2.imwrite('captured_image.png', frame)
            cap.release()
            self.image.source = 'captured_image.png'
            self.image.reload()
            print("Image Captured!")

            # Perform object recognition
            result = object_recognition('captured_image.png')
            print("Object Recognition Result:", result)

class CustomScreenManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        sm = CustomScreenManager()
        sm.add_widget(ObjectRecognitionScreen(name='object_recognition'))
        sm.add_widget(OCRDetectionScreen(name='ocr'))
        sm.current = 'object_recognition'
        return sm

if __name__ == '__main__':
    MyApp().run()
