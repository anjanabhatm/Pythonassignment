import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Page layout
st.set_page_config(page_title="Normal Distribution App", layout="wide")

# Sidebar
st.sidebar.header("Parameters")
mean = st.sidebar.number_input("Mean", value=0.0)
std_dev = st.sidebar.number_input("Standard Deviation", value=1.0)
num_samples = st.sidebar.number_input("Number of Samples", value=1000)

# Generate random data
np.random.seed(0)  # For reproducibility
data = np.random.normal(mean, std_dev, num_samples)

# Create a figure and axis for the histogram
fig, ax = plt.subplots()
ax.hist(data, bins=30, edgecolor="k")
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")
ax.set_title("Histogram of Generated Data")

# Display the plot using st.pyplot()
st.header("Histogram of Generated Data")
st.pyplot(fig)

# Download as CSV
if st.button("Download Data as CSV"):
    df = pd.DataFrame(data, columns=["Value"])
    csv = df.to_csv(index=False)
    st.download_button("Download CSV", data=csv, file_name="generated_data.csv")
