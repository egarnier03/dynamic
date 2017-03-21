# dynamic
Dynamic Programming Algorithms Spring 2017


## recursive idea:
The recursive idea is that if we start at month 12 and figure out the best cost for month 12 for each city. Based off of that value we can know the best path starting at each city for month 11 based off of month 12 and the cost to move cities. Then based off of knowing month 12 and month 11 we can figure out month 10 all the way back to month 1.

recurrence relation:
min_cost(month, min) = min_cost(month+1, min+current_min)

dynamic table:

      m1  m2  m3  m4  m5  m6  m7  m8  m9  m10 m11 m12
NYC
cost1_1
cost1_2
cost1_3
LA 
cost2_1
cost2_2
cost2_3
DEN
cost3_1
cost3_2
cost3_3


dp algo pseudo code:


traceback step:
