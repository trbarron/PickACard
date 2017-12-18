#!/usr/bin/python
import random
import matplotlib.pyplot as plt
import numpy

deck_size = 100
threshold = 0.5

def make_hand(hand_size):
    got_hand = False
    while not got_hand or len(hand) != len(set(hand)):
        hand = []
        for i in range(0,hand_size):
            hand.append(random.randint(1,deck_size))
        got_hand = True
    return(hand)

def run_hand(hand_size):
    hand = make_hand(hand_size)
    for i in range(0,len(hand)):
        decision = False
        skip_evaluation = False
        max_skipped_card = 0
        percent_lowest = 1
        saved_card = 0.1

        #Skip immediately if you've skipped a larger card already
        if hand[i] < max_skipped_card:
            skip_evaluation = True

        #Skip if its the last card
        if i == len(hand)-1:
            saved_card = hand[i]
            skip_evaluation = True
            
        #Evaluate the % every consecutive card is lower
        if hand[i] > len(hand)-i and not skip_evaluation:
            max_skipped_card = max(max_skipped_card,hand[i])
            for w in range(1,len(hand)-i):
                percent_lowest = percent_lowest * ((hand[i]-w-i)/(deck_size-i-w))
            if percent_lowest > threshold:
                decision = True
                saved_card = hand[i]
                break

    return saved_card == max(hand)

def run_trial(hand_size,deck_size,iterations):
    successful_trials = 0
    for i in range(0,iterations):
        successful_trials = successful_trials + run_hand(hand_size)
    return [deck_size,(successful_trials / iterations)]

results = []
for i in range(2,20):
    results.append(run_trial(10,i*10,100000))
x, y = zip(*results)
plt.plot(x,y)
plt.plot(x,y,'ko')
plt.title('Pick A Card, Any Card! With Variable Deck Size\nThreshold: 0.5, Deck Size: 100')
plt.ylabel('Correct Selection (%)')
plt.xlabel('Deck Size')
plt.ylim((0,1))
plt.show()
