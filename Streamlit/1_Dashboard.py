import streamlit as st
import pandas as pd
import plotly.express as px
import json

st.set_page_config(page_title="Mongolian General Entrance Exam Results Dashboard", layout="wide")
df = pd.read_csv("Streamlit/Combined Dataset.csv")

st.markdown("""
    <div style="background-color:#113f67;padding:15px;margin:-2rem -1rem 2rem -1rem;color:#58a0c8">
        <h1 style="color:#e6f6ff;text-align:center;font-size:36px">Mongolian University Entrance Exam Results Dashboard</h1>
    </div>
""", unsafe_allow_html=True)

col3, col4, col5, _, col1, col2 = st.columns(6)

with col1:
    region_options = ["All"] + sorted(df["Region"].dropna().unique().tolist())
    selected_region = st.selectbox("Select Region", region_options)

with col2:
    subject_options = ["All"] + sorted(df["Subject"].dropna().unique().tolist())
    selected_subject = st.selectbox("Select Subject", subject_options)

filtered_df = df.copy()
if selected_region != "All":
    filtered_df = filtered_df[filtered_df["Region"] == selected_region]
if selected_subject != "All":
    filtered_df = filtered_df[filtered_df["Subject"] == selected_subject]

with col3:
    st.metric("Average First Score", f"{filtered_df['Firstscore'].mean():.2f}")

with col4:
    st.metric("No. of Exam Results", f"{filtered_df.shape[0]}")

with col5:
    top_letter = (
        filtered_df["Letterindex"]
        .value_counts()
        .reindex(['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E', 'F'])
        .dropna()
        .idxmax()
    )
    st.metric("Top Letter Index", top_letter)

with open("Streamlit/mn.json", "r", encoding="utf-8") as f:
    geojson = json.load(f)

filtered_df["ISO_Code"] = filtered_df["ISO_Code"].str.replace("-", "")
plotly_data = filtered_df.groupby(["ISO_Code", "Region"]).size().reset_index(name="Exam Count")

scatter_col, table_col = st.columns([3, 2])

with scatter_col:
    st.markdown("<h3 style='font-size:22px;'><strong>First Score in Percentile by Subject</strong></h3>", unsafe_allow_html=True)

    subject_colors = {
        "Mathematics": "#76a9d3",
        "Physics": "#f7af7e",
        "Chemistry": "#7fc385",
        "Biology": "#e08082",
        "English": "#b6a0d8",
        "Mongolian language studies": "#f7b47d",
        "Geology": "#f6dfa9",
        "History": "#a8aeb2",
        "Social Study": "#dce5ef",
        "Russian": "#dce5ef"
    }

    bubble_df = (
        filtered_df.groupby(["Firstscore", "Percentile", "Subject"])
        .size()
        .reset_index(name="Count")
    )

    fig = px.scatter(
        bubble_df,
        x="Percentile",
        y="Firstscore",
        size="Count",
        color="Subject",
        color_discrete_map=subject_colors,
        opacity=0.6,
        size_max=10 
    )

    fig.update_layout(
    height=450,
    margin={"t": 10},
    font=dict(family="Arial", color="#113f67"),
    xaxis_title=dict(text="Percentile", font=dict(color="#113f67")),
    yaxis_title=dict(text="First Score", font=dict(color="#113f67")),
    xaxis=dict(tickfont=dict(color="#113f67"),title_font=dict(color="#113f67")),
    yaxis=dict(tickfont=dict(color="#113f67"),title_font=dict(color="#113f67")),
    legend=dict(title="Subject",title_font=dict(color="#113f67"),font=dict(color="#113f67"))
    )


    st.plotly_chart(fig, use_container_width=True)

with table_col:
    st.markdown("<h3 style='font-size:22px;'><strong>Score Requirements by Percentile</strong></h3>", unsafe_allow_html=True)
    percentiles = [(0.9, "90th"), (0.75, "75th"), (0.6, "60th"),
                   (0.5, "50th"), (0.4, "40th"), (0.25, "25th")]
    rows = []
    for subject, group in filtered_df.groupby("Subject"):
        for p_val, p_label in percentiles:
            firstscore = group["Firstscore"].quantile(p_val)
            convertedscore = group["Convertedscore"].quantile(p_val)
            rows.append({
                "Subject": subject,
                "Percentile": p_label,
                "Percentile Value": p_val,
                "First Score": round(firstscore, 2),
                "Converted Score": round(convertedscore, 2)
            })
    percentile_df = pd.DataFrame(rows)
    percentile_df = percentile_df.sort_values(
        by=["Subject", "Percentile Value"],
        ascending=[True, False]
    ).drop(columns="Percentile Value").reset_index(drop=True)
    st.dataframe(percentile_df, use_container_width=True, hide_index=True)

map_col, bar_col1, bar_col2, bar_col3 = st.columns([2, 1, 1, 1])

with map_col:
    st.markdown("<h3 style='font-size:22px;'><strong>Exam Results per Province Map</strong></h3>", unsafe_allow_html=True)
    fig = px.choropleth_mapbox(
        plotly_data,
        geojson=geojson,
        locations="ISO_Code",
        color="Exam Count",
        featureidkey="properties.id",
        mapbox_style="carto-positron",
        zoom=4.5,
        center={"lat": 46.86, "lon": 103.84},
        opacity=0.6,
        hover_name="Region",
        color_continuous_scale=["#e6f6ff", "#113f67"],
    )
    fig.update_layout(
        height=300,
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        coloraxis_showscale=False
    )
    st.plotly_chart(fig, use_container_width=True)

with bar_col1:
    st.markdown("<h3 style='font-size:22px; color:#113f67;'><strong>First Scores Distribution</strong></h3>", unsafe_allow_html=True)
    bins = list(range(0, 101, 10))
    firstscore_binned = pd.cut(filtered_df["Firstscore"], bins=bins, right=False, include_lowest=True)
    firstscore_df = firstscore_binned.value_counts().sort_index().reset_index()
    firstscore_df.columns = ["Score Range", "Count"]
    firstscore_df["Score Range"] = firstscore_df["Score Range"].astype(str)

    fig1 = px.bar(firstscore_df, x="Score Range", y="Count", color_discrete_sequence=["#113f67"])
    fig1.update_layout(
        margin={"t": 10},
        height=300,
        showlegend=False,
        xaxis_title="Score Range",
        yaxis_title="Count",
        font=dict(family="Arial", color="#113f67"),
        xaxis=dict(title_font=dict(size=14, color="#113f67"), tickfont=dict(size=10, color="#113f67")),
        yaxis=dict(title_font=dict(size=14, color="#113f67"), tickfont=dict(size=10, color="#113f67"))
    )
    st.plotly_chart(fig1, use_container_width=True)


with bar_col2:
    st.markdown("<h3 style='font-size:22px; color:#113f67;'><strong>Converted Scores Distribution</strong></h3>", unsafe_allow_html=True)
    bins_conv = list(range(200, 861, 60))
    converted_binned = pd.cut(filtered_df["Convertedscore"], bins=bins_conv, right=False, include_lowest=True)
    converted_df = converted_binned.value_counts().sort_index().reset_index()
    converted_df.columns = ["Score Range", "Count"]
    converted_df["Score Range"] = converted_df["Score Range"].astype(str)

    fig2 = px.bar(converted_df, x="Score Range", y="Count", color_discrete_sequence=["#113f67"])
    fig2.update_layout(
        margin={"t": 10},
        height=300,
        showlegend=False,
        xaxis_title="Score Range",
        yaxis_title="Count",
        font=dict(family="Arial", color="#113f67"),
        xaxis=dict(title_font=dict(size=14, color="#113f67"), tickfont=dict(size=10, color="#113f67")),
        yaxis=dict(title_font=dict(size=14, color="#113f67"), tickfont=dict(size=10, color="#113f67"))
    )
    st.plotly_chart(fig2, use_container_width=True)


with bar_col3:
    st.markdown("<h3 style='font-size:22px; color:#113f67;'><strong>Letter Index Distribution</strong></h3>", unsafe_allow_html=True)
    letter_order = ['F','E','D-','D','D+','C-','C','C+','B-','B','B+','A-','A']
    letter_df = (
        filtered_df["Letterindex"]
        .value_counts()
        .reindex(letter_order)
        .dropna()
        .reset_index()
    )
    letter_df.columns = ["Letter", "Count"]

    fig3 = px.bar(letter_df, x="Letter", y="Count", color_discrete_sequence=["#113f67"])
    fig3.update_layout(
        margin={"t": 10},
        height=300,
        showlegend=False,
        xaxis_title="Letter",
        yaxis_title="Count",
        font=dict(family="Arial", color="#113f67"),
        xaxis=dict(title_font=dict(size=14, color="#113f67"), tickfont=dict(size=10, color="#113f67")),
        yaxis=dict(title_font=dict(size=14, color="#113f67"), tickfont=dict(size=10, color="#113f67"))
    )
    st.plotly_chart(fig3, use_container_width=True)
