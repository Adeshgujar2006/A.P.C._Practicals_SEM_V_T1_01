
#1.create a graph using matplotlib functions
import matplotlib.pyplot as plt
# plt.plot([1,2,3],[4,5,6],color="yellow")
# plt.xlim(1,5)
# plt.xlim(1,6)
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("Demo graph")
# plt.legend(["Values"])
# plt.show()

#3.Draw a basic line graph from position(0,0) to (6,250)
# import matplotlib.pyplot as plt
# import numpy as np
# plt.title("Inflation in India")

# xpoints = np.array([0,6])
# ypoints = np.array([0, 250])

# plt.plot(xpoints, ypoints)
# plt.show()

#4.Create an irregular graph
# import matplotlib.pyplot as plt
# plt.title("Average per capita income of Indians")
# y=[2014,2018,2020,2024,2025]
# x=[10000,9000,8000,7000,6000]
# plt.xlabel("Years")
# plt.ylabel("Income in dollars '$' ")
# plt.plot(y,x,color="red")
# plt.show()

#5. Scatter plot:
# import matplotlib.pyplot as plt
# x=[2,6,7,8,10]
# y=[5,8,1,6,8]
# plt.scatter(x,y)
# plt.title("scatter plot example")
# plt.show()

#6.Bar plot
# x=["PHYSICS","CHEMISTRY","MATHS","ENGLISH","MARATHI"]
# y=[95,80,85,96,95]
# plt.xlabel("SUBJECTS")
# plt.ylabel("Marks")
# plt.bar(x,y)
# plt.title("Bar chart")
# plt.legend(["bar"])
# plt.show()

#7.Horizontal Bars
# x=["2021","2022","2023","2024","2025"]
# y=[1028,1056,899,1139,1570]

# plt.xlabel("Rainfall(in mm)")
# plt.ylabel("Years")
# plt.barh(x,y)
# plt.title("Average Rainfall in Kolhapur district")
# plt.legend(["bar"])
# plt.show()

#8.Pie Plots
# x=[2,3,4,5]
# e=(0.1,0,0,0)

# plt.pie(x,explode=e)
# plt.show()

#9.Histogram
# x=[1,2,3,4,5,6,7,4]
# plt.hist(x,bins=[1,2,3,4,5,6,7])
# plt.show()

#10.3D Plot
# import numpy as np
# fig=plt.figure()
# ax=plt.axes(projection='3d')
# z=np.linspace(0,1,100)
# x=z*np.sin(25*z)
# y=z*np.cos(25*z)
# ax.plot3D(x,y,z,'red')
# plt.show()

#11.SUBPLOT
# import numpy as np
# x=np.array([1,2,3,4,5])
# y=np.array([5,4,4,3,1])
# plt.subplot(1,2,1)
# plt.plot(y,x)
# plt.title("Income in India")

# x=np.array([0,1,2,3])
# y=np.array([10,20,30,40])
# plt.subplot(1,2,2)
# plt.plot(x,y)
# plt.title("Inflation in India")
# plt.suptitle("Indian Society")
# plt.show()

#12.mixture of graphs


# years = [2021, 2022, 2023, 2024, 2025]
# rainfall = [1028, 1056, 899, 1139, 1570]
# temperature = [27, 28, 29, 28, 27]
# humidity = [75, 78, 72, 80, 82]

# plt.figure(figsize=(12, 9))


# plt.subplot(2, 2, 1)
# plt.bar(years, rainfall)
# plt.title("Annual Rainfall")
# plt.xlabel("Year")
# plt.ylabel("Rainfall (mm)")


# plt.subplot(2, 2, 2)
# plt.plot(years, temperature, marker='o')
# plt.title("Average Temperature")
# plt.xlabel("Year")
# plt.ylabel("Temperature (°C)")


# plt.subplot(2, 2, 3)
# plt.pie(
#     rainfall,
#     labels=years,
    
# )
# plt.title("Rainfall Distribution")


# plt.subplot(2, 2, 4)
# plt.scatter(temperature, humidity)
# plt.title("Temperature vs Humidity")
# plt.xlabel("Temperature (°C)")
# plt.ylabel("Humidity (%)")


# plt.show()

