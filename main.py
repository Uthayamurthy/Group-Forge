import csv
import random

# Helper Functions

# Pretty print - Just to Add colors to the text
def pprint(text, color_code='94'):
    print(f'\033[{color_code}m' + text + '\033[0m')

# Seperator between sections
def sep():
    pprint('+'*20, '95')

# Main Code

people_details = []

sep()
pprint('Reading Name List ...')

# Change the filename here according to your needs ...
namelist_file = 'test-data.csv' 
with open(namelist_file) as csv_file:
    csvreader = csv.reader(csv_file)

    for row in csvreader:
        people_details.append(row)

M_list = []
F_list = []

for detail in people_details:
    if detail[1] == 'M':
        M_list.append(detail[0:1])
    else:
        F_list.append(detail[0:1])
pprint('Done!', '32')

sep()
pprint(f'Male Count: { len(M_list) }')
pprint(f'Female Count: { len(F_list) }')

n = len(people_details)
pprint('Ideal group size : ')
grp_ideal = int(input())

def groupify(n, grp_ideal):
    """
    This function groups a given number of people into groups of a specified ideal size.
    
    Parameters:
    n (int): The total number of people to be grouped.
    grp_ideal (int): The ideal size of each group.
    
    Returns:
    list: A list of integers representing the size of each group.
    """

    grp_nums = []
    # The case when n is a multiple of grp_ideal
    if n % grp_ideal == 0:
        for i in range(n // grp_ideal):
            grp_nums.append(grp_ideal)
    # If that's not the case, group smartly with adjustments ...
    else:
        ideal_count = n // grp_ideal + 1
        extra = grp_ideal - (n % grp_ideal)

        for i in range(ideal_count):
            grp_nums.append(grp_ideal)

        for j in range(1, extra+1):
            grp_nums[-j] -= 1

    return grp_nums

sep()
group_nums = groupify(n, grp_ideal)
pprint(f'Group Distribution : {group_nums}')
pprint(f'Total Count : {sum(group_nums)}')
pprint(f'Number of Groups : {len(group_nums)}')
sep()

def pick_choice(gender):
    """
    Picks a person of the specified gender from the available lists. If Unavailable, picks from the other list.
    
    Parameters:
    gender (str): The gender of the person to be picked ('M' or 'F').
    
    Returns:
    The picked person.
    """
    global M_list, F_list
    def pick_male():
        M_Choice = random.choice(M_list)
        M_list.remove(M_Choice)
        return M_Choice
    def pick_female():
        F_Choice = random.choice(F_list)
        F_list.remove(F_Choice)
        return F_Choice
    
    if gender == 'M':
        # Try to pick a male, if not, pick a female
        try:
            return pick_male()
        except:
            return pick_female()
    else:
        # Try to pick a female, if not, pick a male
        try:
            return pick_female()
        except:
            return pick_male()

# A Simple Custom Data Type to hold the data of group.
class group:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.members = []

# Create necessary group objects !

groups_list = []

for i in range(len(group_nums)):
    groups_list.append(group(f'Group-{i+1}', group_nums[i]))

# Group People !
for i in range(max(group_nums)):
    for grp in groups_list:
            if grp.size != len(grp.members):
                # If there are atleast two slots left to fill
                if grp.size - len(grp.members)  >= 2:
                    grp.members.append(pick_choice('M'))
                    grp.members.append(pick_choice('F'))
                # If only one slot is left, fill with majority
                else:
                    if len(M_list) >= len(F_list):
                        grp.members.append(pick_choice('M'))
                    else:
                        grp.members.append(pick_choice('F'))

# Write the data to csv files inside final groups directory
for g in groups_list:
    pprint(f'Preparing {g.name}')
    with open(f'final_groups/{g.name}.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(g.members)

    pprint('Done !', '92')

sep()