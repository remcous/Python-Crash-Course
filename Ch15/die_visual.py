import pygal
from die import Die

# Create a D6 and a D10.
die_1 = Die()
die_2 = Die(num_sides=20)

# Make some rolls, and store results in a list.
results = []
num_trials = 10000
for roll_num in range(num_trials):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling a D" + str(die_1.num_sides) + " and a D" 
hist.title += str(die_2.num_sides) + " " + str(num_trials) + " times."
hist.x_labels = range(2, max_result+1)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D' + str(die_1.num_sides) + " + D" + str(die_2.num_sides), frequencies)
hist.render_to_file('die_visual.svg')