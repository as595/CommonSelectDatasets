# CommonSelectDatasets
Repository for UK House of Commons Select Committee Minutes Datasets

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
