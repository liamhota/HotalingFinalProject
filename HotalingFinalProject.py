'''
Class: CS230--Section 3
Name: Liam Hotaling
Description: Final Project
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student
'''

import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv("VolcanoesData.csv") #main df
df2 = df[["Volcano Name", "Latitude", "Longitude"]].rename(columns={"Latitude": "lat", "Longitude": "lon"}) # for map, also had to look up how to do this since map wasn't working

st.title("Liam Hotaling Final Project CS 230")

def eruptions_by_region():
    st.write("Eruptions by Volcanic Region")
    regions = [
        "European Volcanic Regions", "Southwest Pacific Volcanic Regions","Sunda-Banda Volcanic Regions", "Northwest Pacific Volcanic Regions", "North America Volcanic Regions",
    ]
    countOfEruptions = df["Volcanic Region"].value_counts().reindex(regions, fill_value=0) # had to look up how to do this part, graph wasn't working as intended
    bars = [countOfEruptions.get(x, 0) for x in regions]

    fig, ax = plt.subplots()
    ax.bar(range(len(regions)), bars, color='b')
    ax.set_xlabel('Volcanic Region')
    ax.set_ylabel('Num of Eruptions')
    ax.set_title('Eruptions by Volcanic Region')
    ax.set_xticks(range(len(regions)))
    ax.set_xticklabels(regions, rotation=45, ha='right') # had to look this up too, names of regions were overlapping and unreadable
    st.pyplot(fig)

def eruption_map():
    st.write("Map of Eruptions")
    st.map(df2)

def main():
    eruptions_by_region()
    print()
    eruption_map()

main()