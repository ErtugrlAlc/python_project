#!/usr/bin/env python
# coding: utf-8

# In[56]:
## Verilen nested list düzleştirilmiştir.

liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
new_list = []
def düzleme(x):
    for i in x :
        if isinstance(i,type(x)):
            düzleme(i)
        else:
            new_list.append(i)

düzleme(liste)
print(new_list)


# In[65]:

## Burada da verilen liste tersten yazdırılmıştır.
sayılar = [[1, 2], [3, 4], [5, 6, [9,10], 7]]


# In[69]:


def reversing(items):
    for item in items:
        if isinstance(item, list):
            reversing(item)
        return items[::-1]


# In[70]:


reversing(sayılar)


# In[ ]:




