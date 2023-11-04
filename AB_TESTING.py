######################################################
# AB Testing
######################################################

import pandas as pd
from scipy.stats import shapiro, levene, ttest_ind

pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", lambda x: "%.5f" % x)


# 1. Set up Hypotheses
# 2. Assumption Check
# - 1st Normality Assumption (shapiro)
# Homogeneity of Variance (levene)
# Implementation of the Hypothesis
# Independent two sample t-test if assumptions are met
# Mannwhitneyu test if assumptions are not met
# 4. Interpret results according to p-value


#####################################################
# Preparing and Analysing the Data
#####################################################


# Read the data set named ab_testing_data.xlsx which consists of control and test group data. Assign control and test group data to separate variables.

control_df = pd.read_excel("ab_testing.xlsx", sheet_name="Control Group")
test_df = pd.read_excel("ab_testing.xlsx", sheet_name="Test Group")


# Adım 2: Kontrol ve test grubu verilerini analiz ediniz.
def check_df(dataframe, head=5):
    """
    It is the function that looks at the overall picture with the given dataframe

    Parameters
    ----------
    dataframe: dataframe

    head : function of dataframe

    Returns
    -------
    """

    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)


test_df(control_df)
test_df(test_df)

# Adım 3: Analiz işleminden sonra concat metodunu kullanarak kontrol ve test grubu verilerini birleştiriniz.
df = pd.concat([control_df.add_suffix("_control"), test_df.add_suffix("_test")], axis=1)
df.head()


# H0: M1=M2
# (There is no significant difference between M1 and M2.)

# H0: M1!=M2
# (There is a significant difference between M1 and M2.)

test_stat, pvalue = shapiro(df[["Purchase_test", "Purchase_control"]].dropna())
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))
# pvalue > 0.05


test_stat, pvalue = levene(df["Purchase_test"], df["Purchase_control"])
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))
# pvalue > 0.05


test_stat, pvalue = ttest_ind(
    df["Purchase_test"], df["Purchase_control"], equal_var=True
)
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))
# pvalue > 0.05

# --------------------- #
# There is no statistically significant difference.
# --------------------- #
