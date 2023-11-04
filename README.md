# A/B Testing Analysis for Average Bidding vs. Maximum Bidding

This analysis focuses on comparing the performance of two bidding strategies: "average bidding" and "maximum bidding" in an A/B test scenario. The goal is to determine if the "average bidding" strategy leads to better results than "maximum bidding" based on the key metric of Purchase conversions.

## Key Metric: Purchase

The primary metric of interest in this A/B test analysis is "Purchase." We will assess whether the differences in bidding strategies have a significant impact on Purchase conversion rates.

## Analysis Steps

1. **Hypotheses Setup:** We establish the following hypotheses for the A/B test:

   - Null Hypothesis (H0): There is no significant difference in Purchase conversion rates between the "average bidding" (test) and "maximum bidding" (control) groups.
   - Alternative Hypothesis (H1): There is a significant difference in Purchase conversion rates between the "average bidding" (test) and "maximum bidding" (control) groups.
2. **Data Collection and Preparation:** We collect and prepare the data from the A/B test, ensuring it's clean and structured for analysis.
3. **Assumption Check:** To perform the A/B test, we validate two critical assumptions:

   - Normality Assumption: Using a normality test (e.g., Shapiro-Wilk), we check if the Purchase data follows a normal distribution.
   - Homogeneity of Variance: Using a variance homogeneity test (e.g., Levene), we verify if the variances of Purchase in both groups are equal.
4. **Implementation of the Hypothesis:** If both assumptions are met, we conduct an independent two-sample t-test to compare the Purchase conversion rates of the test and control groups. If the assumptions are not met, we opt for a non-parametric test.
5. **Interpretation of Results:** We interpret the results based on the p-value:

   - If the p-value is greater than 0.05, we fail to reject the null hypothesis, indicating no statistically significant difference in Purchase conversion rates between the groups.
   - If the p-value is less than or equal to 0.05, we reject the null hypothesis, suggesting a statistically significant difference in Purchase conversion rates.

## Analysis Outcome

This A/B testing analysis aims to provide insights into which bidding strategy, "average bidding" or "maximum bidding," is more effective in driving Purchase conversions. The results will inform data-driven decisions for optimizing bidding strategies in future.
