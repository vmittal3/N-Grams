#!/usr/bin/env python
# coding: utf-8

# # N-grams

# code by Vaibhav Mittal <br>
# last updated on Oct 2, 2021

# In[1]:


import nltk
# nltk.book must be downloaded 
# download using nltk.download() popup


# In[2]:


from nltk.book import *


# In[3]:


text1.concordance("""its water is so transparent that""")


# This simple example (which can be extended to other texts) suggests that many valid sentences in the English language are novel and we might never find them used earlier. Finding probabilities for the word which should appear next becomes challenging. 

# The heuristics we'll use are the chain rule to calculate probabilites, and not going too deep, we'll also use the Markov assumption. For an n-gram, this is -

# \begin{equation*}
# \ P(w_n|w_{1:n-1}) = P(w_n|w_{n-N+1:n-1})
# \end{equation*}

# ## Bigrams

# from https://www.datasciencelearner.com/count-bigrams-in-nltk-stepwise-solution/

# In[4]:


frequency = nltk.FreqDist(nltk.bigrams(text1.tokens))


# In[5]:


for key, value in frequency.items():
    print(key, value)


# ## Let's make our own bigram generator

# In[22]:


def generate_bigrams(text, start = None, stop = None):
    if ((start is None) & (stop is None)):
        for i in range(len(text)):
            text[i] = '<s> ' + text[i] + ' </s>'
    print(text)    


# In[23]:


generate_bigrams(['I am Sam', 'Sam I am', 'I do not like green eggs and ham'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[9]:


print("NLTK v" + nltk.__version__)

