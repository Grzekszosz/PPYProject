from pynput import keyboard

captured_keys = []
def on_press(key):
    try:
        # Sprawdzenie, czy wciśnięty klawisz to zwykły znak
        if hasattr(key, 'char') and key.char:
            captured_keys.append(key.char)
            print(f"Key {key.char} pressed")
        elif key == key.esc:
            # Zakończenie nasłuchiwania, gdy naciśnięty zostanie Enter
            print("Finishing capture")
            return False
    except AttributeError:
        # Obsługa innych klawiszy, które mogą nie mieć atrybutu 'char'
        print(f"Special key {key} pressed")


def on_release():
    pass

#with Listener(on_press=on_press,) as listener:
#   listener.join()