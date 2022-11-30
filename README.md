# dbms_project
# PROJECT TITLE:

CRIME DATA MANAGEMENT SYSTEM

# DESCRIPTION OF PROJECT:

The project has five tables
- Usertable
- crime
- criminal
- fir
- fir_backup

Usertable stores the username and password 
crime table contains the crime_id,crime_type,crime_date and crime_place.
criminal table contains crime_id,criminal_id,past_crimes,jail_name,criminal_name.
fir table contains fir_id,crime_id,fir_writer,fir_description,date_of_fir.
fir_backup is same as fir that stores the fir information as backup if we delete it.


# FUNCTIONALITIES OF THE PROJECT

The Project has 
`
Login page
`

After logging in succesfully,
if Profiles category is choosen,it shows the usernames of the people that has logged in.

We have to chose the category as cop to 
'''sh
Add crime Details
View crime Details
Update Crime Details
Delete crime Details
'''


Add crime details
- We can add crime , criminal and fir details individually

View crime details
- In this section the input data is represented and we can check the delay between the crime date and date of fir by selecting the crime id of the case 
- If the fir is entered before the crime has been comitted , warning message will be shown else the delay of fir is hown

Update Crime details
- we can update the criminal details here and the changes can be seen below the Update button

Delete Crime details
- Fir with the selected crime id can be deleted 
- The deleted fir is stored in the fir_backup table by using trigger





