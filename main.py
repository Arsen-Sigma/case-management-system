import csv
import json


all_investigations = {}


def show_investigation():
   print(f"""
===============================================
RECORD DETAILS
===============================================

GENERAL INFORMATION
-----------------------------------------------
Record ID:      {investigations_2["id"]}
Record Name:    {investigations_2["title"]}

ASSIGNMENT
-----------------------------------------------
Assigned To:    {investigations_2["detective"]}

CASE DETAILS
-----------------------------------------------
Current Status: {investigations_2["status"]}
Priority Level: {investigations_2["priority"]} 
Category:       {investigations_2["category"]}

===============================================""")



while True:
    print("""
===============================================
CASE MANAGEMENT SYSTEM v1.0
===============================================

MAIN MENU
-----------------------------------------------
1.  Create Record
2.  View Records
3.  Find Record
4.  Edit Record
5.  Delete Record
6.  Statistics
7.  Export Records to CSV
8.  Export Records to TXT
9.  Save Records (JSON)
10. Load Records (JSON)
11. Exit

===============================================
""")
    try:
        selection_command = int(input("Select option: "))
    except ValueError:
        print("\n[!] Error: Please enter a valid number from 1 to 11.")
        continue

    
    if (selection_command >= 1) and (selection_command <= 11):
        if selection_command == 1: 
            print("""
===============================================
CREATE NEW RECORD
===============================================
""")
            
            ticket_id = input("ID: ")

            if ticket_id in all_investigations:
                print("""
===============================================
RECORD ALREADY EXISTS
===============================================

A record with this ID already exists.
Please enter a different Record ID.

===============================================""")
                continue

            title = input("Record Name: ")
            detective = input("Assigned To: ")
            status = input("Status: ")
            priority = input("Priority (High / Medium / Low): ").strip().capitalize()

            if (priority == "High") or (priority == "Medium") or (priority == "Low"):
                pass
            else:
                print("""
===============================================
INVALID PRIORITY
===============================================

Available values:

High
Medium
Low

===============================================""")
                continue

            ticket_type = input("Category (Fraud / Osint / Missing / Cyber / Financial / Network / Socials): ").strip().capitalize()

            if (ticket_type == "Fraud") or (ticket_type == "Osint") or (ticket_type == "Missing") or (ticket_type == "Cyber") or (ticket_type == "Financial") or (ticket_type == "Network") or (ticket_type == "Socials"):
                pass
            else:
                print("""
===============================================
INVALID CATEGORY
===============================================

Available values:

Fraud
Osint
Missing
Cyber
Financial
Network
Socials
===============================================""")
                continue
        
            all_investigations[ticket_id] = {
                "id": ticket_id,
                "title": title,
                "detective": detective,
                "status": status,
                "priority": priority,
                "category": ticket_type
            }

            print("""
===============================================
RECORD CREATED SUCCESSFULLY

The new record has been added.

===============================================""")
            
        elif selection_command == 2:
            print("""
===============================================
ALL RECORDS
===============================================""")
            if not all_investigations:
                print("""
===============================================
NO RECORDS FOUND

There are currently no records to display.

===============================================
""")
            else:
                for investigation_id, investigation in all_investigations.items():
                    print(f"""
-----------------------------------------------
Record ID:       {investigation_id}
Record Name:     {investigation["title"]}

Assigned To:     {investigation["detective"]}
Current Status:  {investigation["status"]}
Priority Level:  {investigation["priority"]}
Category:        {investigation["category"]}
-----------------------------------------------""")   
                print(f"\n===============================================\n\nTotal Records: {len(all_investigations)}\n")
                print("\n===============================================")
                    
        elif selection_command == 3:
            print("\n===============================================\nFIND RECORD\n===============================================\n")
            number_1 = input("Enter Record ID: ")

            if number_1 in all_investigations:
                investigations_1 = all_investigations[number_1]
                print(f"""
===============================================
RECORD DETAILS
===============================================

GENERAL INFORMATION
-----------------------------------------------
Record ID:      {investigations_1["id"]}
Record Name:    {investigations_1["title"]}

ASSIGNMENT
-----------------------------------------------
Assigned To:    {investigations_1["detective"]}

CASE DETAILS
-----------------------------------------------
Current Status: {investigations_1["status"]}
Priority Level: {investigations_1["priority"]}
Category:       {investigations_1["category"]}

===============================================""")
            else:
                print("""
===============================================
RECORD NOT FOUND
===============================================

No record with this ID exists.

===============================================
""")
        elif selection_command == 4:
            print("\n===============================================\nEDIT RECORD\n===============================================\n")
            number_2 = input("Enter Record ID: ")
            if number_2 in all_investigations:
                investigations_2 = all_investigations[number_2]
                show_investigation() 
                
                print("""
Select a field to edit:

-----------------------------------------------
1. Record Name
2. Assigned To
3. Current Status
4. Priority Level
5. Category
6. Cancel
-----------------------------------------------""")
                try:
                    ask = int(input("Select option (1-6): "))
                except ValueError:
                    print("\n[!] Error: Please enter a valid number from 1 to 6.")
                    continue

             
                if ask == 1:
                    change = input("Enter new Record Name: ")
                    investigations_2["title"] = change
                    show_investigation()
                elif ask == 2:
                    change = input("Enter new Assigned To: ")
                    investigations_2["detective"] = change
                    show_investigation()
                elif ask == 3:
                    change = input("Enter new Current Status: ")
                    investigations_2["status"] = change
                    show_investigation()
                elif ask == 4:
                    change = input("Enter new Priority Level: ").strip().capitalize()
                    if (change == "High") or (change == "Medium") or (change == "Low"):
                        investigations_2["priority"] = change
                        show_investigation()
                    else:
                        print("""
===============================================
INVALID PRIORITY
===============================================

Available values:

High
Medium
Low

===============================================""")
                        continue
                elif ask == 5:
                    change = input("Enter new Category: ").strip().capitalize()
                    if (change == "Fraud") or (change == "Osint") or (change == "Missing") or (change == "Cyber") or (change == "Financial") or (change == "Network") or (change == "Socials"):
                        investigations_2["category"] = change
                        show_investigation()
                    else:
                        print("""
===============================================
INVALID CATEGORY
===============================================

Available values:

Fraud
Osint
Missing
Cyber
Financial
Network
Socials

The record was not updated.

===============================================""")
                        continue
                elif ask == 6:  
                    continue
                else:
                    print("""
===============================================
INVALID SELECTION
===============================================

Please choose a number from 1 to 6.

===============================================""")   
            else:
                print("""
===============================================
RECORD NOT FOUND
===============================================

No record with this ID exists.

===============================================""")
        elif selection_command == 5:  
                print("""
===============================================
DELETE RECORD
===============================================
""")
                number_3 = input("Enter Record ID: ")
                if number_3 in all_investigations:
                    print("""
===============================================
RECORD DELETED
===============================================

The record has been deleted successfully.

===============================================""")
                    del all_investigations[number_3]
                else:
                    print("""
===============================================
RECORD NOT FOUND
===============================================

No record with this ID exists.
Nothing was deleted.

===============================================""")
        elif selection_command == 6:
            high_count = 0 
            medium_count = 0 
            low_count = 0 

            fraud_count = 0
            osint_count = 0
            missing_count = 0
            cyber_count = 0
            financial_count = 0
            network_count = 0
            socials_count = 0


            for investigations_3 in all_investigations.values():
                if investigations_3["priority"] == "High":
                    high_count += 1
                elif investigations_3["priority"] == "Medium":
                    medium_count += 1
                elif investigations_3["priority"] == "Low":
                    low_count += 1

            for investigations_3 in all_investigations.values():
                if investigations_3["category"] == "Fraud":
                    fraud_count += 1
                elif investigations_3["category"] == "Osint":
                    osint_count += 1
                elif investigations_3["category"] == "Missing":
                    missing_count += 1
                elif investigations_3["category"] == "Cyber":
                    cyber_count += 1
                elif investigations_3["category"] == "Financial":
                    financial_count += 1
                elif investigations_3["category"] == "Network":
                    network_count += 1
                elif investigations_3["category"] == "Socials":
                    socials_count += 1
 
            print(f"""
===============================================
STATISTICS
===============================================

GENERAL
-----------------------------------------------
Total Records:      {len(all_investigations)}

PRIORITY
-----------------------------------------------
High:               {high_count}
Medium:             {medium_count}
Low:                {low_count}
    
CATEGORY
-----------------------------------------------
Fraud:              {fraud_count}
OSINT:              {osint_count}
Missing:            {missing_count}
Cyber:              {cyber_count}
Financial:          {financial_count}  
Network:            {network_count}
Socials:            {socials_count}

===============================================""")   
        elif selection_command == 7:
            with open("records.csv", "w", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)    
                writer.writerow(["record_id", "record_name", "assigned_to", "status", "priority", "category"])
                for value in all_investigations.values():
                    writer.writerow([
                    value["id"],
                    value["title"],
                    value["detective"],
                    value["status"],
                    value["priority"],
                    value["category"]
                ])
            print("""
===============================================
EXPORT COMPLETED
===============================================

Records have been exported to:
records.csv

===============================================""")
        elif selection_command == 8: 
            with open("records.txt", "w", encoding="utf-8") as file: 
                file.write("""
===============================================
ALL RECORDS
===============================================
""")
                for value in all_investigations.values():
                    file.write(f"""                         
Record ID:    {value["id"]}
Record Name:  {value["title"]}
Assigned To:  {value["detective"]}
Status:       {value["status"]}
Priority:     {value["priority"]}
Category:     {value["category"]}
            
-----------------------------------------------
""")
                print("""
===============================================
EXPORT COMPLETED
===============================================

Records have been exported to:
records.txt

===============================================""")
        elif selection_command == 9:
            with open("save.json", "+w", encoding="utf-8") as file:
                json.dump(all_investigations, file, indent=4)
                print("""
===============================================
SAVE COMPLETED
===============================================

Records have been saved to:
save.json

===============================================""")
        elif selection_command == 10:
            with open("save.json", "r", encoding="utf-8") as file:
                user = json.load(file)
                all_investigations = user
                for use in user.values():
                    print(f"""               
Record ID:    {use["id"]}
Record Name:  {use["title"]}
Assigned To:  {use["detective"]}
Status:       {use["status"]}
Priority:     {use["priority"]}
Category:     {use["category"]}
""")

            print("""
===============================================
LOAD COMPLETED
===============================================

Records have been loaded successfully.

===============================================""")
        elif selection_command == 11:
            print("""
===============================================
CASE MANAGEMENT SYSTEM
===============================================

Closing system...

Remember:
Use "Save Records" before exiting if you want
to keep your records for the next session.

Session ended successfully.

===============================================""")
            break

    else:             
        print(f"""
===============================================
INVALID OPTION           
===============================================
            
You see numbers 1 through 11.
Here's what you wrote: {selection_command}.

===============================================
""")
