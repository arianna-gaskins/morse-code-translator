

def morse(text):

    text = str(text)

    letNumToMorse = {
        'A' : '.-', 'B' : '-...', 'C' : '-.-.', 'D' : '-..',
        'E' : '.', 'F' : '..-.', 'G' : '--.', 'H' : '....',
        'I' : '..', 'J' : '.---', 'K' : '-.-', 'L' : '.-..',
        'M' : '--', 'N' : '-.', 'O' : '---', 'P' : '.--.',
        'Q' : '--.-', 'R' : '.-.', 'S' : '...', 'T' : '-',
        'U' : '..-', 'V' : '...-', 'W' : '.--', 'X' : '-..-',
        'Y' : '-.--', 'Z' : '--..',  '1' : '.----', '2' : '..---',
        '3' : '...--', '4' : '....-', '5' : '.....', '6' : '-....',
        '7' : '--...', '8' : '---..', '9' : '----.', '0' : '-----' }
    
    morseToLetNum = {
        '.-' : 'A', '-...' : 'B', '-.-.' : 'C', '-..' : 'D',
        '.' : 'E', '..-.' : 'F', '--.' : 'G', '....' : 'H',
        '..' : 'I', '.---' : 'J', '-.-' : 'K', '.-..' : 'L',
        '--' : 'M', '-.' : 'N', '---' : 'O', '.--.' : 'P',
        '--.-' : 'Q', '.-.' : 'R', '...' : 'S', '-' : 'T',
        '..-' : 'U', '...-' : 'V', '.--' : 'W', '-..-' : 'X',
        '-.--' : 'Y', '--..' : 'Z', '.----' : '1', '..---' : '2',
        '...--' : '3', '....-' : '4', '.....' : '5', '-....' : '6', 
        '--...' : '7', '---..' : '8','----.' : '9', '-----' : '0'}

    
    

while (1==1):
    message = str(input('Enter your message: '))

    morse(message)


