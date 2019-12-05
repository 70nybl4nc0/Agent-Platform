from chord.node import Node
from utils import aid


class Chord:
    'Interface for handle chord ring'
    def __init__(self, id_s, ip_s, port_s):
        for i in range(1, 1023 - port_s):
            try:
                self.node = Node(id_s, ip_s, port_s + i) 
                break
            except:
                raise Exception('Se falló asignando la dirección')
        

    def __del__(self):
        'kill local node and release resources'
        pass 
    
    def add(self, key, value):
        "add a new data into the chord ring"
        self.node.save(key, value)


    def get(self, key):
        'get value of a key located in Chord ring'
        pass
    

    def get_local_values(self):
        'get local node values'
        pass


    def get_values(self):
        'gets all the values stored in the ring'


    def delete_key(self, key):
        'deletes a given key'
        pass


    def join(self, other):
        'joins two chords together (really only one node)'
        pass


    def get_value(self):
        'gets a random value from the chord ring'
        pass