# import random  
# import plotly.express as px
# import plotly.figure_factory as ff

# Dice_Result = []
# Count = []


# for i in range(0,100) :
#     Dice1 = random.randint(1,6)

#     Dice2 = random.randint(1,6)

#     result = Dice1+Dice2
#     Count.append(i)
#     Dice_Result.append(result)

# # fig = px.bar(x = Dice_Result, y = Count)

# fig = ff.create_distplot([Dice_Result],["Result"],show_hist = False)

# fig.show()

#################################################################################################################

# import pandas as pd

# import plotly.figure_factory as ff



# df = pd.read_csv("SOCR-HeightWeight.csv")

# height = df['Height(Inches)'].tolist()

# fig = ff.create_distplot([height],["Height"],show_hist = False)

# fig.show()


import pandas as pd

import plotly.figure_factory as ff

df = pd.read_csv("SOCR-HeightWeight.csv")
weight = df['Weight(Pounds)'].tolist()

fig = ff.create_distplot([weight],["Weight"],show_hist = False)

fig.show()
