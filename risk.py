import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

#image
st.image("risk.png", use_column_width=True, caption="Program By: Marcus C. Rodriguez")

st.write("This quiz helps assess your financial risk tolerance. Please select the answer that best describes you.")

# Questions and scoring grid based on the PDF
questions = [
    ("In general, how would your best friend describe you as a risk taker?", ["A real gambler", "Willing to take risks after research", "Cautious", "A real risk avoider"], [4, 3, 2, 1]),
    ("You are on a TV game show and can choose one of the following. Which would you take?", ["\$1,000 in cash", "50% chance at \$5,000", "25% chance at \$10,000", "5% chance at \$100,000"], [1, 2, 3, 4]),
    ("You have just finished saving for a 'once-in-a-lifetime' vacation. Three weeks before you leave, you lose your job. You would:", ["Cancel the vacation", "Take a modest vacation", "Go as scheduled", "Extend your vacation"], [1, 2, 3, 4]),
    ("If you unexpectedly received \$20,000 to invest, what would you do?", ["Deposit in a bank account", "Invest in safe bonds", "Invest in stocks"], [1, 2, 3]),
    ("In terms of experience, how comfortable are you investing in stocks?", ["Not at all comfortable", "Somewhat comfortable", "Very comfortable"], [1, 2, 3]),
    ("When you think of the word 'risk', which word comes to mind first?", ["Loss", "Uncertainty", "Opportunity", "Thrill"], [1, 2, 3, 4]),
    ("Experts predict that hard assets (gold, real estate) will increase in value while bonds may fall. What would you do?", ["Hold bonds", "Sell bonds and split proceeds", "Sell bonds and buy hard assets", "Sell bonds, buy hard assets, and borrow more"], [1, 2, 3, 4]),
    ("Given the best and worst case returns of these investments, which do you prefer?", ["\$200 gain-best vs \$0 loss-worst", "\$800 gain-best vs \$200 loss-worst", "\$2,600 gain-best vs \$800 loss-worst", "\$4,800 gain-best vs \$2,400 loss-worst"], [1, 2, 3, 4]),
    ("You receive \$1,000 and must choose:", ["A sure gain of \$500", "50% chance to gain \$1,000"], [1, 3]),
    ("You receive \$2,000 and must choose:", ["A sure loss of \$500", "50% chance to lose \$1,000"], [1, 3]),
    ("You inherit \$100,000 and must invest in one option:", ["Savings account", "Mutual fund (stocks & bonds)", "Portfolio of 15 stocks", "Commodities (gold, oil, etc.)"], [1, 2, 3, 4]),
    ("If you had to invest \$20,000, which investment breakdown is most appealing?", ["60% low-risk, 30% medium-risk, 10% high-risk", "30% low-risk, 40% medium-risk, 30% high-risk", "10% low-risk, 40% medium-risk, 50% high-risk"], [1, 2, 3]),
    ("Your geologist friend is forming an exploratory gold mining venture with a 20% success rate. How much would you invest?", ["Nothing", "One month's salary", "Three month's salary", "Six month's salary"], [1, 2, 3, 4])
]

# Initialize user answers
scores = []

# Display questions
for i, (question, options, score_values) in enumerate(questions):
    response = st.radio(question, options, key=f"q{i}")
    selected_score = score_values[options.index(response)]
    scores.append(selected_score)

# Calculate total score
total_score = sum(scores)

# Interpretation of risk score
if total_score <= 18:
    risk_level = "Low Risk Tolerance (Conservative Investor)"
    risk_color = "green"
elif 19 <= total_score <= 22:
    risk_level = "Below-Average Risk Tolerance"
    risk_color = "yellowgreen"
elif 23 <= total_score <= 28:
    risk_level = "Moderate Risk Tolerance"
    risk_color = "yellow"
elif 29 <= total_score <= 32:
    risk_level = "Above-Average Risk Tolerance"
    risk_color = "orange"
else:
    risk_level = "High Risk Tolerance (Aggressive Investor)"
    risk_color = "red"

# Display score and interpretation
st.markdown(
    "<hr style='border: 5px solid; border-image-source: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet); border-image-slice: 1;'>",
    unsafe_allow_html=True,
)

st.subheader(f"Your Risk Tolerance Score: {total_score}")
st.markdown(f"**{risk_level}**")

# Generate risk visualization
fig, ax = plt.subplots(figsize=(8, 1))
ax.set_xlim(0, 47)
ax.set_ylim(0, 1)
ax.set_xticks([5, 15, 25, 35, 47])
ax.set_xticklabels(["Low", "Below Avg", "Moderate", "Above Avg", "High"], fontsize=10)
ax.set_yticks([])

# Define gradient (Fixing color inversion)
cmap = plt.get_cmap("RdYlGn_r")  # REVERSED color scale (green → red)
norm_score = min(max((total_score - 5) / (47 - 5), 0), 1)  # Normalize score to [0,1]
color = cmap(norm_score)

# Create a color bar
ax.axvspan(0, total_score, color=color, alpha=0.7)
ax.axvline(total_score, color='black', linewidth=2)

# Display plot
st.pyplot(fig)

# Reference
st.markdown("***Reference:***")
st.markdown("Grable, J. E., & Lytton, R. H. (1999). Financial risk tolerance revisited: The development of a risk assessment instrument. *Financial Services Review, 8*(3), 163-181.")

