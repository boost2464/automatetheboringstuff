import time, sys
indent = 0 #how many spaces to indent
indentIncreasing = True #Whether the iindentation is increasing

try:
    while True: #the main loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second

        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 50:
                #change the direction:
                indentIncreasing = False

        else:
            #Decreasing the number of spaces
            indent = indent - 1
            if indent == 10:
                #change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
