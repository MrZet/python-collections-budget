import matplotlib.pyplot as plt
from . import Expense
import collections

expenses = Expense.Expenses()
expenses.read_expenses(r'data\spending_data.csv')

spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)

# print(spending_categories)

spending_counter = collections.Counter(spending_categories)

top5 = spending_counter.most_common(5)
categories, counts = zip(*top5)
# print(categories)
# print(counts)

fig, ax = plt.subplots()
ax.bar(categories,counts)
ax.set_title("# of Purchases by Category")
plt.show()
