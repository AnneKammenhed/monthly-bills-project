<h1>Welcome to the monthly bills app!</h1>

<h2>Background</h2>  
This is an app that calculates the cost for a small nursing home and returns the sum and an average from the last six months. It is portfolio project 3 Python Essentials.  

It is built on the Code Institute student template abd the code i placed in the `run.py` file.

There is an API to google sheets and the dependency is placed in the `requirements.txt` file.

<h2>Content</h2>    
The app collects three types of data from user:
<ul>
<li>Costs linked to premises (e.g. rent, heating) is called rent in this app</li>
<li>Number of employees</li>
<li>Phone cost for this month</li>
</ul>

First of all the app checks if the data input is valid and prints an error-message if not and return to beginning. The input values have to be integers and an automated message apears if the user writes a word. Also the input values for rent and phone have to be over certain amount. And the cost for employees is limited to 10 000 000 SEK.

Before moving the numbers to the spreadsheet, the number of employees is multipied by 40 000 SEK to get a sum of salaries. This is an average yearly cost of an employee of 500 000 SEK divided into 12 to get the average monthly cost. 

The rent, salary and telephone costs are added to the bills worksheet.

The sum is calculated and returned to user. The sum is added to sum-worksheet.

A six month average is calculated returned to user. The average is added to worksheet.

<h2>Testing and bugs</h2> 
Over the development of the app, different solutions have been tested to solve the task. I built out smaller parts of the code in replit. One of the trickier parts was to get the average from the sums and return that number to the last worksheet.

I chose the built in function to ask for integers in the input. Even though the int()-question is in the "while" loop, the app does not loop back to ask for the input again if I answer in words. The app starts over. 

<h2>Credits</h2> 
Since this is my first Python project, I've taken inspiration from the Love Sandwiches Walkthrough Project. 