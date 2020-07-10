import matplotlib.pyplot as plt

labels = 'A', 'B', 'C', 'D'
fracs = [15, 30, 45, 10]

explode = [0, 0.1, 0, 0]

plt.pie(x = fracs, labels = labels, autopct = '%.0f%%', explode = explode, shadow = True)

plt.show()

