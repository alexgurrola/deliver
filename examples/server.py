from comm import Comm
import plac


def main():
    server = Comm()
    server.listen('localhost', 8089)


if __name__ == '__main__':
    try:
        plac.call(main)
    except KeyboardInterrupt:
        print('\nGoodbye!')
