class Messenger:
    def __init__(self, connection):
        self._connection = connection

    def send_message(self, text, option=None):
        self._connection.send(text)


class ExtendedMessenger(Messenger):  # Bad example !
    def send_message(self, text, option=None):
        if option == 'message':
            self._connection.send(text)
        elif option == 'image':
            self._connection.send(text)
        elif option == 'math':
            print('2+2=4')
        else:
            print('...')
