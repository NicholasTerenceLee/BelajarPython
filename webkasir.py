import streamlit as st

def calc(x, y, z):
    money = float((25000*x)+(10000*y)+(15000*z))
    return money

st.title("Cashier System")
st.write("Here's the list of items within this Shop : ")
a = st.number_input("Cigarettes", min_value = 0, step = 1)
b = st.number_input("Beer", min_value = 0, step = 1)
c = st.number_input("Lighter", min_value = 0, step = 1)

money = calc(a, b, c)
st.write('Is that all?')
if st.button("That's all!"):
    st.success(f"Your Total is : Rp {money}")
