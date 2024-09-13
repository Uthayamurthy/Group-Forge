# Group Forge
### A Python script to group people randomly while trying to ensure the best possible equal gender representation in all groups !

## Prerequisite
A Namelist along with gender in a csv file (refer to test-data.csv)

## How it works ?
- Group Forge first reads the dataset, gets the total people count. 
- Next, it asks for a ideal group size. It then determines the number of groups and number of members in each group smartly (**Note:** Members in each group will be equal to the ideal group size or 1 lesser)
- After determing the group size of every group, it starts to choose members randomly from the dataset and keeps filling the groups.
- Finally, once the groups are ready, it writes the names to files (each group has it's own file) inside a sub directory named "final_groups"
