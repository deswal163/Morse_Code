import numpy as np
import sounddevice as sd

morse_json = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}


def gen_sine_wave(char):
  # dit and dah duration
  t = .05 if char == '.' else .15

  # make a space character so low that only elephants can hear it
  freq = 500 if char != ' ' else 10

  S_rate = 44100
  T = 1 / S_rate
  N = S_rate * t
  t_seq = np.arange(N) * T
  omega = 2 * np.pi * freq
  wave = np.concatenate((np.sin(omega * t_seq), np.zeros(5000)))

  return wave


def code_to_sound(code):
  wave_group = np.zeros(0)
  for char in code:
    new_wave = gen_sine_wave(char)
    wave_group = np.concatenate((wave_group, new_wave))

  return wave_group


def morse_converter(text):
  try:
    return morse_json[text.lower()] + " "
  except KeyError:
    return " "


def text_to_morse():
  input_string = input("Enter the String : ")
  morse_string = "".join([morse_converter(i) for i in input_string])
  print(f"Morse-Code is : {morse_string}")

  if input("Want to play sound (y/n): ").lower() == 'y':
    morse_sound = code_to_sound(morse_string)
    sd.play(morse_sound, 44100, blocking=True)


def morse_to_text():
  morse_code = input("Enter the Morse-Code : ").lower().split(" ")
  test_string = ""
  for each_word in morse_code:
    if each_word in morse_json.values():
      test_string += list(i for i in morse_json if morse_json[i] == each_word)[0]
    else:
      if each_word == "":
        test_string += " "
      else:
        test_string += "_"

  print(f"Text is : {test_string}")


menu = "Enter the following choices : \n" \
       "1. Text to Morse-Code.\n" \
       "2. Morse-Code to Text.\n" \
       "3. To repeat the Menu.\n" \
       "0. Exit the Program.\n"

print(menu)
choice = None
while choice != 0:
  choice = int(input("Enter your choice : "))
  match choice:
    case 1:
      text_to_morse()
    case 2:
      morse_to_text()
    case 3:
      print(menu)
