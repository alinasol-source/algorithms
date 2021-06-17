import time

class borNode:
    def __init__(self):
        self.go_to = {}
        self.out = []
        self.fake = None


def create_machine(words):
    if type(words) is not list:
        words = [words]
    root = borNode()
    for word in words:
        node = root
        for symbol in word:
            node = node.go_to.setdefault(symbol, borNode())
        node.out.append(word)
    queue = []
    for node in root.go_to.values():
        queue.append(node)
        node.fake = root

    while len(queue) > 0:
        node1 = queue.pop(0)
        for key, node2 in node1.go_to.items():
            queue.append(node2)
            node_fake = node1.fake
            while node_fake is not None and key not in node_fake.go_to:
                node_fake = node_fake.fake
            if node_fake:
                node2.fake = node_fake.go_to[key]
            else:
                node2.fake = root
            node2.out += node2.fake.out
    return root

def Aho_Korasik(string, pattern):
    enter_ind = []
    operation_count = 0
    startTime = time.time()
    root = create_machine(pattern)
    node = root
    l = len(string)
    for i in range(l):
        operation_count += 1
        while node is not None and string[i] not in node.go_to:
            node = node.fake
        if node is None:
            node = root
            continue
        node = node.go_to[string[i]]
        for word in node.out:
            enter_ind.append(i - len(word) + 1)
    totalTime = time.time() - startTime
    return enter_ind, operation_count, totalTime
