import os
import csv

# set path for file

csvfile_path=os.path.join("Resources","budget_data.csv")


#define stockmonth and pnlchnage
stockmonth=[]
pnl=[]
pnlchange=[]
 # open and read csv file
with open(csvfile_path,'r',encoding="utf") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header=next(csvreader)
    cnt=0
    prevval=0
    pnldiff=0
    #loop through the rows to calculate the profit and loss value
    for row in csvreader:
        stockmonth.append(row[0])
        pnl.append(int(row[1]))

    #find the profit and loss difference
        if cnt == 0:
            prevval=int(row[1])
            cnt = 1
        else:
            pnldiff=(int(row[1])) - prevval
            prevval=int(row[1])
        pnlchange.append(pnldiff)
    
  #calculating total months,profit and loss avg,profit and loss change,max and min values      
totmonths=len(stockmonth)
total=sum(pnl)
non_zero_preval=[float(v) for v in pnlchange if v != 0]
pnlavg=round(sum(non_zero_preval) / len(non_zero_preval),2)
pnlchange_list=zip(pnlchange,stockmonth)
max_value, max_month = max(list(pnlchange_list))
pnlchange_list1=zip(pnlchange,stockmonth)
min_value, min_month = min(list(pnlchange_list1))
 
 #set path for txtfile
txtfile_path=os.path.join("Analysis","pybank_output.txt")

#open text file
with open(txtfile_path,"w") as txtfile:

#assiging variable as txt_output
    txt_output= (
        f"Financial Analysis \n"
        f"------------------------------------------------------------\n"
        f"Total Months : {totmonths} \n"
        f"Total : ${total}\n"
        f"Average Change : ${pnlavg} \n"
        f"Greatest Increase in Profits:  {max_month} (${max_value})\n"
        f"Greatest Decrease in Profits:  {min_month} (${min_value})\n"
        f"------------------------------------------------------------\n")
    print(txt_output)
    txtfile.write(txt_output)





        
        
