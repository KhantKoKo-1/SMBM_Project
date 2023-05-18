from socketio.namespace import BaseNamespace

class MyNamespace(BaseNamespace):
    def on_connect(self):
        print('Connected')

    def on_disconnect(self):
        print('Disconnected')

    def on_my_event(self, data):
        print('Received:', data)
        self.emit('my_response', {'response': 'Data received'})

    def on_my_broadcast_event(self, data):
        print('Received broadcast:', data)
        self.broadcast_event('my_response', {'response': 'Broadcast received'})