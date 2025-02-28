import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# App Title
st.title("💰 SmithBudget - Your Personal Finance Companion")

# Mission Statement
st.markdown(
    "**Our Mission:** SmithBudget is designed to help you take control of your finances with an easy-to-use budget calculator. "
    "We believe that financial freedom starts with a clear plan. Let’s build yours today!"
)

# User Inputs
income = st.number_input("Enter your monthly income ($)", min_value=0, value=5000, step=100)

# Expense Categories
st.subheader("Enter Your Monthly Expenses")
categories = ["Housing", "Utilities", "Groceries", "Transportation", "Entertainment", "Savings", "Debt Payments"]
expenses = {cat: st.number_input(f"{cat} ($)", min_value=0, value=0, step=10) for cat in categories}

# Calculate Total Expenses & Budget Allocation
total_expenses = sum(expenses.values())
remaining = income - total_expenses

# Budget Recommendation (50/30/20 Rule)
needs = income * 0.50
wants = income * 0.30
savings = income * 0.20

# Display Results
st.subheader("💡 Budget Summary")
st.write(f"Total Expenses: **${total_expenses}**")
st.write(f"Remaining Balance: **${remaining}**")
st.write("📊 Recommended Allocation:")
st.write(f"🏠 Needs (50%): **${needs:.2f}**")
st.write(f"🎭 Wants (30%): **${wants:.2f}**")
st.write(f"💰 Savings (20%): **${savings:.2f}**")

# Alerts if overspending
if total_expenses > income:
    st.error("⚠️ You're overspending! Consider adjusting your budget.")

# Pie Chart
fig, ax = plt.subplots()
ax.pie([needs, wants, savings], labels=["Needs", "Wants", "Savings"], autopct="%1.1f%%", startangle=90)
ax.set_title("Recommended Budget Allocation")
st.pyplot(fig)

# Financial Advice Based on Budget Categories
st.subheader("📢 Financial Advice")
if remaining < 0:
    st.warning("You're spending more than you earn! Consider cutting discretionary expenses and prioritizing essential needs.")
elif remaining < income * 0.10:
    st.info("You're barely saving. Try to allocate more towards savings to build financial security.")
elif remaining >= income * 0.10 and remaining < income * 0.25:
    st.success("You're doing well! Consider investing or increasing retirement contributions.")
elif remaining >= income * 0.25 and remaining < income * 0.50:
    st.success("Great job! You have a strong financial cushion. Explore investment opportunities.")
elif remaining >= income * 0.50:
    st.balloons()
    st.success("Excellent! You have a significant surplus. Consider diversifying investments or early retirement planning.")

