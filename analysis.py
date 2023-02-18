import pymongo
import matplotlib.pyplot as plt

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["endterm"]
collection = db["olx"]

#____________________________ Query the collection for the count of documents with tags "Бизнес" and "Жеке адам"
# business_count = collection.count_documents({"Tags": "Бизнес"})
# individual_count = collection.count_documents({"Tags": "Жеке адам"})

# # Plot the results as a bar chart
# labels = ['Бизнес', 'Жеке адам']
# counts = [business_count, individual_count]


# business_avg = business_price_sum / business_count if business_count > 0 else 0

# plt.show()

# Query the collection for the average price of documents with tag "Бизнес"
# business_docs = collection.find({"Tags": "Бизнес"})
# business_price_sum = 0
# business_count = 0
# for doc in business_docs:
#     business_price_sum += doc["Price"]
#     business_count += 1

# # Plot the results as a bar chart
# labels = ['Бизнес', 'Жеке адам']
# counts = [business_avg, individual_avg]

# business_avg = business_price_sum / business_count if business_count > 0 else 0

# plt.show()


# _____________________________________Query the collection for the average price of documents with tag "Жеке адам"
# individual_docs = collection.find({"Tags": "Жеке адам"})
# individual_price_sum = 0
# individual_count = 0
# for doc in individual_docs:
#     individual_price_sum += doc["Price"]
#     individual_count += 1
# individual_avg = individual_price_sum / individual_count if individual_count > 0 else 0

# # Plot the results as a bar chart
# labels = ['Бизнес', 'Жеке адам']
# counts = [business_avg, individual_avg]


# fig, ax = plt.subplots()
# ax.bar(labels, counts)

# plt.show()


# ____________________Linegraph of the documents with tags 'Бизнес' and 'Жеке адам'
# query = {"Tags": {"$in": ["Бизнес", "Жеке адам"]}}
# docs = collection.find(query)

# # Extract the prices of the matching documents
# prices = [doc["Price"] for doc in docs]

# # Plot the prices as a line graph
# plt.plot(prices)
# plt.xlabel("Product Index")
# plt.ylabel("Price")
# plt.title("Line Graph of Prices for Products with 'Бизнес' and 'Жеке адам' Tags")
# plt.show()


# ____________DOT GRAPH: BUSINESS/PERSONAL 
# business_prices = []
# personal_prices = []

# for product in collection.find({}):
#     if "Бизнес" in product["Tags"]:
#         business_prices.append(product["Price"])
#     elif "Жеке адам" in product["Tags"]:
#         personal_prices.append(product["Price"])

# plt.scatter(range(len(business_prices)), business_prices, c='red', label='Бизнес')
# plt.scatter(range(len(personal_prices)), personal_prices, c='blue', label='Жеке адам')
# plt.legend()
# plt.xlabel("Products")
# plt.ylabel("Prices")
# plt.title("Prices of Business and Personal Products")
# plt.show()

# ____________DOT GRAPH: NEW/USED_________Dangerous!
new_products = []
used_products = []
for product in collection.find({"Tags": "Күйі: Жаңа"}):
    new_products.append([product["Price"], product["Product_Name"]])
for product in collection.find({"Tags": "Күйі: Қолданылған"}):
    used_products.append([product["Price"], product["Product_Name"]])

# Plot the data
plt.plot(*zip(*new_products), marker='o', color='blue', ls='')
plt.plot(*zip(*used_products), marker='o', color='red', ls='')
plt.xlabel("Price")
plt.ylabel("Product Name")
plt.title("Line Graph Analysis")
plt.legend(["Күйі: Жаңа", "Күйі: Қолданылған"])
plt.show()