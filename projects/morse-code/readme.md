https://morsecode.world/international/translator.html

```
ABCDEFGHIJKLMNOPQRSTUVWXYZ
.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..


alphabet_dict= {
	"A": ".-",
	"B": "-...",
	"C": "-.-.",
	"D": "-..",
	"E": ".",
	"F": "..-.",
	"G": "--.",
	"H": "....",
	"I": "..",
	"J": ".---",
	"K": "-.-",
	"L": ".-..",
	"M": "--",
	"N": "-.",
	"O": "---",
	"P": ".--.",
	"Q": "--.-",
	"R": ".-.",
	"S": "...",
	"T": "-",
	"U": "..-",
	"V": "...-",
	"W": ".--",
	"X": "-..-",
	"Y": "-.--",
	"Z": "--.."
}

0123456789
----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----.

number_dict= {
	"0": "-----",
	"1": ".----",
	"2": "..---",
	"3": "...--",
	"4": "....-",
	"5": ".....",
	"6": "-....",
	"7": "--...",
	"8": "---..",
	"9": "----."
}

```
Below is the circuit board of 2 LED Morse Code decoders. 
- Ground (GND) is pinned to the Negative blue line ( refer to the image below )
- PIN 7 or GPIO4 is for RED LED.
- The positive leg ( long leg ) of the LED is pinned with GPIO4
- The Negative leg ( shorter leg ) of the RED LED is pinned to the ground ( negative, blue )
- Similarly, the Blue LED is another LED with GPIO17
![image](https://github.com/e2eSolutionArchitect/RaspberryPi/assets/62712515/33f8415c-144b-4c2d-a494-c4a75a114a23)

