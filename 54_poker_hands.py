import copy

first = 0
second = 0
third = 0
count_1 = 0
a_wins1 = 0
b_wins = 0

card_to_value_dict = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}

royal_flush_cards = [10, 11, 12, 13, 14]



def consecutive(hand):
    last_val = None
    for x in hand:
        if not last_val:
            last_val = x
        else:
            if x - last_val > 1:
                return False
            else:
                last_val = x
    
    return True


def compute_score(hand):
    card_count = {}
    color_count = {}

    for card in hand:
        card_number = card[0]
        card_suit = card[1]
        if card_count.get(card_number):
            card_count[card_number] += 1
        else:
            card_count[card_number] = 1
        if color_count.get(card_suit):
            color_count[card_suit] += 1
        else: 
            color_count[card_suit] = 1

    sorted_hand = sorted(map(lambda x: card_to_value_dict[x[0]], hand))

    sorted_values_list = sorted(list(card_count.values()))

    highest = 0
    highest_count = 0
    hg = None
    second_highest = 0
    second_highest_count = 0
        

    # print(card_count)
    for k, v in card_count.items():
        if v >= highest_count and card_to_value_dict[k] > highest:
            highest = card_to_value_dict[k]
            hg = k
            highest_count = v

    card_count_copy = copy.deepcopy(card_count)
    del card_count_copy[hg]

    for k, v in card_count_copy.items():
        if v >= second_highest_count:
            second_highest = card_to_value_dict[k]
            second_highest_count = v

    # royal flush
    if sorted_hand == royal_flush_cards and len(color_count) == 1:
        print('royla')
        print(hand)
        return 100000
    
    # straight flush
    if consecutive(sorted_hand) and len(color_count) == 1:
        print('straight')
        print(hand)
        return 90000 + sorted_hand[4]

    # four of a kind
    if len(card_count) == 2 and sorted_values_list[0] == 4:
        print('4 of a kind')
        return 80000 + highest * 20 + sorted_hand[4]
    
    # full house
    if len(card_count) == 2 and sorted_values_list[0] == 3:
        print('full house')
        return 70000 + highest * 20 + second_highest + sorted_hand[4] / 10

    # flush 
    if len(color_count) == 1:
        # print('flush')
        # print(hand)
        # print(6000 + sorted_hand[4])
        return 60000 + sorted_hand[4]
    
    # straight
    if consecutive(sorted_hand):
        return 50000 + sorted_hand[4]
    
    # three of a kind
    if sorted_values_list[0] == 3:
        print('here')
        print('thisisda')
        # print(f'hand2={hand} and value={4000 + highest * 20 + sorted_hand[4]}')
        return 40000 + highest * 20 + sorted_hand[4]

    # 2 pairs
    if len(card_count) == 3:
        i = 0
        ###already_used = 
        used_numbers = []
        for k in card_count.keys():
            if card_count[k] == 2:
                used_numbers.append(card_to_value_dict[k])
                used_numbers.append(card_to_value_dict[k])
            
        ##
        
        un_used_numbers = []
        for j in reversed(sorted_hand):
            if j not in used_numbers:
                un_used_numbers.append(j)
        # print(
        #     f'handddd={hand} and value={3000 + highest * 20 + second_highest + i / 10} and highest={highest} and secondhighest = {second_highest} and hig={i}')
        global third
        third += 1
        return 30000 + highest * 100 + second_highest * 20 + un_used_numbers[0]

    # one pair
    if len(card_count) == 4:
        used_numbers = []
        for k in card_count.keys():
            if card_count[k] == 2:
                used_numbers.append(card_to_value_dict[k])
                used_numbers.append(card_to_value_dict[k])
        un_used_numbers = []
        for j in reversed(sorted_hand):
            if j not in used_numbers:
                un_used_numbers.append(j)

        un_used_numbers = sorted(un_used_numbers)


        # print(
        #     f'hand={hand} and value={2000 + highest * 20 + i} higest={highest}  hig={i}')
        global second 
        second += 1
        return 20000 + highest * 100 + un_used_numbers[2] * 20 + un_used_numbers[1] + un_used_numbers[0] // 10

    # high card
    # print('just the number')
    global first
    first += 1
    return sorted_hand[4] * 100 + sorted_hand[3] * 20 + sorted_hand[2] + sorted_hand[1] // 10 + sorted_hand[0] // 100
        
        

def a_wins(text):
    global count_1
    count_1 += 1
    cards = text.rstrip('\n').split(' ')
    hand_a = cards[0:5]
    hand_b = cards[5:]
    score_a = compute_score(hand_a)
    score_b = compute_score(hand_b)

    if score_a > score_b:
        global a_wins1
        a_wins1 += 1
    else:
        global b_wins
        b_wins += 1

    # print(f'score a = {score_a}')
    # print(f'score b = {score_b}')
    return score_a > score_b


def poker_hands():
    no_wins = 0
    f = open("p054_poker.txt", "r")
    for text in f:
        if a_wins(text):
            no_wins += 1
    print(f'first={first} second={second} third={third} total={first+second+third}')
    print(count_1)
    print(f'a_winns={a_wins1} b_wins={b_wins}')
    return no_wins


print(poker_hands())
