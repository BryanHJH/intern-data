import pandas as pd
from plotly_calplot import calplot

df = pd.read_csv('CRM-GRN-PO-Better.csv')
df['CreatedDate'] = pd.to_datetime(df['CreatedDate'])
df_test = df[["CreatedDate", "PurchaseOrder"]]
df_group = pd.DataFrame(df_test.groupby(['CreatedDate', 'PurchaseOrder']).size())
df_group.reset_index(inplace=True)
df_group.rename(columns = {0: 'Count'}, inplace=True)
fig = calplot(df_group, x='CreatedDate', y='Count', name="Purchase Orders", years_title=True, showscale=True, gap=1)
fig.write_html("index.html")