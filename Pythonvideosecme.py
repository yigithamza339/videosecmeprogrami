import time
import webbrowser
print("📽️video seçme porogramı")
isim = input("merhaba isminiz nedir ")
print("merhaba senin için video bulunuyor "+isim)
print("biraz bekle... ")
time.sleep(5)
input("videon oluşturuldu videonu görmek için enter a bas "+ isim)
time.sleep(2)
webbrowser.open("https://youtube.com/shorts/JZcYAEIi6dw?si=gJrkWpB8syIk_zQw")