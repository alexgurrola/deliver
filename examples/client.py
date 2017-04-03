from comm import Comm
import plac


def main():
    client = Comm()
    client.connect('localhost', 8089)
    client.send(b'hello')
    data = client.receive()
    print('data:', data)
    client.disconnect()


if __name__ == '__main__':
    try:
        plac.call(main)
    except KeyboardInterrupt:
        print('\nGoodbye!')
