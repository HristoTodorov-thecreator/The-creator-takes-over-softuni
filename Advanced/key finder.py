import keyboard

def on_key(event):
    print(f"the_key: {event.name}")

keyboard.on_press(on_key)  # Засича всяко натискане
keyboard.wait()