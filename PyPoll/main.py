import os
import csv

elections = ['1', '2']

for election in elections:

    electionfile1 = os.path.join('..', 'PyPoll', 'raw_data', 'election_data_' + elections[1] + '.csv')
    outputfile = os.path.join('..', 'PyPoll', 'output_data', 'election_data_' + elections[1] + '.txt')
        
    candidates = []
    unique_candidates = []
    candidate_1 = []
    candidate_2 = []
    candidate_3 = []
    candidate_4 = []

    with open(electionfile1, newline='') as electiondata1:
        csvreader = csv.reader(electiondata1, delimiter=',')
        next(csvreader, None)

        for row in csvreader:
            candidates.append(row[2]) 
            
        for candidate in candidates:
            if candidate not in unique_candidates:
                unique_candidates.append(candidate)

for candidate in candidates:
    if candidate == unique_candidates[0]:
        candidate_1.append(candidate)
    
    if candidate == unique_candidates[1]:
        candidate_2.append(candidate)

    if candidate == unique_candidates[2]:
        candidate_3.append(candidate)

    if candidate == unique_candidates[3]:
        candidate_4.append(candidate)              

#========
votes = len(candidates)

c1 = round(len(candidate_1)/len(candidates)*100)
c2 = round(len(candidate_2)/len(candidates)*100)
c3 = round(len(candidate_3)/len(candidates)*100)
c4 = round(len(candidate_4)/len(candidates)*100)

c1_1 = len(candidate_1) 
c2_1 = len(candidate_2) 
c3_1 = len(candidate_3) 
c4_1 = len(candidate_4) 

#======= winner is hard-coded, may need to update candidate index after running the percentages

winner = unique_candidates[0]

#==========
print('Election Results')
print('------------------------------------------------')
print('Total Votes: ' + str(votes))
print('------------------------------------------------')
print(str(unique_candidates[0]) + ': ' + str(c1) + '% ' + '('+ str(c1_1) +')')
print(str(unique_candidates[1]) + ': ' + str(c2) + '% ' + '('+ str(c2_1) +')')
print(str(unique_candidates[2]) + ': ' + str(c3) + '% ' + '('+ str(c3_1) +')')
print(str(unique_candidates[3]) + ': ' + str(c4) + '% ' + '('+ str(c4_1) +')')
print('------------------------------------------------')
print('Winner: ' + winner)
print('------------------------------------------------')

#==========

with open(outputfile, 'w') as datafile:
    writer = csv.writer(datafile)

    datafile.write('\n')
    datafile.write('Election Results\n')
    datafile.write('------------------------------------------------\n')
    datafile.write('Total Votes: ' + str(votes) + " \n")
    datafile.write('------------------------------------------------\n')
    datafile.write(str(unique_candidates[0]) + ': ' + str(c1) + '% ' + '('+ str(c1_1) +')' + " \n")
    datafile.write(str(unique_candidates[1]) + ': ' + str(c2) + '% ' + '('+ str(c2_1) +')' + " \n")
    datafile.write(str(unique_candidates[2]) + ': ' + str(c3) + '% ' + '('+ str(c3_1) +')' + " \n")
    datafile.write(str(unique_candidates[3]) + ': ' + str(c4) + '% ' + '('+ str(c4_1) +')' + " \n")
    datafile.write('------------------------------------------------\n')
    datafile.write('Winner: ' + winner + " \n")
    datafile.write('------------------------------------------------\n')
        