# CommonSelectDatasets
Repository for UK House of Commons Select Committee Minutes Datasets

*If you use these data, please cite the DOI:*

Useful for doing interesting things like... determining the gender balance in the witnesses called to give evidence before each select committee and ranking them:

![](https://github.com/as595/CommonSelectDatasets/blob/master/media/committees.png)

## Using the data

All of the data available here is taken from the [Parliament UK website](https://www.parliament.uk/business/committees/committees-a-z/commons-select/) where the formal minutes of each House of Commons Select Committee are available to download in PDF format. I've extracted the text from each of these pdfs and then created a data object for the minutes of each meeting for each committee. You can either use the plain text directly, or load the JSON data objects. 

The plain text files for each committee for each year are named:

COMMITTEE-NAME_Y1-Y2.txt

and can be obtained in bulk for each committee using the COMMITTEE-NAME.txt.tar files. 

The JSON files for each committe for each year are named:

COMMITTEE-NAME_Y1-Y2.json

and can be obtained in bulk for each committee using the COMMITTEE-NAME.json.tar files. Each individual file contains a list of JSON objects, one for each meeting. The format of the JSON objects [is described here](https://github.com/as595/CommonSelectDatasets/blob/master/PAGES/dataformat.md).

### The JSON object

The JSON object for each committee meeting has a number of keywords which contain information automatically extracted from the text files. These include:

* [date](https://github.com/as595/CommonSelectDatasets/blob/master/PAGES/date.md)
* committee name
* [committee chair](https://github.com/as595/CommonSelectDatasets/blob/master/PAGES/chair.md)
* [present committee members](https://github.com/as595/CommonSelectDatasets/blob/master/PAGES/members.md)
* a list of [witnesses called to give oral evidence](https://github.com/as595/CommonSelectDatasets/blob/master/PAGES/witnesses.md)
* the number of business items
* the content of the minutes for the business
* the date of the next meeting

This format [is illustrated here](https://github.com/as595/CommonSelectDatasets/blob/master/PAGES/dataformat.md).
