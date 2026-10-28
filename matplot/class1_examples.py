"""
Class 1: Introduction and Basic Charts

Matplotlib is a Python library for creating visualizations that help explore
data and communicate patterns. Seaborn builds on Matplotlib with convenient
statistical charts and styling; Plotly focuses on interactive charts.

Install Matplotlib in a terminal with:
    python -m pip install matplotlib

Run these examples with:
    python class1_examples.py
"""

import matplotlib.pyplot as plt


# Figure and Axes using figure() and add_subplot().
figure = plt.figure(figsize=(7, 4))
line_axes = figure.add_subplot(1, 1, 1)
days = [1, 2, 3, 4, 5]
temperatures = [18, 20, 19, 23, 25]
line_axes.plot(days, temperatures, marker="o")
line_axes.set_title("Daily temperature")
line_axes.set_xlabel("Day")
line_axes.set_ylabel("Temperature (°C)")

# subplots() creates a Figure and a grid of Axes for the chart examples.
fig, axes = plt.subplots(4, 2, figsize=(12, 14))

# Bar chart: bar()
products = ["Tea", "Coffee", "Juice"]
sales = [24, 35, 18]
axes[0, 0].bar(products, sales)
axes[0, 0].set_title("Product sales")

# Horizontal bar chart: barh()
axes[0, 1].barh(products, sales)
axes[0, 1].set_title("Product sales (horizontal)")

# Scatter plot: scatter()
advertising = [1, 2, 3, 4, 5]
revenue = [2, 3, 5, 4, 7]
axes[1, 0].scatter(advertising, revenue)
axes[1, 0].set_title("Advertising vs. revenue")
axes[1, 0].set_xlabel("Advertising spend")
axes[1, 0].set_ylabel("Revenue")

# Histogram: hist()
exam_scores = [55, 62, 67, 68, 72, 74, 75, 78, 81, 85, 88, 92, 96]
axes[1, 1].hist(exam_scores, bins=5, edgecolor="black")
axes[1, 1].set_title("Exam score distribution")
axes[1, 1].set_xlabel("Score")

# Pie chart: pie()
share_values = [45, 30, 25]
share_labels = ["Online", "Store", "Wholesale"]
axes[2, 0].pie(share_values, labels=share_labels, autopct="%1.0f%%")
axes[2, 0].set_title("Sales by channel")

# Step plot: step()
hours = [0, 1, 2, 3, 4]
water_level = [2, 2, 4, 4, 3]
axes[2, 1].step(hours, water_level, where="mid")
axes[2, 1].set_title("Water level over time")
axes[2, 1].set_xlabel("Hour")

# Stem plot: stem()
days = [1, 2, 3, 4, 5, 6]
messages = [3, 5, 2, 7, 4, 6]
axes[3, 0].stem(days, messages)
axes[3, 0].set_title("Messages received each day")
axes[3, 0].set_xlabel("Day")

# Leave the final grid position empty.
axes[3, 1].set_visible(False)

# Display both figures.
plt.show()
