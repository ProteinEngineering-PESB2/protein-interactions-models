import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("seaborn-v0_8-white")
plt.rc('axes', grid=False, facecolor="white")
plt.rcParams.update({'font.size': 14})

df_train = pd.read_csv("response_train.csv")
df_test = pd.read_csv("response_test.csv")

fig, axes = plt.subplots(1, 2, figsize=(10, 8))

g1 = sns.scatterplot(ax=axes[0], data=df_train, x="Real values", y="Predictions")
axes[0].set_title("Training process")

# Draw a line of x=y 
x0 = min(df_train['Real values'])
x1 = max(df_train['Real values'])

y0 = min(df_train['Predictions'])
y1 = max(df_train['Predictions'])

lims = [min(x0, y0), max(x1, y1)]
g1.plot(lims, lims, '-r')

g2 = sns.scatterplot(ax=axes[1], data=df_test, x="Real values", y="Predictions")
axes[1].set_title("Testing process")

x0 = min(df_test['Real values'])
x1 = max(df_test['Real values'])

y0 = min(df_test['Predictions'])
y1 = max(df_test['Predictions'])

lims = [min(x0, y0), max(x1, y1)]
g2.plot(lims, lims, '-r')

plt.savefig("plot_real_testing.png", dpi=300)
