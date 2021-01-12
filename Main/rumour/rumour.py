import random

# receiver class
class Receiver:
    def __init__(self, name, status, message):
        self.name = name
        self.status = status
        self.message = message

class Sender:
    def __init__(self, name):
        self.name = name

    def feedback(self, node, message):
        # check if node has the message if it has, 
        # use p
        # robability to decide whether to gossip or not
        if node.status == 1:
            p = 3
            probability = random.choices([0, 1],((p - 1) / p, 1 / p),k=1)
            if probability[0] == 0:
                node.status = 1
                node.message = message
        # if a node has not received the message
        #  do not stop the gossip
        else:
            node.status = 1
            node.message = message
        print(node.name, node.status, node.message)

    def blind(self, node, message):
        # calculate probability
        p = 3
        determinant = 1 / p
        probability = random.choices([1 / p, ((p - 1) / p)], k=1)
        # if probability is not 1/p continue gossipping
        if determinant != probability[0]:
            node.status = 1
            node.message = message
        print(node.name, node.status, node.message)

    # fixed probability
    def fixed(self, nodes, message):
        global node
        k = 3
        count = 0
        for node in nodes:
            if node.status == 1:
                count += 1
        # if the k nodes have not received the message
        #  gossip to them
        if count != k:
            for node in nodes:
                node.status = 1
                node.message = message
            print(node.name, node.status, node.message)


A = Receiver('A', 0, "No message")
B = Receiver('B', 1, "No message")
C = Receiver('C', 0, "No message")
D = Receiver('D', 1, "No message")
nodes = [A, B, C, D]


s = Sender('S')
s.fixed(nodes, "Fixed Probability")
s.blind(D, "Blind probability")
s.feedback(B, "Feedback Probability")
