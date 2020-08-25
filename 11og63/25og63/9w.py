import random
HEADS = 1
TAILS = 2
TOSSES = 10
total_h = 0
total_k = 0
def main():
    global total_h
    global total_k
    for toss in range(TOSSES):
        if random.randint(HEADS, TAILS) == HEADS:
            print('Heads')
            total_h = total_h + 1
        else:
            print('Tails')
            total_k = total_k + 1
    print('Total Heads',total_h)
    print('Total Tails',total_k)
main()