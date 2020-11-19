# Wiki Users Contributions Report

A small tool to get report on any wikipedia user's contribution list as a CSV file.

``` bash
python3 get_user_contributions.py <language> <wikisite> <username> <start_date> <end_date>
```

# example

python3 get_user_contributions.py ta wikisource Tshrinivasan 2015-01-30 2020-11-20

Result will be written in data/user_contrib.csv 

# View Results in browser

Used csv-to-html-table to show the csv file as a web page.

After running the get_user_contributions.py, run below command

``` bash
python3 -m http.server
```

Then, point the browser to "http://localhost:8000"

# Screenshot

![Screenshot](Screenshot.jpg?raw=true "Title")

# Thanks 

CSV to HTML Table

https://github.com/derekeder/csv-to-html-table

Display any CSV file as a searchable, filterable, pretty HTML table. Done in 100% JavaScript.

Check out the working demo: http://derekeder.github.io/csv-to-html-table/


# Copyright
MIT License

# TODO
* Make this as web application using flask or django
* deploy in cloud vps of wikimedia
* Make the items clickable on the HTML table. Like to corresponding wiki page, revision id and diff pages

