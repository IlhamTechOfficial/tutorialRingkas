import pyautogui as py


# https://pyautogui.readthedocs.io/en/latest/
lebar_screen, tinggi_screen = py.size()
print(lebar_screen, tinggi_screen)
print(lebar_screen*tinggi_screen)

posisi_x, posisi_y = py.position()
print("x:",posisi_x, "y:", posisi_y)

py.click(405, 23)
py.doubleClick(405, 23)

py.write("Assalamualaikum, nama saya Amirul Ashraf")

# Assalamualaikum, nama saya Amirul Ashraf

py.hotkey('ctrl', 'v')
py.hotkey('ctrl', 'shift', 'esc')

print(py.KEY_NAMES)
# py.keyDown('ctrl')
# py.press('x')
# py.keyUp('ctrl')

# py.keyDown('ctrl')
# py.press('v')
# py.keyUp('ctrl')

# "Nama saya Amirul"

py.alert("Nama saya ialah Amirul Ashraf!")

py.rightClick(930,301)
