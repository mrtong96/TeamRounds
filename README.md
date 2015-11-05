''' Overview '''

This program is designed to try to pick teams for archery team rounds given a .csv file with names in one row, and scores in the other. In the case it can not assign even teams of 3, it will use 2 and go by closes average scores. This program uses hill climbing to try and achieve good but not optimal outputs. Runs reasonably well on inputs of 100 people with 100 trials of 200 improvement attempts each (~2s on my laptop) which is more than fast enough for its intended use (determining teams for a group of <50 archers).

''' Getting Started '''
* clone this repository
* run hc.py

''' Implementation Notes '''
* This algorithm takes the highest and lowest scoring teams and tries to make their scores closer to each other num_iter times.
* It is possible for the algorithm to get stuck if the scores for the max and min teams are as close as possible, for this reason I use a random ordering num_iter times.
* This could be improved in the future by trying different pairs if the min pair and max pair can not be imrpoved any further. It should be able to get out of local optimum better.

''' Other Notes '''
* This was originally written for the Cal Archery Program
* This program was originally designed to do something else, but the project's specs got changed and so this code got repurposed.

''' Contact '''
email: mrtong96@berkeley.edu

