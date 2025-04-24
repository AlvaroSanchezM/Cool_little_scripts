import sys
import time

def loading_animation():
    chars = ['.  ', '.. ', '...', '   ']# chars = ['-','\\','|','/']
    while True:
        for char in chars:
            sys.stdout.write('\r' + f'Installing library{char}')
            sys.stdout.flush()
            time.sleep(0.2)

if __name__ == "__main__":
    try:
        loading_animation()
    except KeyboardInterrupt:
        sys.stdout.write('\r' + 'Installation complete!      \n')
