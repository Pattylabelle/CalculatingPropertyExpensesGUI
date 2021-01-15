import webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def Compile_Click():
	
	box1_value = int
	box2_value = int
	box3_value = int
	box4_value = int
	box5_value = int
	box6_value = int
	box7_value = int
	box8_value = int
	box9_value = int
	
	box1 = entry_ProjectedMonthlyExpenses.get()
	box1_value = int(box1)
	
	box2 = entry_PurchasePrice.get()
	box2_value = int(box2)
	
	box3 = entry_AssessedHomeValue.get()
	box3_value = int(box3)
	
	box4 = entry_AssessedTotalValue.get()
	box4_value = int(box4)
	
	box5 = entry_MonthlyRentCharged.get()
	box5_value = int(box5)
	
	box6 = entry_Repairs.get()
	box6_value = int(box6)
	
	box7 = entry_SquareFootage.get()
	box7_value = int(box7)
	
	box8 = entry_AveragePricePerSquareFoot.get()
	box8_value = int(box8)
	
	box9 = entry_ProjectedApreciationPercent.get()
	box9_value = float(box9)

# formulas needed for calculating expenses---------------------------------------------------------------------------------
	
	Vacancy = (box1_value * Vacancy_percent)

	Closing_Costs = (.035 * box2_value)
	Closing_Costs = (Closing_Costs + 2000)
	
	Repairs_Maintenance = (box2_value * Repairs_Maintenance_Percent)
	Repairs_Maintenance = (Repairs_Maintenance/12)
	
	Home_to_Land_Value_ratio = (box3_value/box4_value)
	Depreciation_Value_Price = (box2_value * Home_to_Land_Value_ratio)

	
	Total_Monthly_Expenses = int(box1_value + Vacancy + Repairs_Maintenance)
	Cashflow = (box5_value - Total_Monthly_Expenses )
	Cashflow_Annual = (Cashflow * 12)
 	
	Downpayment = (box2_value * Downpayment_Percent )
 	
	Cash_on_Cash_Returned = (Downpayment + box6_value + Closing_Costs)
	Cash_on_Cash_Returned = (Cashflow_Annual / Cash_on_Cash_Returned)
 	
	
	Depreciation_Amount_Per_Year = (Depreciation_Value_Price / Depreciation_term)

	
	Total_Upfront_Costs = (Downpayment + Closing_Costs + box6_value)

	Loan_Amount = (box2_value - Downpayment)

	# formulas needed for calculating expenses---------------------------------------------------------------------------------	
	
	entry1 =(box7_value * box8_value)          #box7_value = Square Footage , box8_value = Square Footage Price
	entry_TopMarketPrice.delete(0, tk.END)
	entry_TopMarketPrice.insert(0, entry1)
	
	entry2 = (box2_value - Downpayment)    #box2_value = Total Price
	entry_LoanAmount.delete(0, tk.END)
	entry_LoanAmount.insert(0, entry2)
	
	entry3 = (Downpayment)    #entry3 = Loan down payment
	entry_LoanDownPayment.delete(0, tk.END)
	entry_LoanDownPayment.insert(0, entry3)
	
	entry4 = (Vacancy)
	entry_VacancyExpense.delete(0, tk.END)
	entry_VacancyExpense.insert(0, entry4)
	
	entry5 = (Repairs_Maintenance)
	entry_RepairsAndMaintenanceExpense.delete(0, tk.END)
	entry_RepairsAndMaintenanceExpense.insert(0, entry5)
	
	entry6 =  (box1_value + Vacancy + Repairs_Maintenance)  #box1_value = Monthly Expenses
	entry_TotalMonthlyExpenses.delete(0, tk.END)
	entry_TotalMonthlyExpenses.insert(0, entry6)
	
	entry7 = (box5_value - box1_value)    #box5_value = Rent Charged , box1_value = Monthly Expenses
	entry_MonthlyCashflow.delete(0, tk.END)
	entry_MonthlyCashflow.insert(0, entry7)
	
	entry8 = Depreciation_Value_Price
	entry_DepreciationValuePrice.delete(0, tk.END)
	entry_DepreciationValuePrice.insert(0, entry8)
	
	entry9 = Depreciation_Amount_Per_Year
	entry_DepreciationAmount.delete(0, tk.END)
	entry_DepreciationAmount.insert(0, entry9)
	
	entry10 = Home_to_Land_Value_ratio
	entry_HomeToLandValuePercent.delete(0, tk.END)
	entry_HomeToLandValuePercent.insert(0, entry10)
	
	entry11 = (box9_value + box7_value * box8_value)   #box9_value = Apreciation Percent , box7_value = Square Footage , box8_value = Square Footage Price 
	entry_ProjectedYearlyApreciation.delete(0, tk.END)
	entry_ProjectedYearlyApreciation.insert(0, entry11)
	
	entry12 =  (Cash_on_Cash_Returned)
	entry_CashOnCashReturn.delete(0, tk.END)
	entry_CashOnCashReturn.insert(0, entry12)
	
	entry13 = (Total_Upfront_Costs)
	entry_TotalUpfrontCosts.delete(0, tk.END)
	entry_TotalUpfrontCosts.insert(0, entry13)
	
	entry14 = (box7_value * box8_value - box2_value)   #box7_value = Square Footage , box8_value = Square Footage Price , box2_value = Total Price
	entry_PotentialUpside.delete(0, tk.END)
	entry_PotentialUpside.insert(0, entry14)
	
	return
	
	
def Calculate_Click():
	RepairCostTrue1=int
	RepairCostTrue2=int
	RepairCostTrue3=int
	RepairCostTrue4=int
	RepairCostTrue5=int
	RepairCostTrue6=int
	RepairCostTrue7=int

	RepairCost1 = int
	RepairCost2 = int
	RepairCost3 = int
	RepairCost4 = int
	RepairCost5 = int
	RepairCost6 = int
	RepairCost7 = int
	
	RepairCost1 = 0
	RepairCost2 = 0
	RepairCost3 = 0
	RepairCost4 = 0
	RepairCost5 = 0
	RepairCost6 = 0
	RepairCost7 = 0		
	
	RepairCostTrue1 = entry_RepairCost1.get()	
	if RepairCostTrue1 == "$":
		pass
	
	else:
		RepairCost1 = entry_RepairCost1.get()
		RepairCost1 = RepairCost1.replace("$" , "")
		RepairCost1 = int(RepairCost1)
			
	RepairCostTrue2 = entry_RepairCost2.get()
	if RepairCostTrue2 == "$":
	    pass
		
	else:
		RepairCost2 = entry_RepairCost2.get()
		RepairCost2 = RepairCost2.replace("$" , "")
		RepairCost2 = int(RepairCost2)
	
	RepairCostTrue3 = entry_RepairCost3.get()
	if RepairCostTrue3 == "$":
		pass	
	
	else:
		RepairCost3 = entry_RepairCost3.get()
		RepairCost3 = RepairCost3.replace("$" , "")
		RepairCost3 = int(RepairCost3)
	
	RepairCostTrue4 = entry_RepairCost4.get()
	if RepairCostTrue4 == "$":
		pass	
	
	else:
		RepairCost4 = entry_RepairCost4.get()
		RepairCost4 = RepairCost4.replace("$" , "")
		RepairCost4 = int(RepairCost4)
	
	RepairCostTrue5 = entry_RepairCost5.get()
	if RepairCostTrue5 == "$":
		pass	
	
	else:
		RepairCost5 = entry_RepairCost5.get()
		RepairCost5 = RepairCost5.replace("$" , "")
		RepairCost5 = int(RepairCost5)
	
	RepairCostTrue6 = entry_RepairCost6.get()
	if RepairCostTrue6 == "$":
		pass	
	
	else:
		RepairCost6 = entry_RepairCost6.get()
		RepairCost6 = RepairCost6.replace("$" , "")
		RepairCost6 = int(RepairCost6)
	
	RepairCostTrue7 = entry_RepairCost7.get()	
	if RepairCostTrue7 == "$":
		pass	
	
	else:
		RepairCost7 = entry_RepairCost7.get()
		RepairCost7 = RepairCost7.replace("$" , "")
		RepairCost7 = int(RepairCost7)
	
	Repair_Total = int(RepairCost1 + RepairCost2 + RepairCost3 + RepairCost4 + RepairCost5 + RepairCost6 + RepairCost7)
	entry_RepairCostTotal.delete(0, tk.END)
	entry_RepairCostTotal.insert(0, Repair_Total)
	entry_RepairCostTotal.insert(0, "$")
	
	
	return Repair_Total

def SendIt_Click():
	 Repair_Totaled = entry_RepairCostTotal.get()	 	
	 if Repair_Totaled == "$":
	 	messagebox.showerror("Error","No Values Have Been Calculated")
		
	 else:
		  Repair_Totaled = entry_RepairCostTotal.get()
		  Repair_Totaled = Repair_Totaled.replace("$" , "")
		  Repair_Totaled = int(Repair_Totaled)
		  Entry_Repair = entry_Repairs.get()
		  Entry_Repair = int(Entry_Repair)
		  
		  #Repair_Total1 = Repair_Total
		  #Repair_Total1 = int(Repair_Total)
		  Entry_Repair_Total = (Entry_Repair + Repair_Totaled)
		  Entry_Repair_Total = int(Entry_Repair_Total)
		  
		 
		 
		  entry_Repairs.delete(0, tk.END)
		  entry_Repairs.insert(0, Entry_Repair_Total)
		  entry_Repairs.insert(0, "$")
		 
	 return
	 
def Get_Browser():	 
	 webbrowser.open("https://www.homedepot.com/" , new=2, autoraise=True)
	 return


#creates Tkinter window
window = tk.Tk() 
#set window size
window.geometry("1100x800")
#prevent window resize
window.resizable(False, False)

# defined variables-------‐---‐----‐-------‐-‐------------------------------------------------------------------------------------------

entry1 = tk.IntVar()
entry2 = tk.IntVar()
entry3 = tk.IntVar()
entry4 = tk.IntVar()
entry5 = tk.IntVar()
entry6 = tk.IntVar()
entry7 = tk.IntVar()
entry8 = tk.IntVar()
entry9 = tk.IntVar()
entry10 = tk.IntVar()
entry11 = tk.IntVar()
entry12 = tk.IntVar()
entry13 = tk.IntVar()
entry14 = tk.IntVar()

Top_Market_Price = int
Square_Footage = int
Square_Footage_Price = int
Total_price = int 
Downpayment = int
Downpayment_Percent = .2
Closing_Costs = int
Total_Upfront_Costs = int
Loan_Amount = int
Monthly_Expenses = int

Vacancy = int 
Vacancy_percent = int
Vacancy_percent = .1

Repairs_Maintenance = int

Repairs_Maintenance_Percent = .03
Repairs = int

Rent_Charged = int
True_or_False = bool

Assessed_Value_Land = int
Assessed_Value_Home = int
Assessed_Value_Total = int
Home_to_Land_Value_ratio = int


Depreciation_term = 27.5
	
Depreciation_Value_Price = int
Depreciation_Amount_Per_Year = int

Cash_on_Cash_Returned = int
	
Cashflow = int
Cashflow_Annual = int

Apreciation_Percent = int

Total_Monthly_Expenses = int		

Repair_Total = int


# defined variables-------‐---‐----‐-------‐-‐------------------------------------------------------------------------------------------

# variables storing single catalog information-------‐---‐----‐-------‐-‐------------------------------------------------------------------------------------------

Interior_Paint_Walls = int 
Interior_Paint_Ceiling = int
Plywood = int
Laminate_Flooring = int
Tile_Flooring = int  # (includes costs for mortar, tile, grout, and 10% for things possible missed)
#Materials = ["Nails", ""]
Cabinets = int
Counters = int
Toilet = int
Shower_Insert = int
Stove = int
Sink = int
Microwave = int
Refrigerator = int
Dishwasher = int



#creates tabs, one for main calculations and one for repairs during walkthroughs

tabControl = ttk.Notebook(window)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text = "Calculations")
tabControl.add(tab2, text = "Repairs")
tabControl.add(tab3, text = "Equations For Footage")
tabControl.pack(expand = 1, fill = "both")

#creates Label(not editable, display purposes) to be put onto the Window, also sets a backround and foreground colors and width and height parameters
greeting = tk.Label(text = "Calculating Property Expenses", width = 29 , height = 1).place(x=800, y=0)
greeting = tk.Label(master = tab1 , text = "INPUTS:", width = 7 , height = 1, borderwidth=2, relief = "solid").place(x=430,y=20)
greeting = tk.Label(master = tab1, text = "OUTPUTS:", width = 9 , height = 1, borderwidth=2, relief = "solid").place(x=1755,y=20)

#creates labels and entries for user input
label_PurchasePrice = tk.Label(master = tab1, text="Purchase Price:").place(x=170 , y=100)
entry_PurchasePrice = tk.Entry(master = tab1, width = 20)
entry_PurchasePrice.place(x=355, y= 100)


label_AssessedTotalValue = tk.Label(master = tab1, text="Assessed Total Value:").place(x=98, y=150)
entry_AssessedTotalValue = tk.Entry(master = tab1, width = 20)
entry_AssessedTotalValue.place(x=355, y=150)

label_AssessedHomeValue = tk.Label(master = tab1, text="Assessed Home Value:").place(x=90, y=200)
entry_AssessedHomeValue = tk.Entry(master = tab1, width = 20)
entry_AssessedHomeValue.place(x=355, y=200)

label_SquareFootage = tk.Label(master = tab1, text="Square Footage:").place(x=162, y=250)
entry_SquareFootage = tk.Entry(master = tab1, width = 20)
entry_SquareFootage.place(x=355, y=250)

label_AveragePricerPerSquareFoot = tk.Label(master = tab1, text="Average Price Per Square Foot:").place(x=0, y=300)
entry_AveragePricePerSquareFoot = tk.Entry(master = tab1, width = 20)
entry_AveragePricePerSquareFoot.place(x=355, y=300)

label_MonthlyRentCharged = tk.Label(master = tab1, text="Monthly Rent Charged:").place(x=90, y= 350)
entry_MonthlyRentCharged = tk.Entry(master = tab1, width = 20)
entry_MonthlyRentCharged.place(x=355, y=350)

label_ProjectedMonthlyExpenses = tk.Label(master = tab1, text="Projected Monthly Expenses:").place(x=20, y=400)
entry_ProjectedMonthlyExpenses = tk.Entry(master = tab1, width = 20)
entry_ProjectedMonthlyExpenses.place(x=355, y=400)

label_ProjectedApreciationPercent = tk.Label(master = tab1, text="Projected Apreciation Percent:").place(x=5, y=450)
entry_ProjectedApreciationPercent = tk.Entry(master = tab1, width = 20)
entry_ProjectedApreciationPercent.place(x=355, y=450)

label_Repairs = tk.Label(master = tab1, text="Cost of Repairs Needed Prior:").place(x=15, y=500)
entry_Repairs = tk.Entry(master = tab1, width = 20)
entry_Repairs.place(x=355, y=500)
entry_Repairs.delete(0, tk.END)
entry_Repairs.insert(0,0)


#creates labels and entries for outputs

label_TopMarketPrice = tk.Label(master = tab1, text="Top Market Price:").place(x=1490 , y=100)
entry_TopMarketPrice = tk.Entry(master = tab1, width = 20, textvariable = entry1)
entry_TopMarketPrice.place(x=1700, y= 100)

label_LoanAmount = tk.Label(master = tab1, text="Loan Amount:").place(x=1530, y=150)
entry_LoanAmount = tk.Entry(master = tab1, width = 20, textvariable = entry2)
entry_LoanAmount.place(x=1700, y=150)

label_LoanDownPayment = tk.Label(master = tab1, text="Loan Down Payment:").place(x=1450, y=200)
entry_LoanDownPayment = tk.Entry(master = tab1, width = 20, textvariable = entry3)
entry_LoanDownPayment.place(x=1700, y=200)

label_VacancyExpense = tk.Label(master = tab1, text="Vacancy Expense:").place(x=1485, y=250)
entry_VacancyExpense = tk.Entry(master = tab1, width = 20, textvariable = entry4)
entry_VacancyExpense.place(x=1700, y=250)

label_RepairsAndMaintenanceExpense= tk.Label(master = tab1, text="Repairs and Maintenance Expense:").place(x=1300, y=300)
entry_RepairsAndMaintenanceExpense = tk.Entry(master = tab1, width = 20, textvariable = entry5)
entry_RepairsAndMaintenanceExpense.place(x=1700, y=300)

label_TotalMonthlyExpenses = tk.Label(master = tab1, text="Total Monthly Expenses:").place(x=1413, y= 350)
entry_TotalMonthlyExpenses = tk.Entry(master = tab1, width = 20, textvariable = entry6)
entry_TotalMonthlyExpenses.place(x=1700, y=350)

label_MonthlyCashflow = tk.Label(master = tab1, text="Monthly Cashflow:").place(x=1480, y= 400)
entry_MonthlyCashflow = tk.Entry(master = tab1, width = 20, textvariable = entry7)
entry_MonthlyCashflow.place(x=1700, y=400)

label_DepreciationValuePrice = tk.Label(master = tab1, text="Depreciation Value Price:").place(x=1413, y= 450)
entry_DepreciationValuePrice = tk.Entry(master = tab1, width = 20, textvariable = entry8)
entry_DepreciationValuePrice.place(x=1700, y=450)

label_DepreciationAmount = tk.Label(master = tab1, text="Depreciation Amount Per Year:").place(x=1350, y= 500)
entry_DepreciationAmount = tk.Entry(master = tab1, width = 20, textvariable = entry9)
entry_DepreciationAmount.place(x=1700, y=500)

label_HomeToLandValuePercent = tk.Label(master = tab1, text="Home To Land Value Percent:").place(x=1360, y= 550)
entry_HomeToLandValuePercent = tk.Entry(master = tab1, width = 20, textvariable = entry10)
entry_HomeToLandValuePercent.place(x=1700, y=550)

label_ProjectedYearlyApreciation = tk.Label(master = tab1, text="Projected Yearly Apreciation:").place(x=1370, y= 600)
entry_ProjectedYearlyApreciation = tk.Entry(master = tab1, width = 20, textvariable = entry11)
entry_ProjectedYearlyApreciation.place(x=1700, y=600)

label_CashOnCashReturn = tk.Label(master = tab1, text="Cash On Cash Return:").place(x=1450, y= 650)
entry_CashOnCashReturn = tk.Entry(master = tab1, width = 20, textvariable = entry12)
entry_CashOnCashReturn.place(x=1700, y=650)

label_TotalUpfrontCosts = tk.Label(master = tab1, text="Total Upfront Costs:").place(x=1460, y= 700)
entry_TotalUpfrontCosts = tk.Entry(master = tab1, width = 20, textvariable = entry13)
entry_TotalUpfrontCosts.place(x=1700, y=700)

label_PotentialUpside = tk.Label(master = tab1, text="Potential Upside:").place(x=1500, y= 750)
entry_PotentialUpside = tk.Entry(master = tab1, width = 20, textvariable = entry14)
entry_PotentialUpside.place(x=1700, y=750)

#creates a button to compile numbers inputed and give outputs
button = tk.Button(master = tab1, text = "Compile" , width = 7 , height = 2 , borderwidth=2 , relief="raised" , command = Compile_Click).place(x=920, y=980)




#code used for Repair tab ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Category_list = ( "Electrical" , "Plumbing" , "Structural" , "Cosmetic" , "Appliances" , "Other")
Location_list = ("Land", "Bedroom", "Kitchen", "Living Room" , "Bathroom", "Exterior", "Interior" , "Other")



#code used for creating entries for Descriptions
label_Repair = tk.Label(master= tab2, text = "Quick Description").place(x=400 , y=50)

label_Repair1 = tk.Label(master = tab2 , text="Repair #1:").place(x=10 , y=100)
entry_Repair1 = tk.Entry(master = tab2, width = 54)
entry_Repair1.place(x=135, y= 100)

label_Repair2 = tk.Label(master = tab2 , text="Repair #2:").place(x=10 , y=150)
entry_Repair2 = tk.Entry(master = tab2, width = 54)
entry_Repair2.place(x=135, y= 150)

label_Repair3 = tk.Label(master = tab2 , text="Repair #3:").place(x=10 , y=200)
entry_Repair3 = tk.Entry(master = tab2, width = 54)
entry_Repair3.place(x=135, y= 200)

label_Repair4 = tk.Label(master = tab2 , text="Repair #4:").place(x=10 , y=250)
entry_Repair4 = tk.Entry(master = tab2, width = 54)
entry_Repair4.place(x=135, y= 250)

label_Repair5 = tk.Label(master = tab2 , text="Repair #5:").place(x=10 , y=300)
entry_Repair5 = tk.Entry(master = tab2, width = 54)
entry_Repair5.place(x=135, y= 300)

label_Repair6 = tk.Label(master = tab2 , text="Repair #6:").place(x=10 , y=350)
entry_Repair6 = tk.Entry(master = tab2, width = 54)
entry_Repair6.place(x=135, y= 350)

label_Repair7 = tk.Label(master = tab2 , text="Repair #7:").place(x=10 , y=400)
entry_Repair7 = tk.Entry(master = tab2, width = 54)
entry_Repair7.place(x=135, y= 400)

#creates a combobox to be used for locations
label_Location = tk.Label(master= tab2, text = "Location").place(x=990 , y=50)

Location1 = tk.StringVar()
LocationPicked1 = ttk.Combobox(master = tab2, width = 15, textvariable = Location1)
LocationPicked1[ 'values' ] = Location_list
LocationPicked1.place(x=930 , y=100)
LocationPicked1.current()

Location2 = tk.StringVar()
LocationPicked2 = ttk.Combobox(master = tab2, width = 15, textvariable = Location2)
LocationPicked2[ 'values' ] = Location_list
LocationPicked2.place(x=930 , y=150)
LocationPicked2.current()

Location3 = tk.StringVar()
LocationPicked3 = ttk.Combobox(master = tab2, width = 15, textvariable = Location3)
LocationPicked3[ 'values' ] = Location_list
LocationPicked3.place(x=930 , y=200)
LocationPicked3.current()

Location4 = tk.StringVar()
LocationPicked4 = ttk.Combobox(master = tab2, width = 15, textvariable = Location4)
LocationPicked4[ 'values' ] = Location_list
LocationPicked4.place(x=930 , y=250)
LocationPicked4.current()

Location5 = tk.StringVar()
LocationPicked5 = ttk.Combobox(master = tab2, width = 15, textvariable = Location5)
LocationPicked5[ 'values' ] = Location_list
LocationPicked5.place(x=930 , y=300)
LocationPicked5.current()

Location6 = tk.StringVar()
LocationPicked6 = ttk.Combobox(master = tab2, width = 15, textvariable = Location6)
LocationPicked6[ 'values' ] = Location_list
LocationPicked6.place(x=930 , y=350)
LocationPicked6.current()

Location7 = tk.StringVar()
LocationPicked7 = ttk.Combobox(master = tab2, width = 15, textvariable = Location7)
LocationPicked7[ 'values' ] = Location_list
LocationPicked7.place(x=930 , y=400)
LocationPicked7.current()

#creates a combobox to be used for locations

label_Category = tk.Label(master= tab2, text = "Category").place(x=1250 , y=50)

Category1 = tk.StringVar()
CategoryPicked1 = ttk.Combobox(master = tab2, width = 15, textvariable = Category1)
CategoryPicked1['values'] = Category_list
CategoryPicked1.place(x=1200 , y=100)
CategoryPicked1.current()

Category2 = tk.StringVar()
CategoryPicked2 = ttk.Combobox(master = tab2, width = 15, textvariable = Category2)
CategoryPicked2['values'] = Category_list
CategoryPicked2.place(x=1200 , y=150)
CategoryPicked2.current()

Category3 = tk.StringVar()
CategoryPicked3 = ttk.Combobox(master = tab2, width = 15, textvariable = Category3)
CategoryPicked3['values'] = Category_list
CategoryPicked3.place(x=1200 , y=200)
CategoryPicked3.current()

Category4 = tk.StringVar()
CategoryPicked4 = ttk.Combobox(master = tab2, width = 15, textvariable = Category4)
CategoryPicked4['values'] = Category_list
CategoryPicked4.place(x=1200 , y=250)
CategoryPicked4.current()

Category5 = tk.StringVar()
CategoryPicked5 = ttk.Combobox(master = tab2, width = 15, textvariable = Category5)
CategoryPicked5['values'] = Category_list
CategoryPicked5.place(x=1200 , y=300)
CategoryPicked5.current()

Category6 = tk.StringVar()
CategoryPicked6 = ttk.Combobox(master = tab2, width = 15, textvariable = Category6)
CategoryPicked6['values'] = Category_list
CategoryPicked6.place(x=1200 , y=350)
CategoryPicked6.current()

Category7 = tk.StringVar()
CategoryPicked7 = ttk.Combobox(master = tab2, width = 15, textvariable = Category7)
CategoryPicked7['values'] = Category_list
CategoryPicked7.place(x=1200 , y=400)
CategoryPicked7.current()

#code used for creating inputs for Repair costs
label_RepairCost = tk.Label(master= tab2, text = "Costs").place(x=1530 , y=50)

entry_RepairCost1 = tk.Entry(master = tab2, width = 15)
entry_RepairCost1.insert( 0, "$")
entry_RepairCost1.place(x=1465, y= 100)

entry_RepairCost2 = tk.Entry(master = tab2, width = 15)
entry_RepairCost2.insert( 0, "$")
entry_RepairCost2.place(x=1465, y= 150)

entry_RepairCost3 = tk.Entry(master = tab2, width = 15)
entry_RepairCost3.insert( 0, "$")
entry_RepairCost3.place(x=1465, y= 200)

entry_RepairCost4 = tk.Entry(master = tab2, width = 15)
entry_RepairCost4.insert( 0, "$")
entry_RepairCost4.place(x=1465, y= 250)

entry_RepairCost5 = tk.Entry(master = tab2, width = 15)
entry_RepairCost5.insert( 0, "$")
entry_RepairCost5.place(x=1465, y= 300)

entry_RepairCost6 = tk.Entry(master = tab2, width = 15)
entry_RepairCost6.insert( 0, "$")
entry_RepairCost6.place(x=1465, y= 350)

entry_RepairCost7 = tk.Entry(master = tab2, width = 15)
entry_RepairCost7.insert( 0, "$")
entry_RepairCost7.place(x=1465, y= 400)

#creates output box for total calculated repairs on Repairs tab
label_RepairCostTotal = tk.Label(master = tab2, text =  "Total Costs").place(x=1500, y=500)
entry_RepairCostTotal = tk.Entry(master = tab2, width = 15)
entry_RepairCostTotal.insert( 0, "$")
entry_RepairCostTotal.place(x=1465, y = 550)



#creates a button to compute numbers on repairs page

button = tk.Button(master = tab2, text = "Calculate" , width = 10 , height = 2 , borderwidth=2 , relief="raised" , command = Calculate_Click).place(x=770, y=980)

#creates a button to send calculated numbers to the main page

button = tk.Button(master = tab2, text = "Send It" , width = 10 , height = 2 , borderwidth=2 , relief="raised" , command = SendIt_Click).place(x=1030, y=980)


#code used for the Equations For Footage tab--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 

Type_list = ( "Walls" , "Floors")
Selection_list = ( "Total" , "Input (Custom)")

#code used for creating entries for Descriptions
#label_Equations = tk.Label(master= tab3, text = "Quick Description").place(x=490 , y=50)

label_Equation_Total_Square_Footage = tk.Label(master = tab3 , text="Total Square Footage:").place(x=10 , y=50)
entry_Equation_Total_Square_Footage = tk.Entry(master = tab3, width = 10)
entry_Equation_Total_Square_Footage.place(x=300, y= 50)

label_Equation_Total_Linear_Footage = tk.Label(master = tab3 , text="Total Linear Footage:").place(x=10 , y=100)
entry_Equation_Total_Linear_Footage = tk.Entry(master = tab3, width = 10)
entry_Equation_Total_Linear_Footage.place(x=300, y= 100)

label_Equation_Square_Footage_Calculate = tk.Label(master = tab3 , text="Square Footage To Calculate:").place(x=10 , y=200)
#entry_Equation_Square_Footage_Calculate = tk.Entry(master = tab3, width = 10)
#entry_Equation_Square_Footage_Calculate.place(x=350, y= 200)

label_Equation_Total_Width = tk.Label(master = tab3 , text="Category").place(x=560 , y=160)
Equation_Total_Width = tk.StringVar()
Equation_Total_Width_Picked = ttk.Combobox(master = tab3, width = 8, textvariable = Equation_Total_Width)
Equation_Total_Width_Picked['values'] = Type_list
Equation_Total_Width_Picked.place(x=550 , y=200)
Equation_Total_Width_Picked.current()


label_Equation_Total_Width = tk.Label(master = tab3 , text="Total \n Width (Feet):").place(x=700 , y=130)
entry_Equation_Total_Width = tk.Entry(master = tab3, width = 10)
entry_Equation_Total_Width.place(x=700, y= 200)

label_Equation_Total_Length = tk.Label(master = tab3 , text="Total \n Length (Feet):").place(x=10 , y=300)
#entry_Equation_Total_Length = tk.Entry(master = tab3, width = 54)
#entry_Equation_Total_Length.place(x=235, y= 300)

label_Equation_Total_Calculated_Square_Footage = tk.Label(master = tab3 , text="Total \n Calculated Square Footage:").place(x=10 , y=350)
#entry_Equation_Total_Calculated_Square_Footage = tk.Entry(master = tab3, width = 54)
#entry_Equation_Total_Calculated_Square_Footage.place(x=235, y= 350)

label_Equation_Equation_Price_Per_Square_Foot = tk.Label(master = tab3 , text="Price Per Square Foot:").place(x=10 , y=400)
#entry_Equation_Equation_Price_Per_Square_Foot = tk.Entry(master = tab3, width = 54)
#entry_Equation_Equation_Price_Per_Square_Foot.place(x=235, y= 400)


window.mainloop()