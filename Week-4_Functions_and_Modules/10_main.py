import matplotlib.pyplot as plot_py
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
temp = [94, 94, 93, 95, 96, 95, 95]

plot_py.figure(figsize=(7.5, 5))
plot_py.plot(days, temp, marker='o', color='black')
plot_py.xlabel('Days of the Week')
plot_py.ylabel('Temperature (°F)')
plot_py.title('Temperature Variations Over a Week')
plot_py.grid(True)
plot_py.show()