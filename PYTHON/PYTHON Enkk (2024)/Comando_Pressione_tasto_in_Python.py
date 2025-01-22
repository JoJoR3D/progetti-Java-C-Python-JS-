import keyboard

#fin quando non verrà premuto il tasto 'invio' verrà stampato "NON è stato premuto il tasto invio"

while not(keyboard.is_pressed('enter')):
  print("NON è stato premuto il tasto invio")
  if keyboard.is_pressed('enter'):
     print("E' stato premuto il tasto invio")
  	