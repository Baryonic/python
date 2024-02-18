import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime

def animate(i):
    # Initialize lists to store time and money values
    time_values = []
    money_values = []

    # Clear the current plot
    plt.clf()

    # Open and read the file
    with open('moneylog.txt', 'r') as file:
        for line in file:
            # Split each line into time and money
            time_str, money_str = line.strip().split(': ')

            # Convert time string to datetime object and append to list
            time_values.append(datetime.datetime.strptime(time_str[4:], '%Y%m%d%H%M%S'))

            # Convert money string to float and append to list
            money_values.append(float(money_str[1:]))

    # Plot the data
    plt.plot(time_values, money_values)
    plt.xlabel('Time')
    plt.ylabel('Money ($)')

    # Add a text box with the current time and last money value
    last_time = time_values[-1].strftime("%Y-%m-%d %H:%M:%S")
    last_money = money_values[-1]
    plt.title(f'Money over Time\nLast update: {last_time}\nLast money value: ${last_money:.2f}')

# Create an animation that updates every second
ani = animation.FuncAnimation(plt.gcf(), animate, interval=500)

# Show the plot
plt.show()

