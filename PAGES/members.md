
Once the Chair has been identified (```members=True```), the lines before the first business item are appended into a list of members. The first business item is identified by the occurrence of a digit as the first character.

```python
if members and len(items)>0:
    if not items[0][0].isdigit():
        list.append(line)
    else:
         members = False
         content = True
         mlist  = list
         list = []
```

#### Data cleaning

In the PDF, the lists of members present are given in two columns. ```textract``` does not distinguish these columns and so the names in each column are concatenated in each line. 

```python
def clean_mlist(mlist):
    
    newlist=[]
    for line in mlist:
    
        # fix separated capitals:
        line = fix_words(line)
        
        # fix common textract error:
        line = line.replace('Tain','Iain') # bit specific...
        
        # loop through lines and separate names:
        items = line.split()
        if len(items)==4:
            newlist.append([items[1],items[0]])
            newlist.append([items[3],items[2]])
        elif len(items)==2:
            newlist.append([items[1],items[0]])
        else:
            newlist.append([line])

    mlist = newlist

    return mlist
```
