# Name:

def Alphabet(character):
    
    pattern = ''
    
    if (character == 'a' or character == 'A'):
        for i in range(1, 8):
            if (i == 1 or i == 2 or i == 4 or i == 5):
                print(6*'* ')
            else:
                print(2*'* ', 2*' ', 2*'* ')
           
    elif (character == 'b' or character == 'B'):
        for i in range(1, 8):
            if (i == 2 or i == 6):
                print(6*'* ')
            elif (i == 1 or i == 4 or i == 7):
                print(5*'* ')
            else:
                print(2*'* ', 2*' ', 2*'* ')    
            
    elif (character == 'c' or character == 'C'):
        for i in range(1, 8):
            if (i == 1 or i == 2 or i == 6 or i == 7):
                print(6*'* ')
            else:
                print(2*'* ')
                
    elif (character == 'd' or character == 'D'):
        for i in range(1, 8):
            if (i == 1 or i == 7):
                print(4*'* ')
            elif (i == 2 or i == 6):
                print(5*'* ')
            else:
                print(2*'* ', 2*' ', 2*'* ')
                
    elif (character == 'e' or character == 'E'):
        for i in range(1, 8):
            if (i == 1 or i == 2 or i == 6 or i == 7 or i == 4):
                print(6*'* ')
            else:
                print(2*'* ')
                
    elif (character == 'f' or character == 'F'):
        for i in range(1, 8):
            if (i == 1 or i == 2 or i == 4):
                print(6*'* ')
            else:
                print(2*'* ')
                
    elif (character == 'g' or character == 'G'):
        for i in range(1, 8):
            if (i == 1 or i == 2 or i == 6 or i == 7):
                print(6*'* ')
            elif (i == 3):
                print(2*'* ')
            else:
                print(2*'* ', '', 3*'* ')
                
    elif (character == 'h' or character == 'H'):
        for i in range(1, 8):
            if (i == 4):
                print(6*'* ')
            else:
                print(2*'* ', '  ', 2*'* ')
                
    elif (character == 'i' or character == 'I'):
        for i in range(1, 8):
            if (i == 1 or i == 2 or i == 6 or i == 7):
                print(6*'* ')
            else:
                print('   ', 2*'* ')
                
    elif (character == 'j' or character == 'J'):
        for i in range(1, 8):
            if (i == 1 or i == 2):
                print(6*'* ')
            elif (i == 6 or i == 7):
                print(4*'* ')
            else:
                print('   ', 2*'* ')
                
    elif (character == 'k' or character == 'K'):
        for i in range(1, 8):
            if (i == 1 or i == 7):
                print(2*'* ', 3*' ', 2*'* ')
            elif (i == 2 or i == 6):
                print(2*'* ', ' ', 2*'* ')
            elif (i == 3 or i == 5):
                print(2*'* ', '', 2*'* ')
            else:
                print(4*'* ')
    
    elif (character == 'l' or character == 'L'):
        for i in range(1, 8):
            if (i == 6 or i == 7):
                print(2*' ', 4*'* ')
            else:
                print(2*' ', 2*'* ')
                
    elif (character == 'm' or character == 'M'):
        for i in range(1, 8):
            if (i == 1 or i == 7 or i == 6):
                print(2*'* ', 2*' ', 2*'* ')
            elif (i == 2 or i == 3):
                print(6*'* ')
            else:
                print(2*'* ', '* ', 2*'* ')
                
    elif (character == 'n' or character == 'N'):
        for i in range(1, 8):
            if (i == 1 or i == 7 or i == 6):
                print(2*'* ', 2*' ', 2*'* ')
            elif (i == 2):
                print(3*'* ', '', 2*'* ')
            elif (i == 3 or i == 4):
                print(6*'* ')
            elif (i == 5):
                print(2*'* ', ' *', 2*'* ')
            else:
                print(2*'* ', '* ', 2*'* ')
                
    elif (character == 'o' or character == 'O'):
        for i in range(1, 8):
            if (i == 1 or i == 2 or i == 6 or i == 7):
                print(6*'* ')
            else:
                print(2*'* ', 2*' ', 2*'* ')
                
    elif (character == 'p' or character == 'P'):
        for i in range(1, 9):
            if (i == 1 or i == 2 or i == 4 or i == 5):
                print(6*'* ')
            elif (i == 6 or i == 7 or i == 8):
                print(2*'* ')
            else:
                print(2*'* ', 2*' ', 2*'* ')
                
    elif (character == 'q' or character == 'Q'):
        for i in range(1, 8):
            if (i == 1 or i == 2 or i == 6):
                print(6*'* ')
            elif (i == 4):
                print(3*'* ', '', 2*'* ')
            elif (i == 5):
                print(2*'* ', '', 3*'* ')
            elif (i == 7):
                print(7*'* ')
            else:
                print(2*'* ', 2*' ', 2*'* ')
                
    elif (character == 'r' or character == 'R'):
        for i in range(1, 9):
            if (i == 1 or i == 2 or i == 4 or i == 5):
                print(6*'* ')
            elif (i == 6 or i == 7 or i == 8):
                print(2*'* ')
            else:
                print(2*'* ', 2*' ', 2*'* ')
                
    elif (character == 's' or character == 'S'):
        for i in range(1, 8):
            if (i == 1 or i == 2 or i == 4 or i == 6 or i == 7):
                print(6*'* ')
            elif (i == 3):
                print(2*'* ')
            else:
                print(7*' ', 2*'* ')  
                  
    elif (character == 't' or character == 'T'):
        for i in range(1, 8):
            if (i == 1 or i == 2):
                print(6*'* ')
            else:
                print('   ', 2*'* ')
                
    elif (character == 'u' or character == 'U'):
        for i in range(1, 8):
            if (i == 6 or i == 7):
                print(6*'* ')
            else:
                print(2*'* ', 2*' ', 2*'* ')
    
    elif (character == 'v' or character == 'V'):
        for i in range(1, 8):
            if (i == 1):
                print(2*'* ', 4*' ', 2*'* ')
            elif (i == 2):
                print('', 2*'* ', 2*' ', 2*'* ')
            elif (i == 3):
                print(' ', 2*'* ', '', 2*'* ')
            elif (i == 4):
                print('  ', 4*'* ')
            elif (i == 5):
                print('   ', 3*'* ')
            elif (i == 6):
                print('    ', 2*'* ')
            else:
                print('     ', '* ')
    
    elif (character == 'w' or character == 'W'):
        for i in range(1, 8):
            if (i == 1 or i == 2 or i == 7):
                print(2*'* ', 2*' ', 2*'* ')
            elif (i == 6 or i == 7):
                print(6*'* ')
            else:
                print(2*'* ', '* ', 2*'* ')
                
    elif (character == 'x' or character == 'X'):
        for i in range(1, 8):
            if (i == 1 or i == 7):
                print(2*'* ', 6*' ', 2*'* ')
            elif (i == 2 or i == 6):
                print(' ', 2*'* ', 2*' ', 2*'* ')
            elif (i == 3 or i == 5):
                print(3*' ', 4*'* ')
            else:
                print(5*' ', 2*'* ')
    
    elif (character == 'y' or character == 'Y'):
        for i in range(1, 8):
            if (i == 1 or i == 2):
                print(2*'* ', 2*' ', 2*'* ')
            elif (i == 3 or i == 4):
                print(6*'* ')
            else:
                print(3*' ', 2*'* ')
    else:
        for i in range(1, 8):
            if (i == 1 or i == 2 or i == 6 or i == 7):
                print(6*'* ')
            elif (i == 3):
                print('     ', 2*'* ')
            elif (i == 4):
                print('   ', 2*'* ')
            elif (i == 5):
                print(' ', 2*'* ')

    return pattern
# Taking input from the user:

name = input("Enter your Name: ")

for i in name:
    c = Alphabet(i)
    print(c)