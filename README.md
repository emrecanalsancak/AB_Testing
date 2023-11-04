# A/B Testing Analysis

A/B testing, also known as split testing, is a method of comparing two versions of a webpage or app to determine which one performs better in terms of a specific goal or metric.

## Data Variables

- **Impression:** Number of ad views.
- **Click:** Number of clicks on the displayed ad.
- **Purchase:** Number of products purchased after the ads were clicked.
- **Earning:** Earnings generated after products were purchased.

## Analysis Steps

1. **Hypotheses Setup:** We set up two hypotheses for the A/B test:

   - Null Hypothesis (H0): There is no significant difference between the control and test groups in terms of the number of products purchased after ad clicks.
   - Alternative Hypothesis (H1): There is a significant difference between the control and test groups in terms of the number of products purchased after ad clicks.
2. **Assumption Check:** To perform the A/B test, we check two critical assumptions:

   - Normality Assumption: We use the Shapiro-Wilk test to check if the data follows a normal distribution.
   - Homogeneity of Variance: We use the Levene test to check if the variances of the two groups are equal.
3. **Implementation of the Hypothesis:** If both assumptions are met, we perform an independent two-sample t-test to compare the means of the control and test groups. If the assumptions are not met, we use the Mann-Whitney U test.
4. **Interpretation of Results:** We interpret the results based on the p-value:

   - If the p-value is greater than 0.05, we fail to reject the null hypothesis, indicating no statistically significant difference between the groups.
   - If the p-value is less than or equal to 0.05, we reject the null hypothesis, suggesting a statistically significant difference between the groups.

## Analysis Outcome

In the analysis performed on the data, the p-value for the A/B test was greater than 0.05, indicating that there is no statistically significant difference between the control and test groups in terms of the number of products purchased after changes. This suggests that the changes made in the test group did not result in a significant impact on purchase behavior.
