n = 12	# number of months
k = 3	# number of cities

NY = 0;		# these are the corresponding rows in the city matrix
LA = 1;		# also the corresponding row / col in the opportunity matrix
DEN = 2;	# so just reference them

# set up the
# hardcoded (gross)
city_items = [8, 3, 10, 43, 15, 48, 5, 40, 20, 30, 28, 24, 18, 1, 35, 18, 10, 19, 18, 10, 8, 5, 8, 20,40, 5, 8, 13, 21, 12, 4, 27, 25, 10, 5, 15]
opportunity_items = [0, 20, 15, 20, 0, 10, 15, 10, 0]

city_matrix = []

i=0

for r in range (0,k):
    row = []
    for c in range (0,n):
        row.append(city_items[i])
        i+=1
    city_matrix.append(row)

# print the city_matrix
print "city_matrix"
for row in city_matrix:
    for val in row:
        print '{:4}'.format(val),
    print

# set up the opportunity costs
# could do this as a map if you like
opportunity_cost_matrix = []

i=0

for r in range (0,k):
    row = []
    for c in range (0,k):
        row.append(opportunity_items[i])
        i+=1
    opportunity_cost_matrix.append(row)

# print the city_matrix
print "opportunity_cost_matrix"
for row in opportunity_cost_matrix:
    for val in row:
        print '{:4}'.format(val),
    print










