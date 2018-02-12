from Chapter_4.Trie import Trie

t = Trie()

t.insert('apple')
t.insert('apples')
t.insert('banana')
t.insert('applet')

# print( t.has_word('na') )
# print( t.has_prefix('ap') )

t.dump_trie()
