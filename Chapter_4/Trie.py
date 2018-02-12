class TrieNode:
    def __init__(self, char):
        # define the node label char
        self.char = char
        # to hold this nodes childs nodes
        self.childrens = []
        # to flag this node is it last char for word or not
        self.word_finished = False
        # to define how many times this char appears
        self.counter = 1


class Trie:
    def __init__(self):
        # This Trie node which always be empty node
        self.root = TrieNode('')
        self.curr = self.root

    def insert(self, word):
        """
            This to insert new key to trie what will do :
                iterate over all string chars and check if this char exist 
                in each node childrens so move to it and go to next one
                 if it's not exist so add new node for it and append it to current node
                 childrens
                
        :param word: string 
        :return: void
        """
        current = self.root
        for ch in word:
            current = self.insert_ch(current, ch)

        current.word_finished = True

    def insert_ch(self, head, ch):
        """
            traverse current node childs if our char in it's childs
            return it otherwise, add new node by our char and add it
            to current node childs
        :param head: this refer to current node in trie 
        :param ch:  the char whanted to insert
        :return: new node added if not exist oterwise return it if it's exist
        """
        for child in head.childrens:
            if child.char == ch:
                child.counter += 1
                return child

        new_child = TrieNode(ch)
        head.childrens.append( new_child )

        return new_child

    def has_word(self, word):
        """
            traverse string and check fpr each char is it current node
            childs has this char or not if it is not return false
            otherwise, return true
        :param word: string wanted word to search 
        :return: bolean true if trie has word or false if doesn't
        """
        current = self.root

        for ch in word:
            char_not_found = True
            for child in current.childrens:
                if child.char == ch:
                    char_not_found = False
                    current = child
                    break

            if char_not_found:
                return False

        return True

    def has_prefix(self, prefix):
        """
            It's so like has word function but here we return the counter
            value which refer to the number of existance of this prefix in words
            which built the trie
        :param prefix: prefix wanted to check if it exist or not in any words 
        :return: True or false if prefix exist or not and count of existence of this prefix 
        """
        current = self.root

        if not current.childrens:
            return False, 0

        for ch in prefix:
            char_not_found = True
            for child in current.childrens:
                if child.char == ch:
                    char_not_found = False
                    current = child
                    break
            if char_not_found:
                return False, 0

        return True, current.counter

    def dump_trie(self, level = 0):
        print( self.curr.char )
        if self.curr.word_finished:
            print()
            # print( " " * level )
        for child in self.curr.childrens:
            self.curr = child
            self.dump_trie( level + 2 )

        self.curr = self.root