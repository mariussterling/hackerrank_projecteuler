
from collections import Counter

T = 5
# T = int(input())

data = "\
5H 5C 6S 7S KD 2C 3S 8S 8D TD;\
5D 8C 9S JS AC 2C 5C 7D 8S QH;\
2D 9C AS AH AC 3D 6D 7D TD QD;\
4D 6S 9H QH QC 3D 6D 7H QD QS;\
2H 2D 4C 4D 4S 3C 3D 3S 9S 9D"
data = data.split(';')
x = data[0].split()[:5]

sorted_cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def sort_cards(x, reverse=True):
    return sorted(x, key=lambda x: sorted_cards.index(x[0]), reverse=reverse)

def check_pairs(x, two_pairs=False, three_of_a_kind=False):
    c = Counter([i[0] for i in x])
    
    if three_of_a_kind:
        if c.most_common()[0][1] == 3 and c.most_common()[1][1] == 2:
            # TODO
            return True, c.most_common()[0][0], [i for i in x if i[0] != c.most_common()[0][0]]
        return False, None, None
    elif two_pairs:
        if c.most_common()[0][1] == 2 and c.most_common()[1][1] == 2:
            pair_cards = sort_cards([c.most_common()[0][0], c.most_common()[1][0]])
            return True, pair_cards, [i for i in x if i[0] not in pair_cards]
        else:
            return False, None, None
    else:
        if c.most_common()[0][1] == 2 and c.most_common()[1][1] == 1:
            return True, c.most_common()[0][0], [i for i in x if i[0] != c.most_common()[0][0]]
        return False, None, None

def check_two_pairs(x):
    c = Counter([i[0] for i in x])
    if c.most_common()[0][1] == 2 and c.most_common()[1][1] == 2:
        
    return False, None, None

def check_

def check_
