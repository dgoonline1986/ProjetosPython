
import pandas as pd

import pandasql as ps




df1 = pd.DataFrame([[1234, 'Customer A', '123 Street'],

               [1234, 'Customer A', '333 Street'],

               [1233, 'Customer B', '444 Street', '333 Street'],

              [1233, 'Customer B', '444 Street', '666 Street']], columns=

['ID', 'Customer', 'Billing', 'Shipping'])




q1 = """SELECT ID, Customer, Billing FROM df1 ORDER BY Billing"""




df2 = pd.read_csv(r'C:\Users\dnsilva2\OneDrive - Stefanini\Documents\Pandas\aluguel.csv', sep=';')


#df2.head()

q2 = """SELECT * FROM df2 ORDER BY Tipo"""




print(ps.sqldf(q1, locals()))

print(ps.sqldf(q2, locals()))