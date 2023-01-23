print('---------- Welcome to Blackjack ----------\n')

import random


def playgame(*cards):

    x =(random.sample(cards, 2))

    d =(random.sample(cards, 2))

    return x
    return d


def newcard(*cards):

    hitcard = (random.choice(cards))
    return hitcard


def invalidentry():
    print('Invalid Entry. Please enter y or n.')


def invalidoption():
    print('Invalid Entry. Please enter h or s.\n')


def endgame():
    print('\nThank you for playing. Goodbye!\n')


#*****************************************************************
r = 'y'

while r == 'y':
    pg = input('Would you like to start a new game? (y/n): ')

    while pg.lower() != 'y' and pg.lower() != 'n':

        print('Invalid entry. Please enter a y or n.')

        pg = input('Would you like to start a new game? (y/n): ')
        continue
    else:
        pass

    if pg.lower() == 'n':
        endgame()
        break
    else:

        print('\n**** Lets Play. ****\n')

        cards = (1,2,3,4,5,6,7,8,9,10)
        pc = playgame(*cards)
        pctotal = pc[0] + pc[1]

        dc = playgame(*cards)
        dctotal = dc[0] + dc[1]

        print('You drew a {} and a {}. Total is {}' .format(pc[0], pc[1], pctotal))
        print('Dealer drew a {} and a hidden card\n' .format(dc[0]))


    while pg.lower() =='y':

        if pctotal != 21:
            hitme = input('Hit or stand. (h/s): ')
        else:
            pass

        if hitme.lower() == 'h' and pctotal != 21:


            h = newcard(*cards)
            pctotal += h
            print('Hit Me - you drew {} your total is {}' .format(h, pctotal))

            if pctotal > 21:
                print('BUST!! Dealer wins\n')
                break

        elif hitme.lower() != 's' and pctotal != 21:

            #if hitme.lower() != 's': #and pctotal != 21:
            invalidoption()
            continue
        else:
            print('\nYou Stand.')
            print("The dealer's hidden card is a {} and has a total of {}" .format(dc[1], dctotal))


            while dctotal <= 16:
                d = newcard(*cards)
                dctotal += d

                print('Dealer drew {}. Dealer total {}' .format(d, dctotal))

            else:

                if dctotal > 21:
                    print('Dealer Bust. You win!\n')
                    break

                elif dctotal < pctotal:
                    print('Player total is {} and the Dealer total is {}' .format(pctotal, dctotal))
                    print('You Win!\n')


                elif dctotal == pctotal or dctotal > pctotal:
                    print('Player total is {} and the Dealer total is {}' .format(pctotal, dctotal))
                    print('Dealer Wins!\n')
                    break

                    #r = input('Would you like to play again? (y/n): ')

                    #if r == 'y':
                    #    continue
                    #else:
                    #    break



                break

    else:
        invalidentry()
else:
    print('GOODBYE!!!')
