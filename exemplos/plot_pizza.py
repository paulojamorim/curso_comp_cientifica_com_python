import matplotlib.pyplot as plt

labels =  '4 queijos', 'Frango/Catupiry', 'Portuguesa', 'Provolone'
sizes = [10, 40, 45, 5]
colors = ['lightgreen','yellow','lightskyblue', 'lightgray']
explode = (0, 0, 0.1, 0) 

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

plt.axis('equal')
plt.show()
