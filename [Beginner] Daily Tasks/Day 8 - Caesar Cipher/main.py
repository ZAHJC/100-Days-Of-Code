import art

# Alphabet for cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# For application loop
applicationState = 1

# Utilised to not allow symbols at this stage
def parse_input(input_text, alphabet):
    for letter in input_text:
        if letter not in alphabet:
            raise ValueError("The input is not in the alphabet")
        else:
            return

# Checks if encoding or decoding and shifts characters by set amount
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            if encode_or_decode == "decode":
                shift_amount *= -1
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")



while applicationState == 1:

    # Gets user input and runs expected result
    print(art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    parse_input(text, alphabet)
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    applicationState = input("Are there anymore tasks you would like to do? Yes(1) No(0)")



