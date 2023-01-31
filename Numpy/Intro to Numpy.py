
fig, ax=plt.subplots()
ax.plot(x,y);
print(type(fig),type(ax))
plt.show()

##### MATPLOT LIB EXAMPLE WORKFLOW TITLE AND AXIS RENAMING

fig, ax= plt.subplots(figsize = (10,10)) # width, Height
ax.plot(x,y)
ax.set(title = "Learning Matplotlib Plot", xlabel = "X-Axis", ylabel = "Y-Axis")
plt.show()


##### MAKING FIGURES WITH NUMPY ARRAYS SCATTER PLOT

x = np.linspace(0,10,50, endpoint=True, )
print(x[:10])
fig, ax =  plt.subplots() 
ax.scatter(x,np.sin(x))
plt.show()

##### BAR GRAPH
x = {"Shahab" : 100, "Asim" : 2000, "Asdaq" : 3000, "Ali" : 4000}
fig, ax =  plt.subplots() 
ax.bar(x.keys(),x.values())
ax.set(title = " Age", xlabel = "Name", ylabel = "Years")
plt.show()

#### Horizontal Bar Graph
x = {"Shahab" : 100, "Asim" : 2000, "Asdaq" : 3000, "Ali" : 4000}
fig, ax =  plt.subplots()
ax.barh(list(x.keys()), list(x.values()))
ax.set(title = " Age", xlabel = "Name", ylabel = "Years")
plt.show();

####### SUBPLOT WAY #1
fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(nrows=2,ncols=2, figsize =(10,10))
ax1.plot(x,y)
ax2.scatter(x,y)
ax3.bar(x,y)
ax4.hist(np.random.randn(1000))
plt.show();

####option 2 for subplots
fig, ax = plt.subplots(nrows=2,ncols=2, figsize = (10,5))
ax[0,0].plot(x,y)
ax[0,1].scatter(x,y)
ax[1,0].bar(x,y)
ax[1,1].barh(x,y)
plt.show()


plot cumulative data
df2 = pd.Series(np.random.randn(1000), index = pd.date_range('1/1/2022', periods = 1000))
df2 = df2.cumsum()
df2.plot()
plt.show()

#######Plotting from Pandas Data Frames
df  = pd.read_csv('007 car-sales.csv')
df["Price"] = df["Price"].str.replace('[\$\,\.]', '')
df["Price"] = df["Price"].str[:-2]
print(df)
df["sale_date"] = pd.date_range('1/1/2020',periods = len(df))
print(df)
df.Price =  df.Price.astype(int)
df["Total_Sales"] =  df.Price.cumsum()
print(df)
df.plot(x="sale_date",y= "Total_Sales", kind = "bar")
plt.show()


x= np.random.rand(10,4)
df = pd.DataFrame(x,columns = ['a','b','c','d'])
print(df)
df.plot.bar();
plt.show();
