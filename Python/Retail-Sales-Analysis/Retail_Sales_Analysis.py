import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as pt
import seaborn as sns
from openpyxl.styles.alignment import vertical_aligments


pr=pd.read_csv('INT_products.csv')
cs=pd.read_csv('INT_customers.csv')
sl=pd.read_csv('INT_sales.csv')
ep=pd.read_csv('INT_employees.csv')
br=pd.read_csv('INT_branches.csv')
mr=pd.read_csv('INT_marketing.csv')

pr=pd.DataFrame(pr)
cs=pd.DataFrame(cs)
sl=pd.DataFrame(sl)
ep=pd.DataFrame(ep)
br=pd.DataFrame(br)
mr=pd.DataFrame(mr)
# print(pr.columns)
# print(cs.columns)
# print(sl.columns)
# print(ep.columns)
# print(br.columns)
# print(mr.columns)

font2={'family':'Times New Roman','color':'#006400','size':15,'weight':'light'}
font3={'family':'Times New Roman','color':'#003366','size':12,'weight':'light'}

# 1.How did total sales change month by month during 2024?
# print(sl['sale_date'])
# print(sl.dtypes)
sl['sale_date']=pd.to_datetime(sl['sale_date'])
sl['sale_month']=sl['sale_date'].dt.month
sm=sl.groupby('sale_month')['total'].sum().reset_index()
# print(sm)
x1=sm['sale_month']
y1=sm['total']/100000
v_y1=sm['total']
pt.subplot(1,2,1)
pt.plot(x1,v_y1,color='black',marker='o',mfc='red')
pt.xlabel('Sales Month',fontdict=font3)
pt.ylabel('Total Sales',fontdict=font3)
pt.title('Total Sales change month by month',fontdict=font2)
for i in range(len(x1)):
    pt.text(x1[i],v_y1[i],str(f"{y1[i]:.2f}L"))


#2. Which months recorded the highest and lowest total revenue?
# sl['sale_date']=pd.to_datetime(sl['sale_date'])
# sl['sale_month']=sl['sale_date'].dt.month
hl=sl.groupby('sale_month')['total'].sum().reset_index()
# print(sm)
x2=hl['sale_month']
y2=hl['total']/100000
v_y2=hl['total']
pt.subplot(1,2,2)
pt.bar(x2,v_y2,color='grey')
pt.xlabel('Sales Month',fontdict=font3)
pt.ylabel('Total Sales',fontdict=font3)
pt.title('Highest and lowest total revenue',fontdict=font2)
for i in range(len(x2)):
    pt.text(x2[i],v_y2[i],str(f"{y2[i]:.2f}L"))

pt.suptitle('Sales Analysis Report',family='Times New Roman',color='#003366',size=20,weight='light')
pt.show()


# 3.What is the average order value per month across all sales?
sl['sale_date']=pd.to_datetime(sl['sale_date'])
sl['sale_month']=sl['sale_date'].dt.month
avg=sl.groupby('sale_month')['total'].mean().reset_index()
# print(sm)
x3=avg['sale_month']
y3=avg['total']/1000
v_y3=avg['total']
pt.subplot(1,2,1)
pt.bar(x3,v_y3,color='lightblue')
pt.xlabel('Sales Month',fontdict=font3)
pt.ylabel('Average Sales',fontdict=font3)
pt.title('Average sales per month',fontdict=font2)
for i in range(len(x3)):
    pt.text(x3[i],v_y3[i],str(f"{y3[i]:.0f}K"),verticalalignment='top')



#4. How does the total quantity sold vary month by month?
# print(sl.columns)
qty=sl.groupby('sale_month')['quantity'].sum().reset_index()
# print(sm)
x4=qty['sale_month']
y4=qty['quantity']
pt.subplot(1,2,2)
pt.bar(x4,y4,color='pink')
pt.xlabel('Sales Month',fontdict=font3)
pt.ylabel('Quantity Sales',fontdict=font3)
pt.title('Total quantity sold vary month by month',fontdict=font2)
for i in range(len(x4)):
    pt.text(x4[i],y4[i],str(y4[i]))


pt.suptitle('Sales Analysis Report',family='Times New Roman',color='#003366',size=20,weight='light')
pt.show()

# 5.Which 3 Categories generated the highest revenue?
ps=pd.merge(pr,sl,on='product_id')
# print(ps[['product_name','category']])
# print(ps.columns)
psh=ps.groupby('category')['total'].sum().sort_values(ascending=False).head(3).reset_index()
# print(psh)
x5=psh['category']
y5=psh['total']
pt.subplot(1,2,1)
pt.plot(x5,y5,color='black',marker='o',mfc='orange',linestyle='')
pt.xlabel('Category name',fontdict=font3)
pt.ylabel('High Revenue',fontdict=font3)
pt.title('Top 3 Highest Revenue per category',fontdict=font2)
for i in range(len(x5)):
    pt.text(x5[i], y5[i], str(y5[i]))


# 6.Which 2 Categories generated the lowest revenue?
psl=ps.groupby('category')['total'].sum().sort_values(ascending=False).tail(2).reset_index()
# print(psl)
# print(psh)
x6=psl['category']
y6=psl['total']
pt.subplot(1,2,2)
pt.plot(x6,y6,color='black',marker='o',mfc='red',linestyle='')
pt.xlabel('Category name',fontdict=font3)
pt.ylabel('Lowest Revenue',fontdict=font3)
pt.title('Top 2 Lowest Revenue per category',fontdict=font2)
for i in range(len(x6)):
    pt.text(x6[i], y6[i], str(y6[i]),horizontalalignment='center')

pt.suptitle('Sales Analysis Report',family='Times New Roman',color='#003366',size=20,weight='light')
pt.show()

# 7.Highest and Lowest sold products in before categories?
pss=pd.merge(pr,sl,on='product_id')
psp=pss[pss['category'].isin(['Sports','Electronics','Home'])]
ps_id=psp.groupby(['category','product_id'])['total'].sum().reset_index()
sports=ps_id[ps_id['category']=='Sports']
Electronics=ps_id[ps_id['category']=='Electronics']
Home=ps_id[ps_id['category']=='Home']
sp_h=sports.sort_values('total',ascending=False).head(1)
el_h=Electronics.sort_values('total',ascending=False).head(1)
ho_h=Home.sort_values('total',ascending=False).head(1)
# print(sp_h)
fin=pd.concat([sp_h,el_h,ho_h],ignore_index=True)
# print(fin)
x7=fin['category']
y7=fin['total']
pt.bar(x7,y7,color='green',width=0.3)
pt.xlabel('Category name',fontdict=font3)
pt.ylabel('Total Revenue',fontdict=font3)
for i in range(len(x7)):
    pt.text(x7[i], y7[i], str(y7[i]))

psl=pss[pss['category'].isin(['Clothing','Grocery'])]
psl_id=psl.groupby(['category','product_id'])['total'].sum().reset_index()
# print(psl_id)
clothing=psl_id[psl_id['category']=='Clothing']
grocery=psl_id[psl_id['category']=='Grocery']
cl_l=clothing.sort_values('total',ascending=False).tail(1)
gr_l=grocery.sort_values('total',ascending=False).tail(1)
fin_l=pd.concat([cl_l,gr_l],ignore_index=True)
# print(fin)
x8=fin_l['category']
y8=fin_l['total']
pt.bar(x8,y8,color='red',width=0.3)
pt.title('Highest and Lowest sold products in before categories',fontdict=font2)
for i in range(len(x8)):
    pt.text(x8[i], y8[i], str(y8[i]))

pt.suptitle('Sales Analysis Report',family='Times New Roman',color='#003366',size=20,weight='light')
pt.show()

# 8.Highest and lowest brand overall revenue?
brd=pd.merge(pr,sl,on='product_id')
# print(brh['brand'].unique())
brh=brd.groupby('brand')['total'].sum().sort_values(ascending=False).head(2).reset_index()
x9=brh['brand']
y9=brh['total']/100000
v_y9=brh['total']
pt.subplot(1,2,1)
pt.bar(x9,y9,color='red',width=0.3)
pt.plot(x9,v_y9,color='black',marker='o',mfc='green',linestyle=' ',markersize=10)
pt.xlabel('Brand name',fontdict=font3)
pt.ylabel('Total Revenue',fontdict=font3)
pt.title('Highest and lowest Revenue per Brands',fontdict=font2)
for i in range(len(x9)):
    pt.text(x9[i], v_y9[i], str(f"{y9[i]:.2f}L"),verticalalignment='top')

brl=brd.groupby('brand')['total'].sum().sort_values(ascending=False).tail(1).reset_index()
x10=brl['brand']
y10=brl['total']/100000
v_y10=brl['total']
pt.subplot(1,2,1)
pt.plot(x10,v_y10,color='black',marker='o',mfc='red',linestyle=' ',markersize=10)
pt.xlabel('Brand name',fontdict=font3)
pt.ylabel('Total Revenue',fontdict=font3)
for i in range(len(x10)):
    pt.text(x10[i], v_y10[i], str(f"{y10[i]:.2f}L"))

pt.ticklabel_format(style='plain',axis='y')


# 9.How are product prices distributed across the catalog?
bins=[1000,2000,3000,4000,5000,6000,7000]
# lab=['low','minimum','average','maximum','high']
# pr['range']=pd.cut(pr['price'],bins=bins,labels=lab)
pt.subplot(1,2,2)
pt.hist(pr['price'],bins=bins,ec='black',color='red',alpha=0.5)
pt.xlabel('Price Range',fontdict=font3)
pt.ylabel('Count',fontdict=font3)
pt.title('Product price distribution',fontdict=font2)
pt.suptitle('Sales Analysis Report',family='Times New Roman',color='#003366',size=20,weight='light')
pt.show()



# 10.How does product price relate to the quantity purchased.
pq=pd.merge(pr,sl,on='product_id')
# pri_qty=pq.groupby('quantity')
x11=pq['price']
y11=sl['quantity']
pt.scatter(x11,y11,c=y11,s=100,alpha=0.5,cmap='cool')
pt.xlabel('Price',fontdict=font3)
pt.ylabel('Quantity',fontdict=font3)
pt.title('Relation of Product price & Quantity purchased',fontdict=font2)
pt.colorbar(orientation='vertical')
pt.suptitle('Sales Analysis Report',family='Times New Roman',color='#003366',size=20,weight='light')
pt.show()


# 11.Which customer cities contribute the most to total sales?
sc=pd.merge(sl,cs,on='customer_id')
scp=sc.groupby('city')['total'].sum().reset_index()
# # print(scp)
x12=scp['city']
y12=scp['total']/100000
v_y12=scp['total']
pt.subplot(1,2,1)
pt.bar(x12,v_y12,color='orange',width=0.3)
pt.xlabel('Cities',fontdict=font3)
pt.ylabel('Total Revenue',fontdict=font3)
pt.title('Cities contribute the most to total sales',fontdict=font2)
for i in range(len(x12)):
    pt.text(x12[i], v_y12[i], str(f"{y12[i]:.2f}L"), verticalalignment='top')


# 12.What does the age distribution of customers look like?
bi=[18,25,30,35,40,45,50,55,60,65,70]
x13=cs['age']
pt.subplot(1,2,2)
pt.hist(x13,bins=bi,ec='black',color='blue',alpha=0.5)
pt.xlabel('Range of age',fontdict=font3)
pt.ylabel('Age',fontdict=font3)
pt.title('Age Distribution',fontdict=font2)
pt.suptitle('Sales Analysis Report',family='Times New Roman',color='#003366',size=20,weight='light')
pt.show()


# 13.Find the count of Membership and Non-Membership customers?
msp=pd.merge(sl,cs,on='customer_id')
msp['membership']=msp['membership'].fillna('Non-member')
mbt=msp.groupby('membership')['customer_id'].count().sort_values(ascending=False).tail(2).reset_index()
# print(mb)
x14=mbt['membership']
y14=mbt['customer_id']
pt.subplot(1,2,1)
pt.bar(x14,y14,color='purple',width=0.2)
pt.xlabel('Membership',fontdict=font3)
pt.ylabel('Count of Customers',fontdict=font3)
pt.title("Count of Membership and Non-Membership customers",fontdict=font2)
for i in range(len(x14)):
    pt.text(x14[i],y14[i],str(y14[i]))

mbh=msp.groupby('membership')['customer_id'].count().sort_values(ascending=False).head(1).reset_index()
x15=mbh['membership']
y15=mbh['customer_id']
pt.bar(x15,y15,color='purple',width=0.2,alpha=0.5)
pt.xlabel('Membership',fontdict=font3)
pt.ylabel('Count of Customers',fontdict=font3)
for i in range(len(x15)):
    pt.text(x15[i],y15[i],str(y15[i]))


# 14. How do different membership types and non-membership compare in terms of total spending?
msc=pd.merge(sl,cs,on='customer_id')
msc['membership']=msc['membership'].fillna('Non-member')
mst=msc.groupby('membership')['total'].sum().reset_index()
# print(mst)
x16=mst['membership']
y16=mst['total']/100000
v_y16=mst['total']
pt.subplot(1,2,2)
pt.bar(x16,v_y16,color='hotpink',width=0.3)
pt.xlabel('Membership',fontdict=font3)
pt.ylabel('Total amount spent',fontdict=font3)
pt.title('Total amount spent by Membership and Non-Membership customers',fontdict=font2)
for i in range(len(x16)):
    pt.text(x16[i],v_y16[i],str(f"{y16[i]:.2f}L"))

pt.ticklabel_format(style='plain', axis='y')
pt.suptitle('Sales Analysis Report',family='Times New Roman',color='#003366',size=20,weight='light')
pt.show()

# 15.How many new customers were acquired each quarter by city?
csq=pd.merge(sl,cs,on='customer_id')
csq['sale_date']=pd.to_datetime(csq['sale_date'])
csq['quarter']= csq['sale_date'].dt.quarter
# print(csq)
qct = csq.groupby(['quarter','city'])['customer_id'].count().reset_index()
# pt.subplot(1,2,2)
sns.barplot(data=qct, x='quarter', y='customer_id', hue='city')
pt.xlabel('Quarter',fontdict=font3)
pt.ylabel('New Customers',fontdict=font3)
pt.title('New Customers Acquired per Quarter (by City)',fontdict=font2)
pt.xticks([0,1,2,3,], ['Q1','Q2','Q3','Q4'])
pt.suptitle('Sales Analysis Report',family='Times New Roman',color='#003366',size=20,weight='light')
pt.show()

# 16.Which branch generates the highest revenue?
brs=sl.groupby('branch_id')['total'].sum().reset_index()
# print(brs)
x17=brs['branch_id']
y17=brs['total']/100000
v_y17=brs['total']
pt.subplot(1,2,1)
pt.plot(x17,v_y17,color='black',marker='o',mfc='red',ls='-')
pt.xlabel('Branches',fontdict=font3)
pt.ylabel('Total Revenue',fontdict=font3)
pt.title('Highest Revenue generates by Branches',fontdict=font2)
for i in range(len(x17)):
    pt.text(x17[i], v_y17[i], str(f"{y17[i]:.2f}L"), verticalalignment='top')

pt.xticks([1,2,3,4,5,6,7,8,9,10], ['Bran 1','Bran 2','Bran 3','Bran 4',
                                   'Bran 5','Bran 6','Bran 7','Bran 8','Bran 9','Bran 10'],rotation=45)


# 17.Which branch has the highest average order value?
high_avg=sl.groupby('branch_id')['total'].mean().reset_index()
x20=high_avg['branch_id']
y20=high_avg['total']/1000
v_y20=high_avg['total']
pt.subplot(1,2,2)
pt.plot(x20,v_y20,color='black',marker='o',mfc='red',ls='-')
pt.xlabel('Branches',fontdict=font3)
pt.ylabel('Average order value',fontdict=font3)
pt.title('Highest average order value by Branches',fontdict=font2)
for i in range(len(x20)):
    pt.text(x20[i], v_y20[i], str(f"{y20[i]:.2f}K"), verticalalignment='top')

pt.xticks([1,2,3,4,5,6,7,8,9,10], ['Bran 1','Bran 2','Bran 3','Bran 4',
                                   'Bran 5','Bran 6','Bran 7','Bran 8','Bran 9','Bran 10'],rotation=45)
pt.suptitle('Sales Analysis Report',family='Times New Roman',color='#003366',size=20,weight='light')
pt.show()


# 18.Who are the top 20 customers based on total purchase value?
top=pd.merge(sl,cs,on='customer_id')
top_gp=top.groupby(['customer_id','city'])['total'].sum().sort_values(ascending=False).head(20).reset_index()
# print(top_gp)
# print(v_y17)
sns.barplot(data=top_gp, x='customer_id', y='total', hue='city')
pt.xlabel('Customer ID',fontdict=font3)
pt.ylabel('Total Sales',fontdict=font3)
pt.title('Top 20 customers based on total purchase value',fontdict=font2)
pt.suptitle('Sales Analysis Report',family='Times New Roman',color='#003366',size=20,weight='light')
pt.show()

# 19.How do the different branch cities perform in terms of total revenue?
sl_br=pd.merge(sl,br,on='branch_id')
br_ct=sl_br.groupby('branch_city')['total'].sum().reset_index()
# print(br_ct)
x21=br_ct['branch_city']
y21=br_ct['total']/100000
v_y21=br_ct['total']
pt.subplot(1,2,1)
pt.bar(x21,v_y21,color='tab:purple')
pt.xlabel('Branch Cities',fontdict=font3)
pt.ylabel('Total revenue',fontdict=font3)
pt.title('Different branch cities perform in terms of total revenue',fontdict=font2)
for i in range(len(x21)):
    pt.text(x21[i], v_y21[i], str(f"{y21[i]:.2f}L"))

pt.ticklabel_format(style='plain',axis='y')

# 20.Which branch sells the highest quantity of products overall?
hqr=sl.groupby('branch_id')['quantity'].sum().reset_index()
# print(hqr)
x22=hqr['branch_id']
y22=hqr['quantity']
pt.subplot(1,2,2)
pt.bar(x22,y22,color='mediumseagreen')
pt.xlabel('Branches',fontdict=font3)
pt.ylabel('Total quantities sold',fontdict=font3)
pt.title('Different branches perform in terms of total quantites sold',fontdict=font2)
for i in range(len(x22)):
    pt.text(x22[i], y22[i], str(y22[i]))

pt.xticks([1,2,3,4,5,6,7,8,9,10], ['Bran 1','Bran 2','Bran 3','Bran 4',
                                   'Bran 5','Bran 6','Bran 7','Bran 8','Bran 9','Bran 10'],rotation=45)
pt.suptitle('Sales Analysis Report',family='Times New Roman',color='#003366',size=20,weight='light')
pt.show()

# 21.How many employees are working in each branch?
emp_c=ep.groupby('branch_id')['employee_id'].count().reset_index()
# print(emp_c)
x23=emp_c['branch_id']
y23=emp_c['employee_id']
pt.subplot(1,2,1)
sns.lineplot(x='branch_id', y='employee_id', data=emp_c)
pt.xlabel('Branches',fontdict=font3)
pt.ylabel('Count of employees',fontdict=font3)
pt.title("Count of employees working in each branch",fontdict=font2)
for i in range(len(x23)):
    pt.text(x23[i], y23[i], str(y23[i]))

pt.xticks([1,2,3,4,5,6,7,8,9,10], ['Bran 1','Bran 2','Bran 3','Bran 4',
                                   'Bran 5','Bran 6','Bran 7','Bran 8','Bran 9','Bran 10'],rotation=45)


# 22.What is the distribution of employee roles within the company?
cp=ep
cp['role_d']=cp['role']
epr_c=cp.groupby(['role','role_d'])['employee_id'].count().reset_index()
# print(epr_c)
pt.subplot(1,2,2)
x24=epr_c['role']
y24=epr_c['employee_id']
sns.barplot(data=epr_c, x='role', y='employee_id', palette='viridis',hue='role_d', edgecolor='black')
pt.xlabel("Employee Role",fontdict=font3)
pt.ylabel("Count",fontdict=font3)
pt.title("Distribution of Employee Roles",fontdict=font2)
for i in range(len(y24)):
    pt.text(x24[i], y24[i], str(y24[i]))
# pt.xticks(rotation=45)
pt.suptitle('Sales Analysis Report',family='Times New Roman',color='#003366',size=20,weight='light')
pt.show()

# 23.How are employee salary distributed?
bin1=[15000,20000,25000,30000,35000,40000,45000,50000,55000,60000,65000,70000,75000]
# print(ep['salary'].max())
x25=ep['salary']
pt.hist(x25,bins=bin1,ec='black',color='tab:olive')
pt.xlabel('Range of Salary',fontdict=font3)
pt.ylabel('Salary Distribution',fontdict=font3)
pt.title('Employee Salary Distribution',fontdict=font2)
pt.suptitle('Sales Analysis Report',family='Times New Roman',color='#003366',size=20,weight='light')
pt.show()

# 24.Which employee roles have the highest average salaries?
avg_hs=ep.groupby('role')['salary'].mean().reset_index()
# print(avg_hs)
x26=avg_hs['role']
y26=avg_hs['salary']/1000
v_y26=avg_hs['salary']
pt.subplot(1,2,1)
pt.bar(x26,v_y26,color='tab:orange',width=0.4,alpha=0.5)
pt.xlabel('Roles',fontdict=font3)
pt.ylabel('Salaries',fontdict=font3)
pt.title('Employee roles highest & lowest average salaries',fontdict=font2)
for i in range(len(x26)):
    pt.text(x26[i], v_y26[i], str(f"{y26[i]:.2f}K"), verticalalignment='top')


# 25.How does branches spend amount for monthly marketing ad throughout the year?
mr['month']=pd.to_datetime(mr['month'])
mr['month_n']=mr['month'].dt.month
ad_sp=mr.groupby('month_n')['ad_spend'].sum().reset_index()
# print(ad_sp)
x27=ad_sp['month_n']
y27=ad_sp['ad_spend']/1000
v_y27=ad_sp['ad_spend']
pt.subplot(1,2,2)
pt.bar(x27, v_y27,color='tab:blue')
pt.xlabel('Months',fontdict=font3)
pt.ylabel('Amount spend for ad',fontdict=font3)
pt.title('Amount spend for ad throughout the year',fontdict=font2)
for i in range(len(x27)):
    pt.text(x27[i], v_y27[i], str(f"{y27[i]:.2f}K"))

pt.xticks([1,2,3,4,5,6,7,8,9,10,11,12], ['1','2','3','4','5','6','7','8','9','10','11','12'])
pt.suptitle('Sales Analysis Report',family='Times New Roman',color='#003366',size=20,weight='light')
pt.show()

# 26.How do monthly ad spend and monthly sales correlate?
sl['sale_date']=pd.to_datetime(sl['sale_date'])
sl['sl_mon']=sl['sale_date'].dt.month
# print(sl['sl_mon'])
ad_sl=sl.groupby('sl_mon')['total'].sum().reset_index()
# print(ad_sl)
ad_mr=mr.groupby('month_n')['ad_spend'].sum().reset_index()
# print(ad_mr)
corr_df=pd.merge(ad_sl, ad_mr, left_on='sl_mon',right_on='month_n')
# print(corr_df)
corr_df.rename(columns={'sl_mon':'month'}, inplace=True)
corr_df=corr_df[['ad_spend','total']]
pt.subplot(1,2,1)
sns.heatmap(corr_df.corr(), annot=True, cmap='viridis')
pt.title("Correlation Between Monthly Ad Spend & Monthly Sales",fontdict=font2)



# 27.Which marketing campaign type receives the most spending?
mr['cp_type']=mr['campaign_type']
mark_camp=mr.groupby(['campaign_type','cp_type'])['ad_spend'].sum().reset_index()
# print(mark_camp)
pt.subplot(1,2,2)
x28=mark_camp['cp_type']
y28=mark_camp['ad_spend']/100000
v_y28=mark_camp['ad_spend']
sns.barplot(x='campaign_type', y='ad_spend', data=mark_camp,hue='cp_type')
pt.title('Campaign Type and Amount Spend',fontdict=font2)
pt.xlabel('Campaign Type',fontdict=font3)
pt.ylabel('Amount Spend for Ad',fontdict=font3)
for i in range(len(x28)):
    pt.text(x28[i], v_y28[i], str(f"{y28[i]:.2f}L"))

pt.suptitle('Sales Analysis Report',family='Times New Roman',color='#003366',size=20,weight='light')
pt.ticklabel_format(style='plain',axis='y')
pt.show()

# 28.Which branch receives the highest marketing budget?
high_bud=mr.groupby('branch_id')['ad_spend'].sum().sort_values(ascending=False).head(1).reset_index()
# print(high_bud)
x29=high_bud['branch_id']
y29=high_bud['ad_spend']/100000
v_y29=high_bud['ad_spend']
pt.bar(x29, v_y29,color='tab:brown')
pt.xlabel('Branch',fontdict=font3)
pt.ylabel('Amount Spend for Ad',fontdict=font3)
pt.title('Branch that receives the highest marketing budget',fontdict=font2)
for i in range(len(x29)):
    pt.text(x29[i], v_y29[i], str(f"{y29[i]:.2f}L"))

low_bud=mr.groupby('branch_id')['ad_spend'].sum().sort_values(ascending=False).tail(6).reset_index()
x30=low_bud['branch_id']
y30=low_bud['ad_spend']/100000
v_y30=low_bud['ad_spend']
pt.bar(x30, v_y30,color='tab:brown',alpha=0.7)
pt.xlabel('Branches',fontdict=font3)
pt.ylabel('Amount Spend for Ad',fontdict=font3)
for i in range(len(x30)):
    pt.text(x30[i], v_y30[i], str(f"{y30[i]:.2f}L"))

pt.suptitle('Sales Analysis Report',family='Times New Roman',color='#003366',size=20,weight='light')
pt.xticks(range(1,11))
pt.ticklabel_format(style='plain',axis='y')
pt.show()

# 29.How are product price, quantity sold, and total sales amount related?
# Merge products with sales
sp =pd.merge(sl,pr,on='product_id')
# Select numerical columns for pairplot
pp=sp[['price','quantity','total']]
sns.pairplot(pp, diag_kind='kde')
# pt.title("Relationship Between Product Price, Quantity Sold & Total Sales")
pt.suptitle('Sales Analysis Report',family='Times New Roman',color='#003366',size=15,weight='light')
pt.show()

