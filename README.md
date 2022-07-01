<h1>Welcome to the monthly bills app!</h1>

<h2>Background</h2>  
This is an app that calculates the cost for a small nursing home per month and returns the sum and an average from the last six months. It is portfolio project 3 Python Essentials.  

It is built on the Code Institute student template abd the code i placed in the `run.py` file.

There is an API to google sheets and the dependency is placed in the `requirements.txt` file.

<h2>Content and features</h2>    
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

A six month average is calculated from the last six sums and returned to user. The average is added to worksheet.

<h2>Testing and bugs</h2> 
Over the development of the app, different solutions have been tested to solve the task. Smaller parts of code has been built and tested in replit. I also commented out parts of code in gitpod during the process.

I checked the code in https://www.pythonchecker.com/ and got back a good result. 

One of the trickier parts during the development was that I started off by asking for integers in the input-field (int(input("rent")). An answer in the input field that was not an integer exited the whole app and skipped the while loop that returns the user to the same question. 

The input for both rent and phone has been changed in late testing of the app. The validator functions check if the inputs are integers and if not, returns the user to the same question. 

Since the function calculates monthly salary from the number of employee input, this integer requirement is left in the app, even though the solution is not optimal. A word in the input field skips the while loop.

<h2>Deployment</h2>

Heroku 

<h2>Credits</h2> 
Inspiration has been taken from the Love Sandwiches Walkthrough Project. 

Thank you to my mentor at Code Institute Ronan McClelland for good discussions during the project. 