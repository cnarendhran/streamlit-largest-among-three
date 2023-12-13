import streamlit as st

# Define function to find the largest
def largest(a, b, c):
  return max(a, b, c)

# Create input fields for user to enter values
num1 = st.number_input("Enter first number:", key="num1")
num2 = st.number_input("Enter second number:", key="num2")
num3 = st.number_input("Enter third number:", key="num3")

# Calculate the largest
largest_num = largest(num1, num2, num3)

# Display the result
st.write(f"The largest number is: {largest_num}")
