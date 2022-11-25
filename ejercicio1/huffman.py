from heapq import heappush, heappop, heapify


class HuffmanCoding(object):
    """HuffmanCoding implementation"""

    def __init__(self):
        super(HuffmanCoding, self).__init__()
        self.tree = []

    def encode(self,symb2freq):
        """Huffman encode the given dict mapping symbols to weights
        :param symb2freq: dictionary of frecuencies
        """
        heap = [(wt,sym) for sym, wt in symb2freq.items()]
        heapify(heap)
        while len(heap) > 1:
            lo = heappop(heap)
            hi = heappop(heap)
            heappush(heap, (lo[0]+hi[0],[lo,hi]))
        self.tree = heap[0]

    def tree_to_table(self,tree=None,n=""):
        """Extracts from Huffman coding tree the symbols, giving a tables with the rows:
         Symbol, frecuency, Coding
        :param n: temporal coding path to leaf
         """
        if not tree:
            tree = self.tree

        if not isinstance(tree[1],list):
            return [[tree[1],tree[0],n]]
        else:
            leaf=[]
            # left subtree
            leaf.extend(self.tree_to_table(tree[1][0],n+"0"))
            # right subtree
            leaf.extend(self.tree_to_table(tree[1][1],n+"1"))
            print("LEAF",)
            return leaf