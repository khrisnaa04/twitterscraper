import matplotlib.pyplot as plt

# Plot most mentioned products
top_products = product_counts.most_common(10)
names, counts = zip(*top_products)

plt.barh(names, counts)
plt.xlabel('Mentions')
plt.ylabel('Product')
plt.title('Top 10 Mentioned Products')
plt.show()