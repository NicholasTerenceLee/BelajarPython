import streamlit as st

def BALLOONS():
    st.balloons()
    st.balloons()
    st.balloons()
    st.balloons()
    st.balloons()
    st.balloons()
    st.balloons()
    st.balloons()
    st.balloons()
    st.balloons()

def square(side):
    luas = side*side
    keliling = 4*side
    return luas, keliling

def rectangle(length, width):
    luas = length*width
    keliling = 2*(length*width)
    return luas, keliling

def triangle(base, height, side):
    luas = 0.5*base*height
    keliling = 3*side
    return luas, keliling
list = ['Square', 'Rectangle', 'Triangle']
st.title("2D Shapes Calculator")
shape = st.selectbox("Choose a shape : " , list)

if shape == "Square":
    side = st.number_input("Size of Side : ", min_value=0)
    if st.button("Calculate!"):
        luas, keliling = square(side)
        st.success(f"Area of Square : {luas}")
        st.info(f"Circumference of Square : {keliling}")

if shape == "Rectangle":
    length = st.number_input("Size of Length : ", min_value=0)
    width = st.number_input("Size of Width : ", min_value=0)
    if st.button("Calculate!"):
        luas, keliling = rectangle(length, width)
        st.success(f"Area of Rectangle : {luas}")
        st.info(f"Circumference of Rectangle : {keliling}")

if shape == "Triangle":
    base = st.number_input("Size of Base : ", min_value=0)
    height = st.number_input("Size of Height : ", min_value=0)
    side = st.number_input("Size of Side : ", min_value=0)
    if st.button("Calculate!"):
        luas, keliling = triangle(base, height, side)
        st.success(f"Area of Triangle : {luas}")
        st.info(f"Circumference of Triangle : {keliling}")
