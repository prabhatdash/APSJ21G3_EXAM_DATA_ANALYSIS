def avgsale():
    total_sale = df['FPrice'].sum()
    items_sold = df['Qty'].sum()
    avg_sale = total_sale/items_sold
    print('AVERAGE SALE', avg_sale)
def topfivesalesbyprice():
    prod_sales = pd.DataFrame(df.groupby('Item_Name').sum()['FPrice'])
    # Top 5 sales ie By Price
    prod_sales.sort_values(by=['FPrice'], inplace=True, ascending=False)
    top_prods = prod_sales.head(5)
    print(top_prods)
def mostsellingproducts():
    # Most selling products ie More Quantity
    best_selling_prods = pd.DataFrame(df.groupby('Item_Name').sum()['Qty'])
    best_selling_prods.sort_values(by=['Qty'], inplace=True, ascending=False)
    best_selling_prods = best_selling_prods.head(5)
    print('MOST SELLING PRODUCTS', best_selling_prods)
def revenueperitem():
    print('REVENUE PER ITEM')
    x = pd.DataFrame(df.groupby('Item_Name').sum()['FPrice'])
    print(x)
def revenuepercat():
    print('REVENUE PER CATEGORY')
    x = pd.DataFrame(df.groupby('Item_Category').sum()['FPrice'])
    print(x)
def revenuepercustomer():
    print('REVENUE PER CUSTOMER')
    mostvalcus = pd.DataFrame(df.groupby('Customer').sum()['FPrice'])
    print(mostvalcus)
def mostvaluablecustomer():
     mostvalcus = pd.DataFrame(df.groupby('Customer').sum()['FPrice'])
     mostvalcus.sort_values(by=['FPrice'], inplace=True, ascending=False)
     mostvalcus = mostvalcus.head(1)
     print("MOST VALUABLE CUSTOMER=",mostvalcus)
def tfs_graph():
    list = df['Price'] * df['Qty']
    df['FPrice'] = list
    # 1
    prod_sales = pd.DataFrame(df.groupby('Item_Name').sum()['FPrice'])
    # Top 5 sales ie By Price
    prod_sales.sort_values(by=['FPrice'], inplace=True, ascending=False)
    top_prods = prod_sales.head(5)
    l1 = []
    l2 = []
    for i in top_prods.iterrows():
        l1.append(i[0])
        l2.append(i[1][0])
    plt.bar(l1, l2, width=0.5)
    plt.ylabel('Price', size=10, color='g')
    plt.xlabel('Item Name', size=10, color='b')
    plt.title('Graph of Top five products per price ', size=15, color='r')
    plt.show()
def tfms_graph():
    best_selling_prods = pd.DataFrame(df.groupby('Item_Name').sum()['Qty'])
    best_selling_prods.sort_values(by=['Qty'], inplace=True, ascending=False)
    best_selling_prods = best_selling_prods.head(5)
    l3=[]
    l4=[]

    for i in best_selling_prods.iterrows():
         l3.append(i[0])
         l4.append(i[1][0])
    plt.plot(l3,l4)
    plt.ylabel('Item_Name',size=10)
    plt.xlabel('Qty',size=10)
    plt.title('Top 5 sales by quantity',size=15)
    plt.show()
def rpcu():
    mostvalcus = pd.DataFrame(df.groupby('Customer').sum()['FPrice'])

    l5=[]
    l6=[]
    for i in mostvalcus.iterrows():
        l5.append(i[0])
        l6.append(i[1][0])
    plt.plot(l5,l6)

    plt.xlabel('Customers',size=10)
    plt.ylabel('Revenue',size=10)
    plt.title("Revenue per Customer",size=15)
    plt.show()
def rpca():
    x = pd.DataFrame(df.groupby('Item_Category').sum()['FPrice'])

    l7 = []
    l8 = []
    for i in x.iterrows():
        l7.append(i[0])
        l8.append(i[1][0])
    plt.bar(l7, l8, width=0.5)

    plt.xlabel('Item_Category ', size=10)
    plt.ylabel('Revenue', size=10)
    plt.title("Revenue per Category", size=15)
    plt.show()