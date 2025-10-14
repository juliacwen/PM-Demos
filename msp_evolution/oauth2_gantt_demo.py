# oauth2_gantt_demo.py
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

def render_oauth2_gantt():
    st.subheader("OAuth 2.0 Project Plan — Professional Waterfall Gantt")

    project_start = datetime(2025, 5, 1)

    # Tasks with realistic durations
    tasks = [
        {"Task": "Gather Requirements", "Start": project_start, "Finish": project_start + timedelta(days=5), "Resource": "PM / Security Architect"},
        {"Task": "Design OAuth Flows & Token Strategy", "Start": project_start + timedelta(days=5), "Finish": project_start + timedelta(days=10), "Resource": "Solution Architect"},
        {"Task": "Authorization Server Implementation", "Start": project_start + timedelta(days=10), "Finish": project_start + timedelta(days=52), "Resource": "Dev / DevOps"},  # 6 weeks
        {"Task": "  • Setup DB & Storage", "Start": project_start + timedelta(days=10), "Finish": project_start + timedelta(days=16), "Resource": "Dev / DevOps"},
        {"Task": "  • Token Endpoint & Flows", "Start": project_start + timedelta(days=16), "Finish": project_start + timedelta(days=36), "Resource": "Dev / DevOps"},
        {"Task": "  • Logging & Security Hardening", "Start": project_start + timedelta(days=36), "Finish": project_start + timedelta(days=52), "Resource": "Dev / DevOps"},
        {"Task": "Integrate Client Applications", "Start": project_start + timedelta(days=30), "Finish": project_start + timedelta(days=45), "Resource": "Dev / DevOps"},
        {"Task": "Testing: Auth Flows & Security", "Start": project_start + timedelta(days=45), "Finish": project_start + timedelta(days=52), "Resource": "QA / Security"},
        {"Task": "Deployment", "Start": project_start + timedelta(days=52), "Finish": project_start + timedelta(days=54), "Resource": "DevOps"},
        {"Task": "Maintenance & Monitoring", "Start": project_start + timedelta(days=54), "Finish": project_start + timedelta(days=70), "Resource": "DevOps / Security"},
    ]

    df = pd.DataFrame(tasks)

    color_discrete_map = {
        "PM / Security Architect": "#1f77b4",
        "Solution Architect": "#ff7f0e",
        "Dev / DevOps": "#2ca02c",
        "QA / Security": "#d62728",
        "DevOps": "#9467bd",
        "DevOps / Security": "#8c564b"
    }

    fig = px.timeline(
        df,
        x_start="Start",
        x_end="Finish",
        y="Task",
        color="Resource",
        height=800,
        color_discrete_map=color_discrete_map,
        title="OAuth 2.0 Implementation Gantt"
    )

    fig.update_yaxes(autorange="reversed")  # Top-down order
    fig.update_xaxes(tickformat="%b %d", tickangle=45)
    fig.update_layout(
        font=dict(size=14),
        margin=dict(l=40, r=40, t=50, b=100),
        bargap=0.25,
        legend=dict(
            title="Resource",
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="right",
            x=1
        )
    )

    st.plotly_chart(fig, use_container_width=True)

    # Task details
    st.markdown("### Task Details")
    for t in tasks:
        st.markdown(f"- **{t['Task']}** ({t['Resource']}): {t['Start'].strftime('%b %d')} → {t['Finish'].strftime('%b %d')}")
