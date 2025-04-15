# VegaPraksa
Data Analytics Internship
We have a snapshot of the data warehouse from the Smart Store. Orders tables (one for each
region) contain information about orders where each row is uniquely identified by column “Row
ID”. Returns table contains items order ids that are returned. Users table shows manager names
for each region of the United States. The goal of following tasks is to perform business analysis
of the store.
**SQL**
1. Importing Data

● Create a database in SQL.

● Import data into a database with appropriate table names, column names and
datatypes. Define fitting primary and foreign keys.

● Round columns “Discount”, “Unit Price”, “Shipping Cost”, “Product Base Margin”,
“Profit” and “Sales” up to 2 decimal places in orders tables.

2. Queries
● Find the top 3 customers who have the highest total sales in an east region,
along with their total profit and the number of orders placed.

● Find top 3 product subcategories based on the highest number of orders along
with their total sales and total profits.

● Find the average product base margin, average profit and average sales by
month where quantity ordered is greater than 10 and sales are greater than
average of sales.

● Assign rank to each product subcategory by total sales and return top 5
best-selling subcategories.

● Assign rank to each manager by total profits.

● Find which product subcategory is returned the most times.

3. Views

● Create a view that combines orders from all regions.

● Create a view that combines previously created orders view with returns and
users.

● Create a view that shows customer id’s, customer names and their total
discounts, total profits and total sales. Sort table by total sales descending.

**BI**

Import data from SQL. Report should contain following pages:
1. Overview
● On the top 4 cards that contain information about how many unique orders and
unique customers we have as well as total sales and total profits. Cards should
be evenly distributed horizontally. Category labels in all cards should be bolded.
Total sales and total profits cards should be in currency format (dollars) and
numbers rounded up to 2 decimal places. Total profit value should be green if
positive or red if negative.

● On the second half of the page a bar chart that shows counts of product category
and product subcategory hierarchically. When clicked on any bar that represents
counts of a specific category, the bar chart should show only the counts of that
category subcategories. Tooltips should contain information about product
category, count of product category and total profits. On each bar there should be
a data label, more specifically count values.

2. Distribution Map
● Format “Postal Code” column. Postal codes in the USA are in 5 digit format.

● Whole page should be a map with information about the amount of sales by state
or province, city and postal code presented with the size of the bubbles. Color of
bubbles should be green if profit is positive value or red if profit is negative value.
Tooltips should contain information about location, sales and profits. When a
bubble that represents sales by state or province is selected, the map should
display distribution in that state or province by city and when city is selected, the
map should display distribution in that city by postal code. Show only cities and
postal codes in the United States (There can be cities with same names and
postal codes with same values in the rest of the world).

3. Table
● Table needs to contain the following columns: “Customer ID”, “Customer Name”,
“Order Priority”, “Product Category”, “Product Sub-Category”, “State or Province”,
”‘City”, “Postal Code”, “Order Date”, “Ship Date”, “Sales” and “Profits”. Profit
column values should be green if positive or red if negative value. Columns
“Order Date” and “Ship Date” should be in “mm/dd/yyyy” format. At the bottom of
the table “Sales” and “Profit” columns should contain totals for sales and profit.

● We should incorporate the following slicers: “Order Priority”, “Product Category”,
“State or Province and City”, and “Order Date”. First 3 slicers should be
dropdown slicers. “Order Date” slicer should be designed to pick a date interval.

4. Analysis of Sales by Product Category and Sub-Category
● This page should contain the following visuals: decomposition tree, pie chart,
slicer and Q&A visual.

● The decomposition tree should analyze sales which should be explained by
product category and product subcategories where values are sorted
descending.

● Pie chart should represent counts and percentages by order priority.

● Slicer should contain state or province tiles so the page could be filtered by it.

● Q&A visual should show information about unique orders by city.

5. Delivery Analysis
● This page should provide insights about the time difference between orders and
shipping dates.

● Main visual here should be a line chart.

● Line chart should show values of average number of days between order date
and shipping date and median number of days between order date and shipping
date by order priority.

● On the X-axis values of order priority should be sorted in the following manner:
“Low”, “Medium”, “High”, “Critical” and “Not Specified”.

● Tooltips on this visual should contain information about:
  ○ Average number of days between order date and shipping date
  ○ Median number of days between order date and shipping date
  ○ Shipping cost average
  ○ Median of shipping cost
  ○ Maximum shipping cost
  ○ Minimum shipping cost

● Slicers: filtering by month and state or province and by manager.

6. Profit Change
● This page should contain the following visuals: ribbon chart, matrix and slicer.

● Slicer to filter page by state or province.

● Ribbon chart to show information about profits by month and product category.

● Matrix to show information about product subcategories by row and unique
orders and profit by column. Add total by column.

● Make sure that ribbon chart filters the matrix but the matrix does not filter the
ribbon chart.

7. Analysis of your own choice
● Research data and perform analysis on your own.

**Python**
1. Preprocessing and Dataframe Manipulation
● Read data from SQL.

● Check if there are any null values. If there are any, replace null values with
median. How many rows contained null value?

● Add a column to the orders dataframe which calculates days between order date
and ship date for every order.

● Format column named “Postal Code”. Postal codes in the USA are in 5 digit
format.

● Calculate correlation between orders dataframe columns. Do not include columns
“Row ID”, “Customer ID” and “Order ID”. Return top 3 most and least correlated
pairs of attributes. Export results as csv file to an arbitrary location.

● Calculate most valuable customers (top 10) with respect to sales amount. Export
results as csv file to an arbitrary location without indexes.

● Create 5 pivot tables that shows the average of columns “Discount”, “Shipping
Cost” and “Days Between Order and Ship Date” and totals of “Profit” and “Sales”
by “Order Priority”, “Customer Segment”, “Product Category”, “Product
Sub-Category” and “State or Province”. Rename each column accordingly, round
values and export each table in csv format to an arbitrary location.

2. Exploratory Data Analysis and Visualization
● Think about what visuals can give us useful information about our dataset, plot
them and write short conclusions for each of them.

Extra Tasks

1. Animation
● Plot animated bar chart race which displays top 10 states by cumulative sum of
sales between the largest time period in data per date.

● Plot animated bar chart race which displays cumulative sum of profits for order
priority between largest time period in data per week number.

2. Statistics
● Check if there exists a statistically significant difference between regions for the
mean of sales. - Hint: Transform to normal distribution

● If the above is true, find out between which pairs of regions a statistically
significant difference is suggested.
