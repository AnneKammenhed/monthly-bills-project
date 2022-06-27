<h1>Welcome to monthly bills app!</h1>

<h2>Background</h2>  
This is an app that calculates the cost for a small nursing home and returns the sum and an average from the last six months.

It is built on the Code Institute student template abd the code i placed in the `run.py` file.

There is an API to google sheets and the dependency is placed in the `requirements.txt` file.

<h2>Content</h2>    
The app collects three types of data from user:
<ul>
<li>Costs linked to premises (e.g. rent, heating) is called rent in this app</li>
<li>Number of employees</li>
<li>Phone cost for this month</li>
</ul>

 First of all the app checks if the data input is valid and prints an error-message if not and return to beginning.

Before moving the numbers to the spreadsheet, the number of employees is multipied by 40000 to get a sum of salaries. To make this a little easier I have taken a average yearly cost of 500 000 SEK and divided into 12 to get  the average cost for an employee. 

The rent, salary and telephone costs are added to worksheet.

The sum is calculated. The sum is added to worksheet. The sum is returned to user.

A six month average is calculated. The average is added to worksheet. The average is returned to user.

"""
When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.
"""