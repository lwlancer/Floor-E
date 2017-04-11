import readchar

exit = False

while exit == False:
  c = readchar.readchar()
  key = readchar.readkey()
  if key == w:
    print("Forward Pressed:")
  elif key == 'a':
    print("Left Pressed:")
  elif key == 's':
    print("Back Pressed:")
  elif key == 'd':
    print("Right Pressed:")
  elif key == 'q':
    quit()
