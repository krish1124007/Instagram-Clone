import matplotlib.pyplot as plt

# Data
years = [
    2012, 2013, 2014, 2015, 2016, 
    2017, 2018, 2019, 2020, 2021, 
    2022, 2023, 2024
]
values = [
    75000, 100000, 125000, 150000, 175000, 
    215000, 300000, 325000, 350000, 375000, 
    400000, 500000, 430000
]

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(years, values, marker='o', color='g', linestyle='-', linewidth=2, markersize=8)

# Adding titles and labels
plt.title('Maruti Creation', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Income', fontsize=14)

# Displaying the graph
plt.grid(True)
plt.show()




