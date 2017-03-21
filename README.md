# dynamic
Dynamic Programming Algorithms Spring 2017


## dynamic design:
The recursive idea is that if we start at month 12 and figure out the best cost for month 12 for each city. Based off of that value we can know the best path starting at each city for month 11 based off of month 12 and the cost to move cities. Then based off of knowing month 12 and month 11 we can figure out month 10 all the way back to month 1.

recurrence relation:
min_cost(month, min) = min_cost(month+1, min+current_min)

dynamic table:

dp algo pseudo code:


traceback step:

## complexity:  

## implementation:

## demonstration:
