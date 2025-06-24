import pandas as pd
from datetime import datetime

# Create sample data
data = [
    {'timestamp': '2025-03-14 10:01:00', 'type': 'click', 'element': 'Button', 'page': 'HomePage', 'user_id': 1},
    {'timestamp': '2025-03-14 10:02:00', 'type': 'click', 'element': 'Link', 'page': 'ProductPage', 'user_id': 1},
    {'timestamp': '2025-03-14 10:03:00', 'type': 'scroll', 'element': 'ProductCard', 'page': 'ProductPage', 'user_id': 1},
    {'timestamp': '2025-03-14 10:04:00', 'type': 'click', 'element': 'Button', 'page': 'CheckoutPage', 'user_id': 1},
    {'timestamp': '2025-03-14 10:05:00', 'type': 'click', 'element': 'Button', 'page': 'HomePage', 'user_id': 2},
    {'timestamp': '2025-03-14 10:06:00', 'type': 'scroll', 'element': 'ProductCard', 'page': 'ProductPage', 'user_id': 2},
    {'timestamp': '2025-03-14 10:07:00', 'type': 'click', 'element': 'Link', 'page': 'ProductPage', 'user_id': 2},
    {'timestamp': '2025-03-14 10:08:00', 'type': 'click', 'element': 'Button', 'page': 'CheckoutPage', 'user_id': 2},
    {'timestamp': '2025-03-14 10:09:00', 'type': 'scroll', 'element': 'ProductCard', 'page': 'ProductPage', 'user_id': 3},
    {'timestamp': '2025-03-14 10:10:00', 'type': 'click', 'element': 'Button', 'page': 'HomePage', 'user_id': 3},
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert 'timestamp' to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# # Display the DataFrame
# print(df)
# Filter only 'click' interactions
click_data = df[df['type'] == 'click']

# Count the most clicked elements
most_clicked_elements = click_data['element'].value_counts()

# Display the result
print("Most Clicked Elements:")
print(most_clicked_elements)
# Count the most frequent pages
most_visited_pages = df['page'].value_counts()

# Display the result
print("Most Frequent Pages:")
print(most_visited_pages)
import matplotlib.pyplot as plt
import seaborn as sns

# Plot Most Clicked Elements
plt.figure(figsize=(8, 6))
sns.barplot(x=most_clicked_elements.index, y=most_clicked_elements.values)
plt.title('Most Clicked Elements')
plt.xlabel('Element')
plt.ylabel('Click Count')
plt.show()

# Plot Most Frequent Pages
plt.figure(figsize=(8, 6))
sns.barplot(x=most_visited_pages.index, y=most_visited_pages.values)
plt.title('Most Frequent Pages')
plt.xlabel('Page')
plt.ylabel('Visit Count')
plt.show()
