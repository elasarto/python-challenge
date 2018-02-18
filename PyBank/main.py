import os
import csv

budgets = ['1', '2']

for budget in budgets:

    budgetfile1 = os.path.join('..', 'PyBank', 'raw_data', 'budget_data_' + budgets[0] + '.csv')
    outputbudgetfile = os.path.join('..', 'PyBank', 'output_data', 'budget_data_' + budgets[0] + '.txt')
        
    total_months = []
    total_revenue = []
    avg_change = []

    with open(budgetfile1, newline='') as budgetdata1:
        csvreader = csv.reader(budgetdata1, delimiter=',')
        next(csvreader, None)

        for row in csvreader:
           
            total_months.append(row[0]) 
            total_revenue.append(float(row[1]))

    for i in range(len(total_revenue)-1):
            avgc = (float(total_revenue[i+1]))-(float(total_revenue[i]))
            avg_change.append(avgc)

#========== print average change index to input into final month analysis

#print(avg_change.index(max(average_change)))
#print(avg_change.index(min(average_change)))

#===============            
months = len(total_months)
revenue = round(sum(total_revenue))
rev_formatted = '${:,.2f}'.format(revenue)
change = round((total_revenue[0] - total_revenue[-1])/len(total_revenue), 2)
change_formatted = '${:,.2f}'.format(change)
minimum = round(min(avg_change))
min_formatted = '${:,.2f}'.format(minimum)
maximum = round(max(avg_change))
max_formatted = '${:,.2f}'.format(maximum)

print('Financial Analysis')
print('------------------------------------------------')
print('Total Months: ' + str(months))
print('Total Revenue: ' + str(rev_formatted))
print('Average Revenue Change: ' + str(change_formatted))
print('Greatest Increase in Revenue: ' + str(total_months[39]) + " " + str(max_formatted))
print('Greatest Decrease in Revenue: ' + str(total_months[21]) + " " + str(min_formatted))

with open(outputbudgetfile, 'w') as datafile:

    datafile.write('\n')
    datafile.write("Financial Analysis\n")
    datafile.write("------------------------------------------------\n")
    datafile.write("Total Months: " + str(months) + " \n")
    datafile.write("Total Revenue: " + str(rev_formatted) + " \n")
    datafile.write("Average Revenue Change: " + str(change_formatted) + " \n")
    datafile.write("Greatest Increase in Revenue: " + str(total_months[39]) + " " + str(max_formatted) + " \n")
    datafile.write("Greatest Decrease in Revenue: " + str(total_months[21]) + " " + str(min_formatted) + " \n")
   
           
