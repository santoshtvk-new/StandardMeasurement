import streamlit as st
st.title("Unit Conversions")
st.subheader("Temperature")

sldr1 = st.slider('Celsius')
st.write(sldr1, 'degree Celsius in Fahrenheit -> ', sldr1 * 9/5 + 32)
st.write(sldr1, 'degree Celsius in Kelvin -> ', sldr1 + 273.15)

st.subheader("Length")
sldr2 = st.slider('Meters')
st.write(sldr2, 'Meters in Feet -> ', sldr2 * 3.281)
st.write(sldr2, 'Meters in Inch -> ', sldr2 * 39.37)
st.write(sldr2, 'Meters in Mile -> ', sldr2 / 1609)
st.write(sldr2, 'Meters in Yard -> ', sldr2 * 1.094)

st.subheader("Weight")
sldr3 = st.slider('Kilogram')
st.write(sldr3, 'Meters in Tonne -> ', sldr3 / 1000)
st.write(sldr3, 'Meters in Stone -> ', sldr3 / 6.35)
st.write(sldr3, 'Meters in Pound -> ', sldr3 * 2.205)
st.write(sldr3, 'Meters in Ounce -> ', sldr3 * 35.274)
