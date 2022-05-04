import pandas as pd
import sys
import numpy as np

def get_input(file_name):
    
    """
    
    reads the input file and returns the first line as numbers_to_be_called
    and tickets as a dataframe.
    
    parameters:
    arg1 (str): filename
  
    returns:
    list: numbers to be called
    DataFrame: dataframe of all tickets
    
    """
    
    with open(file_name) as file:
        lines = [i.strip().split() for i in list(file)]
        numbers_to_be_called = lines[0]
        numbers_to_be_called = [i.split(',') for i in numbers_to_be_called]
        numbers_to_be_called = [item for sublist in numbers_to_be_called for item in sublist]
        tickets = []
        for i,j in enumerate(lines[1:]):
            if j:
                tickets.append(j)
        tickets = pd.DataFrame(tickets)
        
    return numbers_to_be_called, tickets

def get_winning_tickets(numbers_to_be_called, tickets, ticket_size=None):
    
    """
    
    returns statements for first and last bingo tickets
    
    parameters:
    numbers_to_be_called (list): numbers to be called for BINGO!!!
    tickets (DataFrame): dataframe of all tickets
    ticket_size (int): need this just in case the size of the ticket differs (most likely won't need it)
  
    returns: None
    
    """
    winning_tickets = []
    numbers_called = []
    winning_numbers = []
    for m, i in enumerate(numbers_to_be_called):
        numbers_called.append(i)
        for j in np.array_split(tickets, tickets.shape[0] / int(ticket_size)):
            for k in range(j.shape[0]):
                if set(j.iloc[:,k]) <= set(numbers_called) or (set(j.iloc[k,:]) <= set(numbers_called)):
                    if not True in [j.equals(x) for x in winning_tickets]:
                        winning_tickets.append(j)
                        winning_numbers.append(numbers_called[:m+1])
                    else:
                        pass
    print('First ticket to be winning is {}'.format(winning_tickets[0]))
    print('First ticket won after calling {}'.format(winning_numbers[0][-1]))
    print('First Score is {}'.format(sum([int(i) for i in set(winning_tickets[0].values.flatten()) - set(winning_numbers[0])]) * int(winning_numbers[0][-1])))
    print('Last ticket to be winning is {}'.format(winning_tickets[-1]))
    print('Last ticket won after calling {}'.format(winning_numbers[-1][-1]))
    print('Last Score is {}'.format(sum([int(i) for i in set(winning_tickets[-1].values.flatten()) - set(winning_numbers[-1])]) * int(winning_numbers[-1][-1])))
    
            
def main():
    numbers_to_be_called, tickets = get_input(str(sys.argv[1]))
    get_winning_tickets(numbers_to_be_called, tickets, str(sys.argv[2]))

if __name__ == '__main__':
    
    """ USAGE: python3 day_4.py filename(str) size_of_ticket(int) """
    
    main()
