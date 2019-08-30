
Each meeting commences with the date of the meeting in the format: Day Number Month Year. 

For example: Tuesday 15 February 2017

There is no common standard of capitalisation, e.g. both Tuesday and TUESDAY are used.

An exception to this format is found in the minutes for the EXITING-THE-EUROPEAN-UNION-COMMITTEE which does not include the year (even though the minutes span multiple years).

```python

if 2<len(items)<5 and items[0].replace('‘','').lower() in days:
            date = line.strip('\n')
```

Additionally ```textract``` inserts an apostrophe before some days in the TRANSPORT-COMMITTEE minutes, which must be removed.
