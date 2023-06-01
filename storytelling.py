import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import animation


def animate(year):
    plt.cla()
    ax.set_ylim(0, 3)
    ax.tick_params(axis='x', labelrotation=45)
    ax.set_title(f'Average years of tertiary schooling in {int(year)}')
    graph = sns.barplot(data=df[df.Year == year], x="Ages", y="Value", hue = "Gender")
    return graph

if __name__ == "__main__":
    st.title("Evolution of tertiary education in diferent countries along years")
    df = pd.read_csv("poland.csv")
    text = "Poland"
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        if st.button('Poland'):
            text = "Poland"
            df = pd.read_csv("poland.csv")
    with col2:
        if st.button("Australia"):
            text = "Australia"
            df = pd.read_csv("australia.csv")
    with col3:
        if st.button('Japan'):
            text = "Japan"
            df = pd.read_csv("australia.csv")

    col4, col5, col6 = st.columns([1,1,1])
    with col4:
        if st.button('France'):
            text = "France"
            df = pd.read_csv("france.csv")
    with col5:
        if st.button("Italy"):
            text = "Italy"
            df = pd.read_csv("italy.csv")
    with col6:
        if st.button('Korea'):
            text = "Korea"
            df = pd.read_csv("korea.csv")

    st.header(text)

    fig, ax = plt.subplots(figsize=(5, 7))
    plt.ylim(0,3)

    l, = plt.plot([], [], 'r-')
    #plt.title('Average years of tertiary schooling in ')
    anim = animation.FuncAnimation(fig, animate, frames = [1970., 1975., 1980., 1985., 1990., 1995., 2000., 2005., 2010.], interval = 500)
    #line_ani = animation.FuncAnimation(fig, animate, 25, fargs=(data, l), interval=50, blit=True)

    components.html(anim.to_jshtml(), height=1000)