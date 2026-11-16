from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.core.window import Window
from analyzer import analyze_chart

Window.clearcolor = (0.05, 0.06, 0.09, 1)

class Root(BoxLayout):
    def __init__(self, **kw):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kw)
        self.image_path = None

        self.add_widget(Label(
            text='[b]TradeScanner AI[/b]', markup=True,
            font_size='28sp', color=(0.8, 0.6, 1, 1), size_hint_y=0.12
        ))
        self.img_display = Image(size_hint_y=0.45)
        self.add_widget(self.img_display)

        btn = Button(
            text='رفع صورة الشارت', size_hint_y=0.12,
            background_normal='', background_color=(0.4, 0.2, 0.8, 1),
            font_size='18sp'
        )
        btn.bind(on_press=self.open_picker)
        self.add_widget(btn)

        self.result = Label(
            text='ارفع صورة للبدء', font_size='20sp',
            color=(0.9, 0.9, 0.9, 1), size_hint_y=0.2
        )
        self.add_widget(self.result)

    def open_picker(self, inst):
        content = BoxLayout(orientation='vertical')
        fc = FileChooserIconView(filters=['*.png', '*.jpg', '*.jpeg'])
        content.add_widget(fc)
        sel = Button(text='اختيار', size_hint_y=0.15)
        content.add_widget(sel)
        popup = Popup(title='اختر صورة', content=content, size_hint=(0.95, 0.95))
        sel.bind(on_release=lambda x: self.pick(fc.selection, popup))
        popup.open()

    def pick(self, selection, popup):
        if selection:
            self.image_path = selection[0]
            self.img_display.source = self.image_path
            r = analyze_chart(self.image_path)
            s, c, ms = r['signal'], r['confidence'], r['time_ms']
            if s == 'BUY':
                self.result.text = f'شراء (BUY)\nثقة: {c}% | {ms}ms'
                self.result.color = (0.2, 1, 0.4, 1)
            elif s == 'SELL':
                self.result.text = f'بيع (SELL)\nثقة: {c}% | {ms}ms'
                self.result.color = (1, 0.3, 0.3, 1)
            else:
                self.result.text = f'انتظار (HOLD)\n{ms}ms'
                self.result.color = (1, 0.8, 0.2, 1)
        popup.dismiss()

class TradeScannerApp(App):
    def build(self):
        return Root()

if __name__ == '__main__':
    TradeScannerApp().run()
