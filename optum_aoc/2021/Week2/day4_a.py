import sys
import time


def parse(file_loc):
    """
    read input and separates into two lists, one for cards, another for bingo numbers
    """

    bingo_input = open(file_loc, "r").read().strip('\n\n').split()
    bingo_numbers = bingo_input[0].split(',')
    bingo_cards = separate_cards(bingo_input[1:])

    return bingo_numbers, bingo_cards


def separate_cards(card_numbers):
    """
    Each card has a total of 25 numbers, this function separates all of the numbers into their cards
    """
    cards = []
    for i in range(0, len(card_numbers), 25):
        cards.append(card_numbers[i:i + 25])

    return cards


def mark_cards(bingo_numbers, bingo_cards):
    """"
    iterates through the cards and bingo numbers, if the number matches on one of the cards, it is checked too see if
    there is a bingo.
    """
    winning_cards = []
    for number in bingo_numbers:
        for card in bingo_cards:
            if card not in winning_cards:
                for iterate, c in enumerate(card):
                    if int(number) == int(c):
                        card[iterate] = 1000
                        check_response = check_cards(card)
                        if check_response != None:
                            winning_cards.append(card)
                            if len(winning_cards) == len(bingo_cards):
                                bingo(winning_cards[-1], number)


def check_cards(card):
    """"
    checks rows and columns for bingo
    """
    row_card = check_rows(card)
    col_card = check_columns(card)

    if row_card != None:
        return row_card
    elif col_card != None:
        return col_card
    else:
        return None


def check_rows(card):
    """
    checks row of a card to see if there is a bingo
    """
    for i in range(0, len(card), 5):
        row_numbers = card[i:i + 5]
        if all(x == 1000 for x in row_numbers):
            return card
    return None


def check_columns(card):
    """
    checks columns of card to see if there is a bingo
    """
    for i in range(0, 5):
        col_numbers = card[i::5]
        if all(x == 1000 for x in col_numbers):
            return card
    return None


def bingo(card, last_called_number):
    """
    Takes winning card and last called number to get a cards score
    """
    print('Bingo!!')
    print(card)
    print(last_called_number)
    for i in range(0, len(card), 5):
        unmarked_sum = 0
        for unmarked in card:
            if unmarked != 1000:
                unmarked_sum += int(unmarked)
        print(unmarked_sum)
        print(f'Score of winning card = {int(unmarked_sum) * int(last_called_number)}')
        sys.exit()


def main(file):
    numbers, cards = parse(file)

    mark_cards(numbers, cards)


if __name__ == '__main__':
    start_time = time.time()
    file_loc = 'Day4_input.txt'
    main(file_loc)
    end_time = time.time()
    duration = end_time - start_time
