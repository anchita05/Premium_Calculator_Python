This is a project I took up for CS (CBSE) when I was in 12th.
This is basically an insurance premium calculator, that calculates the premium for your
overseas travel journey with preloaded and user-entered data.

Prerequisites

    1) A database already created on your sql server (Ex: here I used project2022)
    2) A table customer in the database with following names and constraints:
       name varchar(20),
       phno varchar(10),
       dest varchar(50),
       address varchar(50),
       days int(3),
       age int(2),
       plan1 varchar(50),
       premium varchar(20)

The first file uploaded (database_tables) would use the csv files to load the required data into your
database (use rates1 for premium50 table, rates2 for premium100 table and rates3 for premium250 table).

The other file has the code for premium calculator. It was made using Python, SQL and TkInter.
It has 3 main parts for user that he may choose according to his need- 

a)Calculator: to calculate their premium

b)Update: to update their details in our database

c)Delete: to delete their details from our database


REFERENCE OUTPUTS:

![Screenshot 2024-11-12 225532](https://github.com/user-attachments/assets/05027ae1-e9ef-4aa6-8291-36485ef63c1b)

![image](https://github.com/user-attachments/assets/481bbce1-238a-4607-88ff-164a6355f493)

![image](https://github.com/user-attachments/assets/5dd1635b-b0ad-4806-a417-f9603d2969d9)

![image](https://github.com/user-attachments/assets/5d970d13-be5a-4750-b52e-34386e5cf493)
