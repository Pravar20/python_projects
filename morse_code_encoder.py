morse_decode_dict = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.----',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    ' ': '/'
}


def morse_encode(sentence):
    print(sentence, end=":\n\t")
    for each_letter in sentence:
        print(morse_decode_dict[each_letter], end=' ')
    print()


if __name__ == '__main__':
    strings = ["pravar kochar", "programming is fun", "test alpha",
               "professor kartchner", "cmsc", "coincidence can be freaky",
               "today i laughed until my abs started hurting so i can skip "
               "the gym", "wonder is the beginning of wisdom",
               "to find yourself think for yourself"]
    for s in strings:
        morse_encode(s)
