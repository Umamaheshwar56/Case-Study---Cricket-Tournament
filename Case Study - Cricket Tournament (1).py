#!/usr/bin/env python
# coding: utf-8

# <h2 style = "color : Brown"> Case Study - Cricket Tournament </h2>
# 
# <h4 style = "color : Sky blue"> Example - 1</h4>  
# 
# ##### Players list contain the height(inches) and weight(lbs) data for all the players
# 

# In[2]:


min = (lambda x, y: x if x < y else y)
min(101*99, 102*98)


# In[3]:


# list of height and weight of the players.
players = [(74, 180), (74, 215), (72, 210), (72, 210), (73, 188), (69, 176), (69, 209), (71, 200), (76, 231), (71, 180), (73, 188), (73, 180), (74, 185), (74, 160), (69, 180), (70, 185), (73, 189), (75, 185), (78, 219), (79, 230), (76, 205), (74, 230), (76, 195), (72, 180), (71, 192), (75, 225), (77, 203), (74, 195), (73, 182), (74, 188), (78, 200), (73, 180), (75, 200), (73, 200), (75, 245), (75, 240), (74, 215), (69, 185), (71, 175), (74, 199), (73, 200), (73, 215), (76, 200), (74, 205), (74, 206), (70, 186), (72, 188), (77, 220), (74, 210), (70, 195), (73, 200), (75, 200), (76, 212), (76, 224), (78, 210), (74, 205), (74, 220), (76, 195), (77, 200), (81, 260), (78, 228), (75, 270), (77, 200), (75, 210), (76, 190), (74, 220), (72, 180), (72, 205), (75, 210), (73, 220), (73, 211), (73, 200), (70, 180), (70, 190), (70, 170), (76, 230), (68, 155), (71, 185), (72, 185), (75, 200), (75, 225), (75, 225), (75, 220), (68, 160), (74, 205), (78, 235), (71, 250), (73, 210), (76, 190), (74, 160), (74, 200), (79, 205), (75, 222), (73, 195), (76, 205), (74, 220), (74, 220), (73, 170), (72, 185), (74, 195), (73, 220), (74, 230), (72, 180), (73, 220), (69, 180), (72, 180), (73, 170), (75, 210), (75, 215), (73, 200), (72, 213), (72, 180), (76, 192), (74, 235), (72, 185), (77, 235), (74, 210), (77, 222), (75, 210), (76, 230), (80, 220), (74, 180), (74, 190), (75, 200), (78, 210), (73, 194), (73, 180), (74, 190), (75, 240), (76, 200), (71, 198), (73, 200), (74, 195), (76, 210), (76, 220), (74, 190), (73, 210), (74, 225), (70, 180), (72, 185), (73, 170), (73, 185), (73, 185), (73, 180), (71, 178), (74, 175), (74, 200), (72, 204), (74, 211), (71, 190), (74, 210), (73, 190), (75, 190), (75, 185), (79, 290), (73, 175), (75, 185), (76, 200), (74, 220), (76, 170), (78, 220), (74, 190), (76, 220), (72, 205), (74, 200), (76, 250), (74, 225), (75, 215), (78, 210), (75, 215), (72, 195), (74, 200), (72, 194), (74, 220), (70, 180), (71, 180), (70, 170), (75, 195), (71, 180), (71, 170), (73, 206), (72, 205), (71, 200), (73, 225), (72, 201), (75, 225), (74, 233), (74, 180), (75, 225), (73, 180), (77, 220), (73, 180), (76, 237), (75, 215), (74, 190), (76, 235), (75, 190), (73, 180), (71, 165), (76, 195), (75, 200), (72, 190), (71, 190), (77, 185), (73, 185), (74, 205), (71, 190), (72, 205), (74, 206), (75, 220), (73, 208), (72, 170), (75, 195), (75, 210), (74, 190), (72, 211), (74, 230), (71, 170), (70, 185), (74, 185), (77, 241), (77, 225), (75, 210), (75, 175), (78, 230), (75, 200), (76, 215), (73, 198), (75, 226), (75, 278), (79, 215), (77, 230), (76, 240), (71, 184), (75, 219), (74, 170), (69, 218), (71, 190), (76, 225), (72, 220), (72, 176), (70, 190), (72, 197), (73, 204), (71, 167), (72, 180), (71, 195), (73, 220), (72, 215), (73, 185), (74, 190), (74, 205), (72, 205), (75, 200), (74, 210), (74, 215), (77, 200), (75, 205), (73, 211), (72, 190), (71, 208), (74, 200), (77, 210), (75, 232), (75, 230), (75, 210), (78, 220), (78, 210), (74, 202), (76, 212), (78, 225), (76, 170), (70, 190), (72, 200), (80, 237), (74, 220), (74, 170), (71, 193), (70, 190), (72, 150), (71, 220), (74, 200), (71, 190), (72, 185), (71, 185), (74, 200), (69, 172), (76, 220), (75, 225), (75, 190), (76, 195), (73, 219), (76, 190), (73, 197), (77, 200), (73, 195), (72, 210), (72, 177), (77, 220), (77, 235), (71, 180), (74, 195), (74, 195), (73, 190), (78, 230), (75, 190), (73, 200), (70, 190), (74, 190), (72, 200), (73, 200), (73, 184), (75, 200), (75, 180), (74, 219), (76, 187), (73, 200), (74, 220), (75, 205), (75, 190), (72, 170), (73, 160), (73, 215), (72, 175), (74, 205), (78, 200), (76, 214), (73, 200), (74, 190), (75, 180), (70, 205), (75, 220), (71, 190), (72, 215), (78, 235), (75, 191), (73, 200), (73, 181), (71, 200), (75, 210), (77, 240), (72, 185), (69, 165), (73, 190), (74, 185), (72, 175), (70, 155), (75, 210), (70, 170), (72, 175), (72, 220), (74, 210), (73, 205), (74, 200), (76, 205), (75, 195), (80, 240), (72, 150), (75, 200), (73, 215), (74, 202), (74, 200), (73, 190), (75, 205), (75, 190), (71, 160), (73, 215), (75, 185), (74, 200), (74, 190), (72, 210), (74, 185), (74, 220), (74, 190), (73, 202), (76, 205), (75, 220), (72, 175), (73, 160), (73, 190), (73, 200), (72, 229), (72, 206), (72, 220), (72, 180), (71, 195), (75, 175), (75, 188), (74, 230), (73, 190), (75, 200), (79, 190), (74, 219), (76, 235), (73, 180), (74, 180), (74, 180), (72, 200), (74, 234), (74, 185), (75, 220), (78, 223), (74, 200), (74, 210), (74, 200), (77, 210), (70, 190), (73, 177), (74, 227), (73, 180), (71, 195), (75, 199), (71, 175), (72, 185), (77, 240), (74, 210), (70, 180), (77, 194), (73, 225), (72, 180), (76, 205), (71, 193), (76, 230), (78, 230), (75, 220), (73, 200), (78, 249), (74, 190), (79, 208), (75, 245), (76, 250), (72, 160), (75, 192), (75, 220), (70, 170), (72, 197), (70, 155), (74, 190), (71, 200), (76, 220), (73, 210), (76, 228), (71, 190), (69, 160), (72, 184), (72, 180), (69, 180), (73, 200), (69, 176), (73, 160), (74, 222), (74, 211), (72, 195), (71, 200), (72, 175), (72, 206), (76, 240), (76, 185), (76, 260), (74, 185), (76, 221), (75, 205), (71, 200), (72, 170), (71, 201), (73, 205), (75, 185), (76, 205), (75, 245), (71, 220), (75, 210), (74, 220), (72, 185), (73, 175), (73, 170), (73, 180), (73, 200), (76, 210), (72, 175), (76, 220), (73, 206), (73, 180), (73, 210), (75, 195), (75, 200), (77, 200), (73, 164), (72, 180), (75, 220), (70, 195), (74, 205), (72, 170), (80, 240), (71, 210), (71, 195), (74, 200), (74, 205), (73, 192), (75, 190), (76, 170), (73, 240), (77, 200), (72, 205), (73, 175), (77, 250), (76, 220), (71, 224), (75, 210), (73, 195), (74, 180), (77, 245), (71, 175), (72, 180), (73, 215), (69, 175), (73, 180), (70, 195), (74, 230), (76, 230), (73, 205), (73, 215), (75, 195), (73, 180), (79, 205), (74, 180), (73, 190), (74, 180), (77, 190), (75, 190), (74, 220), (73, 210), (77, 255), (73, 190), (77, 230), (74, 200), (74, 205), (73, 210), (77, 225), (74, 215), (77, 220), (75, 205), (77, 200), (75, 220), (71, 197), (74, 225), (70, 187), (79, 245), (72, 185), (72, 185), (70, 175), (74, 200), (74, 180), (72, 188), (73, 225), (72, 200), (74, 210), (74, 245), (76, 213), (82, 231), (74, 165), (74, 228), (70, 210), (73, 250), (73, 191), (74, 190), (77, 200), (72, 215), (76, 254), (73, 232), (73, 180), (72, 215), (74, 220), (74, 180), (71, 200), (72, 170), (75, 195), (74, 210), (74, 200), (77, 220), (70, 165), (71, 180), (73, 200), (76, 200), (71, 170), (75, 224), (74, 220), (72, 180), (76, 198), (79, 240), (76, 239), (73, 185), (76, 210), (78, 220), (75, 200), (76, 195), (72, 220), (72, 230), (73, 170), (73, 220), (75, 230), (71, 165), (76, 205), (70, 192), (75, 210), (74, 205), (75, 200), (73, 210), (71, 185), (71, 195), (72, 202), (73, 205), (73, 195), (72, 180), (69, 200), (73, 185), (78, 240), (71, 185), (73, 220), (75, 205), (76, 205), (70, 180), (74, 201), (77, 190), (75, 208), (79, 240), (72, 180), (77, 230), (73, 195), (75, 215), (75, 190), (75, 195), (73, 215), (73, 215), (76, 220), (77, 220), (75, 230), (70, 195), (71, 190), (71, 195), (75, 209), (74, 204), (69, 170), (70, 185), (75, 205), (72, 175), (75, 210), (73, 190), (72, 180), (72, 180), (72, 160), (76, 235), (75, 200), (74, 210), (69, 180), (73, 190), (72, 197), (72, 203), (75, 205), (77, 170), (76, 200), (80, 250), (77, 200), (76, 220), (79, 200), (71, 190), (75, 170), (73, 190), (76, 220), (77, 215), (73, 206), (76, 215), (70, 185), (75, 235), (73, 188), (75, 230), (70, 195), (69, 168), (71, 190), (72, 160), (72, 200), (73, 200), (70, 189), (70, 180), (73, 190), (76, 200), (75, 220), (72, 187), (73, 240), (79, 190), (71, 180), (72, 185), (74, 210), (74, 220), (74, 219), (72, 190), (76, 193), (76, 175), (72, 180), (72, 215), (71, 210), (72, 200), (72, 190), (70, 185), (77, 220), (74, 170), (72, 195), (76, 205), (71, 195), (76, 210), (71, 190), (73, 190), (70, 180), (73, 220), (73, 190), (72, 186), (71, 185), (71, 190), (71, 180), (72, 190), (72, 170), (74, 210), (74, 240), (74, 220), (71, 180), (72, 210), (75, 210), (72, 195), (71, 160), (72, 180), (72, 205), (72, 200), (72, 185), (74, 245), (74, 190), (77, 210), (75, 200), (73, 200), (75, 222), (73, 215), (76, 240), (72, 170), (77, 220), (75, 156), (72, 190), (71, 202), (71, 221), (75, 200), (72, 190), (73, 210), (73, 190), (71, 200), (70, 165), (75, 190), (71, 185), (76, 230), (73, 208), (68, 209), (71, 175), (72, 180), (74, 200), (77, 205), (72, 200), (76, 250), (78, 210), (81, 230), (72, 244), (73, 202), (76, 240), (72, 200), (72, 215), (74, 177), (76, 210), (73, 170), (76, 215), (75, 217), (70, 198), (71, 200), (74, 220), (72, 170), (73, 200), (76, 230), (76, 231), (73, 183), (71, 192), (68, 167), (71, 190), (71, 180), (74, 180), (77, 215), (69, 160), (72, 205), (76, 223), (75, 175), (76, 170), (75, 190), (76, 240), (72, 175), (74, 230), (76, 223), (74, 196), (72, 167), (75, 195), (78, 190), (77, 250), (70, 190), (72, 190), (79, 190), (74, 170), (71, 160), (68, 150), (77, 225), (75, 220), (71, 209), (72, 210), (70, 176), (72, 260), (72, 195), (73, 190), (72, 184), (74, 180), (72, 195), (72, 195), (75, 219), (72, 225), (73, 212), (74, 202), (72, 185), (78, 200), (75, 209), (72, 200), (74, 195), (75, 228), (75, 210), (76, 190), (74, 212), (74, 190), (73, 218), (74, 220), (71, 190), (74, 235), (75, 210), (76, 200), (74, 188), (76, 210), (76, 235), (73, 188), (75, 215), (75, 216), (74, 220), (68, 180), (72, 185), (75, 200), (71, 210), (70, 220), (72, 185), (73, 231), (72, 210), (75, 195), (74, 200), (70, 205), (76, 200), (71, 190), (82, 250), (72, 185), (73, 180), (74, 170), (71, 180), (75, 208), (77, 235), (72, 215), (74, 244), (72, 220), (73, 185), (78, 230), (77, 190), (73, 200), (73, 180), (73, 190), (73, 196), (73, 180), (76, 230), (75, 224), (70, 160), (73, 178), (72, 205), (73, 185), (75, 210), (74, 180), (73, 190), (73, 200), (76, 257), (73, 190), (75, 220), (70, 165), (77, 205), (72, 200), (77, 208), (74, 185), (75, 215), (75, 170), (75, 235), (75, 210), (72, 170), (74, 180), (71, 170), (76, 190), (71, 150), (75, 230), (76, 203), (83, 260), (75, 246), (74, 186), (76, 210), (72, 198), (72, 210), (75, 215), (75, 180), (72, 200), (77, 245), (73, 200), (72, 192), (70, 192), (74, 200), (72, 192), (74, 205), (72, 190), (71, 186), (70, 170), (71, 197), (76, 219), (74, 200), (76, 220), (74, 207), (74, 225), (74, 207), (75, 212), (75, 225), (71, 170), (71, 190), (74, 210), (77, 230), (71, 210), (74, 200), (75, 238), (77, 234), (76, 222), (74, 200), (76, 190), (72, 170), (71, 220), (72, 223), (75, 210), (73, 215), (68, 196), (72, 175), (69, 175), (73, 189), (73, 205), (75, 210), (70, 180), (70, 180), (74, 197), (75, 220), (74, 228), (74, 190), (73, 204), (74, 165), (75, 216), (77, 220), (73, 208), (74, 210), (76, 215), (74, 195), (75, 200), (73, 215), (76, 229), (78, 240), (75, 207), (73, 205), (77, 208), (74, 185), (72, 190), (74, 170), (72, 208), (71, 225), (73, 190), (75, 225), (73, 185), (67, 180), (67, 165), (76, 240), (74, 220), (73, 212), (70, 163), (75, 215), (70, 175), (72, 205), (77, 210), (79, 205), (78, 208), (74, 215), (75, 180), (75, 200), (78, 230), (76, 211), (75, 230), (69, 190), (75, 220), (72, 180), (75, 205), (73, 190), (74, 180), (75, 205), (75, 190), (73, 195)]


# In[4]:


len(players)


# In[5]:


players[1][1]


# In[6]:


import numpy as np

np_players = np.array(players)


# In[7]:


np_players


# In[8]:


type(np_players)


# In[ ]:





# <h4 style = "color : Sky blue"> Example - 2 (Numpy Attributes)</h4>
# 
# ##### Print the structure of the 2-D Array

# In[9]:


np_players.shape


# ##### Print the dimensions of the array

# In[10]:


np_players.ndim


# ##### Print the data type of elements in the array

# In[11]:


np_players.dtype


# ##### Print the size of a single item of the array

# In[12]:


np_players.itemsize


# <h4 style = "color : Sky blue"> Example - 3</h4>
# 
# ##### Convert the heights to meters and weights to kg 

# In[13]:


players_converted = np_players * [0.0254, 0.453592]


# In[14]:


players_converted


# <h4 style = "color : Sky blue"> Sub-Setting 2-D Arrays</h4>
# 
# ##### Fetch the first row from the array 

# In[15]:


players_converted[0]


# ##### Fetch the first row 2nd element from the array 

# In[16]:


players_converted[0][1]


# ##### Fetch the first column from the array 

# In[17]:


players_converted[:, 0]


# ##### Fetch the height (1st column) of 125th player from the array 

# In[18]:


players_converted[124][0]


# In[19]:


players_converted[124,0]


# <h4 style = "color : Sky blue"> Conditional Sub-Setting Arrays</h4>
# 
# ##### Fetch height and weight of players with height above 1.8m
# 

# In[20]:


tall_players = players_converted[players_converted[:,0] > 1.8]


# In[21]:


players_converted.shape


# In[22]:


tall_players.shape


# ##### Skills Array - holds the player key skills.

# In[23]:


skills = np.array(['Keeper', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Bowler', 'Batsman', 'Batsman', 'Bowler', 'Bowler', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Batsman', 'Keeper', 'Bowler', 'Keeper-Batsman', 'Keeper', 'Bowler', 'Keeper', 'Keeper', 'Keeper', 'Keeper', 'Bowler', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Bowler', 'Batsman', 'Batsman', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Bowler', 'Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Batsman', 'Batsman', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Batsman', 'Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Bowler', 'Batsman', 'Keeper', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Bowler', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Bowler', 'Keeper-Batsman', 'Keeper', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Bowler', 'Keeper-Batsman', 'Bowler', 'Keeper', 'Batsman', 'Bowler', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Bowler', 'Bowler', 'Bowler', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Keeper', 'Batsman', 'Keeper', 'Bowler', 'Bowler', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Bowler', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Bowler', 'Keeper', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper', 'Bowler', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Batsman', 'Batsman', 'Bowler', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Batsman', 'Batsman', 'Batsman', 'Keeper', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Bowler', 'Bowler', 'Bowler', 'Batsman', 'Keeper', 'Bowler', 'Bowler', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper', 'Bowler', 'Batsman', 'Bowler', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper', 'Keeper', 'Batsman', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper', 'Batsman', 'Bowler', 'Keeper', 'Keeper', 'Batsman', 'Bowler', 'Bowler', 'Batsman', 'Keeper', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Bowler', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Bowler', 'Batsman', 'Bowler', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Bowler', 'Batsman', 'Batsman', 'Batsman', 'Keeper', 'Keeper', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Batsman', 'Batsman', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Bowler', 'Batsman', 'Keeper', 'Bowler', 'Keeper', 'Bowler', 'Batsman', 'Keeper', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper', 'Bowler', 'Batsman', 'Keeper', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper', 'Batsman', 'Bowler', 'Keeper', 'Bowler', 'Batsman', 'Batsman', 'Bowler', 'Batsman', 'Batsman', 'Bowler', 'Bowler', 'Bowler', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Batsman', 'Bowler', 'Keeper', 'Bowler', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Batsman', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Bowler', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Batsman', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Batsman', 'Batsman', 'Keeper', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Bowler', 'Bowler', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Bowler', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Bowler', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Bowler', 'Keeper', 'Bowler', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Bowler', 'Bowler', 'Batsman', 'Keeper', 'Keeper', 'Keeper-Batsman', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper', 'Batsman', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Batsman', 'Bowler', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Bowler', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Bowler', 'Bowler', 'Keeper', 'Bowler', 'Keeper', 'Batsman', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Bowler', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper', 'Bowler', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Bowler', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Batsman', 'Bowler', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Batsman', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Bowler', 'Batsman', 'Keeper', 'Bowler', 'Bowler', 'Keeper', 'Bowler', 'Bowler', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Bowler', 'Bowler', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Keeper-Batsman'])
skills


# ##### Fetch Heights of the Batsmen

# In[24]:


batsmen = players_converted[skills == 'Batsman']


# In[25]:


batsmen.shape


# In[26]:


batsmen[:, 0]


# In[ ]:




