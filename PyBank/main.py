# Import required modules / libraries
import os
import csv

# Get the data from the resource file
budget_data = os.path.join('.', 'Resources', 'budget_data.csv')

# Define the months field & profit / loss
TotalMonths = 0
TotalProfitLoss = 0

# Dollar amount from data
DollarAmount = 0

# Define the Date list
Dates = []
ProfitLoss = []
with open(budget_data, "r") as BudgetFile:
    BudgetReader = csv.reader(BudgetFile, delimiter = ",")

    # Header Row   
    ColumnHeaders = next(BudgetReader)
    # Save the column numbers
    ColumnNumbers = range(len(ColumnHeaders))



    # Read the first row to set as defaults
    FirstDataRow = next(BudgetReader)
    Date = FirstDataRow[0]
    RowAmount = int(FirstDataRow[1])
    TotalMonths +=1
    TotalProfitLoss+= RowAmount
    PreviousDollarAmount=RowAmount

    # Setting up a loop for the rest of the data rows
    for row in  BudgetReader:
            Date = row[0]
            RowAmount = int(row[1])
            Dates.append(Date)

            # Calculate change, then list changes, Increment months, and net amount Profit/loss
            DollarChange = RowAmount-PreviousDollarAmount
            ProfitLoss.append(DollarChange)
            PreviousDollarAmount = RowAmount
            TotalMonths +=1
            TotalProfitLoss = TotalProfitLoss + RowAmount

    # identify the greatest increase in profit
    GreatestProfitLossIncrease = max(ProfitLoss)
    GreatestProfitLossIncreasef = "${:,.2f}".format(GreatestProfitLossIncrease)
    GreatestProfitLossIndex = ProfitLoss.index(GreatestProfitLossIncrease)
    GreatestProfitLossDate = Dates[GreatestProfitLossIndex]

    # Identify the greatest Decrease in profit
    GreatestProfitLossDecrease = min(ProfitLoss)
    GreatestProfitLossDecreaseIndex = ProfitLoss.index(GreatestProfitLossDecrease)
    GreatestProfitLossDecreaseDate = Dates[GreatestProfitLossIndex]

    # AVG Delta in Profit / loss between months (entire period)
    AverageChange = sum(ProfitLoss)/len(ProfitLoss)
    AverageChangef = "${:,.2f}".format(AverageChange)


# Print Analysis results
print("Financial Analysis")
print("--------------------")
print(f"Total Months: {str(TotalMonths)}")
print(f"Total: ${str(TotalProfitLoss)}")

# Print f average change
print(f"Average Change: {AverageChangef}")
print(f"Greatest Increase in Profits: {GreatestProfitLossDate} {GreatestProfitLossIncreasef}")
print(f"Greatest Decrease in Profits: {GreatestProfitLossDecreaseDate} (${str(GreatestProfitLossDecrease)}) ")

# Put Analysis summary into a text file
outputpath = os.path.join(".", "analysis", "results.txt")
output = open(outputpath, "w")
output.write("Financial Analysis\n")
output.write("--------------------\n")
output.write(str(f"Total Months: {str(TotalMonths)}\n"))
output.write(str(f"Total: ${str(TotalProfitLoss)}\n"))
output.write(str(f"Average Change: {AverageChangef}\n"))
output.write(str(f"Greatest Increase in Profits: {GreatestProfitLossDate} (${str(GreatestProfitLossIncrease)})\n"))
output.write(str(f"Greatest Decrease in Profits: {GreatestProfitLossDecrease} (${str(GreatestProfitLossDecrease)})\n"))
