
Where witnesses are listed in a paragraph of meeting business, that paragraph will conclude with *gave evidence.* or *gave oral evidence.* This is used to identify paragraphs that list the names of witnesses. Names are identifed from the text that lies between the phrase ```evidence.``` and the item number of the paragraph, e.g. ```2.```

For example,

```
2. Improving the rail passenger experience

Mick Cash, General Secretary, and Paul Cox, Regional Organiser South East, National
Union of Rail, Maritime and Transport Workers (RMT); and Dyan Crowther, Chief
Operating Officer, and Charles Horton, Chief Executive Officer, Govia Thameslink Railway
gave oral evidence.
```

#### Data preparation

Before the search, the text of each paragraph has the business item section headings removed. For example:

```2. Improving the rail passenger experience``` becomes ```2. ```

This improves the recovery of names from the start of the following paragraph.


#### Top level code

```python
def get_witnesses(text):

    # clean out the business item headings:
    text = strip_titles(text)
    
    # split the text into a list of words:
    tlist = text.split()
    
    # get the limits of the witness list in the text:
    limits = get_limits(tlist)
    
    # extract the names from the text:
    if len(limits)==1:
        words = tlist[limits[0][0]:limits[0][1]]
        block = ' '.join(words)
        names = first_and_last_names(block)
    elif len(limits)>1: # in some minutes there are multiple paragraphs of witnesses
        x = limits[:][0]
        y = limits[:][1]
        x.sort()
        y.sort()
        minlim = x[0]
        maxlim = y[-1]
        words = tlist[minlim:maxlim]
        block = ' '.join(words)
        names = first_and_last_names(block)
    else:
        names = "None"

    return names
```

#### Lower level code

First and last names for each witness are extracted from the text using routines from the ```nltk``` natural language processing toolkit in Python. 
