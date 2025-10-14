
# waterfall_pm_demo.py
import streamlit as st
import plotly.graph_objects as go
from msp_cloud_acronyms import ACRONYMS  # ensure your acronyms dict includes SRS, HLD, LLD, etc.


def render_waterfall_pm_demo():
    st.subheader("Waterfall Project Management — Typical Phases & PM Role")

    # Professional colors
    phase_colors = ["#4C72B0", "#55A868", "#C44E52", "#8172B2", "#CCB974", "#64B5CD"]

    # Waterfall phases
    phases = [
        {"phase": "Requirements", "description": "Gather all business, functional, and technical requirements upfront."},
        {"phase": "Design", "description": "Define architecture, system design, and specifications."},
        {"phase": "Implementation", "description": "Develop the actual product (coding, building, etc.)."},
        {"phase": "Verification (Testing)", "description": "Validate against requirements; QA ensures correctness."},
        {"phase": "Deployment", "description": "Deliver or release the final product to users."},
        {"phase": "Maintenance", "description": "Support, patch, and update post-deployment."},
    ]

    # Tuckman's Ladder
    tuckman_stages = [
        {"stage": "Forming", "desc": "Team meets and learns project context."},
        {"stage": "Storming", "desc": "Conflicts emerge; PM mediates roles."},
        {"stage": "Norming", "desc": "Team establishes norms and trust."},
        {"stage": "Performing", "desc": "Team executes effectively and collaboratively."},
        {"stage": "Adjourning", "desc": "Project closure, lessons learned, recognition."},
    ]

    # Acronyms
    ACRONYMS = {
        "SPI": "Schedule Performance Index",
        "CPI": "Cost Performance Index",
        "VAC": "Variance at Completion",
        "SRS": "Software Requirements Specification",
        "HLD": "High-Level Design",
        "LLD": "Low-Level Design",
    }

    # Key Documents
    key_documents = [
        "Project Charter / Plan — scope, objectives, milestones, timeline",
        "Requirements Specification (<span title='Software Requirements Specification' style='text-decoration: underline dotted; cursor: help;'>SRS</span>) — functional & non-functional needs",
        "Design Documents (<span title='High-Level Design Document' style='text-decoration: underline dotted; cursor: help;'>HLD</span> / <span title='Low-Level Design Document' style='text-decoration: underline dotted; cursor: help;'>LLD</span>) — high- and low-level designs",
        "Test Plans / Test Cases — verify deliverables",
        "Change Control Logs — track post-baseline changes",
    ]

    # PM Responsibilities
    pm_responsibilities = [
        "Develops and maintains a Gantt chart",
        "Manages dependencies, deliverables, and milestones",
        "Ensures each stage has formal sign-off",
        "Maintains scope and change control",
        "Reports progress using SPI, CPI, VAC",
        "Monitors milestone adherence",
    ]

    # Layout
    col1, col2 = st.columns([3, 1])

    with col1:
        n = len(phases)
        total_height = 0.85
        spacing_ratio = 0.15
        box_height = total_height / n * (1 - spacing_ratio)
        spacing = total_height / n * spacing_ratio
        y_start = 0.98
        x0 = 0.45

        fig = go.Figure()

        for i, step in enumerate(phases):
            y1 = y_start - i * (box_height + spacing)
            y0 = y1 - box_height
            color = phase_colors[i % len(phase_colors)]

            fig.add_shape(
                type="rect",
                x0=x0 - 0.35, x1=x0 + 0.35,
                y0=y0, y1=y1,
                line=dict(color="black", width=1.5),
                fillcolor=color,
            )

            fig.add_annotation(
                x=x0, y=y1 + 0.01,
                text=f"<b>{step['phase']}</b>",
                showarrow=False, font=dict(size=16, color="white"), xanchor="center"
            )

            fig.add_annotation(
                x=x0, y=(y0 + y1)/2,
                text=step["description"],
                showarrow=False, font=dict(size=14, color="white"),
                xanchor="center", yanchor="middle"
            )

            if i < n - 1:
                fig.add_annotation(
                    x=x0, y=y0 - 0.01,
                    ax=x0, ay=y0 + 0.01,
                    showarrow=True, arrowhead=3, arrowsize=1.5, arrowwidth=2, arrowcolor="black"
                )

        # Tuckman ladder aligned to right
        ladder_x = 0.92
        ladder_y_start = 0.9
        ladder_height = 0.10
        ladder_spacing = 0.04

        for i, stage in enumerate(tuckman_stages):
            y_top = ladder_y_start - i * (ladder_height + ladder_spacing)
            y_bottom = y_top - ladder_height
            fig.add_shape(
                type="rect",
                x0=ladder_x - 0.15, x1=ladder_x + 0.15,
                y0=y_bottom, y1=y_top,
                line=dict(color="black", width=1),
                fillcolor="#E6A157",
            )
            fig.add_annotation(
                x=ladder_x, y=(y_top + y_bottom)/2,
                text=f"<b>{stage['stage']}</b><br><span style='font-size:12px'>{stage['desc']}</span>",
                showarrow=False, xanchor="center", yanchor="middle",
                font=dict(size=13, color="white")
            )

        fig.update_xaxes(visible=False, range=[0,1])
        fig.update_yaxes(visible=False, range=[0,1])
        fig.update_layout(height=750, plot_bgcolor="white", paper_bgcolor="white", margin=dict(l=20, r=20, t=20, b=20))

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("### PM Responsibilities / Key Metrics")
        for r in pm_responsibilities:
            st.markdown(f"- {r}")

    with col2:
        st.markdown("### Acronyms")
        for k, v in ACRONYMS.items():
            st.markdown(f"- **{k}** — {v}")

        st.markdown("### Key Documents")
        for doc in key_documents:
            st.markdown(f"- {doc}", unsafe_allow_html=True)
