# ---------------------------------------------------------
# cloud_pm_dashboard.py
# Cloud Migration Dashboard — Streamlit + Plotly
# Author: Julia Wen (wendigilane@gmail.com)
# Date: 10-06-2025
#
# Description:
#   Interactive dashboard for cloud migration project, displays three diagram types:
#     * Flow Diagram (Lifecycle) — boxes with phase tasks and arrows
#     * Hierarchical WBS Tree — top-down tree with phases and tasks
#     * Swimlane Chart — tasks per phase × role with role-based colors
#
# Dependencies:
#   - streamlit
#   - plotly
#
# Usage:
#   1. Run in terminal:  streamlit run cloud_pm_dashboard.py
#   2. Use dropdown menu to switch between diagrams.
#
# Notes:
#   - Dark theme is default; a Light/Dark toggle is provided.
#   - All diagrams are programmatically drawn with Plotly shapes & annotations.
#   - Designed to run without Graphviz/diagrams package.
# ---------------------------------------------------------

import streamlit as st
import plotly.graph_objects as go
import textwrap

# ---------------------------
# Config & Styles
# ---------------------------
st.set_page_config(page_title="☁️ Cloud Migration Dashboard", layout="wide")

# Sidebar controls (theme and diagram selector)
with st.sidebar:
    st.title("☁️ Cloud Migration")
    theme = st.selectbox("Theme", ["Dark", "Light"])
    diagram_type = st.selectbox(
        "Diagram",
        ["Flow Diagram (Lifecycle)", "Hierarchical WBS Tree", "Swimlane Chart"],
    )
    st.markdown("---")
    st.caption("Professional palette | role-based colors | responsive layout")

# Choose color palette based on theme
PROFESSIONAL_PALETTE = {
    "flow_box": "#1F77B4",  # steel blue
    "flow_fill": "#A9C6EA",
    "wbs_root": "#234E70",
    "wbs_node": "#99CCFF",
    "lane_colors": {
        "Project Coordinator": "#2B5D8A",
        "Cloud Engineer": "#16789B",
        "Security Engineer": "#1F8A70",
        "Client IT Lead": "#4C6A88",
    },
    "text": "#FFFFFF" if theme.startswith("Dark") else "#111111",
    "bg": "#0f1720" if theme.startswith("Dark") else "#FFFFFF",
}

# Apply background (Streamlit can't change full page BG reliably, but we set plot bgs)
PLOT_BG = PROFESSIONAL_PALETTE["bg"]
TEXT_COLOR = PROFESSIONAL_PALETTE["text"]

# ---------------------------
# Helpers
# ---------------------------
def wrap_lines(text, width):
    """Return list of wrapped lines for given text (preserve manual newlines)."""
    out = []
    if text is None:
        return out
    for para in str(text).splitlines():
        if para.strip() == "":
            out.append("")
        else:
            out.extend(textwrap.wrap(para, width=width) or [""])
    return out

# ---------------------------
# Data (phases, roles, tasks)
# ---------------------------
PHASES_FLOW = [
    ("Assessment", ["Inventory tracking", "Risk register", "Policy approval"]),
    ("Design", ["Architecture design", "Encryption & network planning", "Validate design policies"]),
    ("Migration", ["Configure cloud services", "Execute migration", "Migration checkpoints"]),
    ("Validation", ["Support testing", "Penetration & compliance testing", "UAT sign-off"]),
    ("Closure", ["Document lessons learned", "Decommission environments", "Finalize security logs"]),
]

WBS_PHASES = [
    ("1. Planning", ["Inventory of applications & data", "Risk register", "Policy approval"]),
    ("2. Design", ["Architecture & compliance", "Encryption & network planning", "Validate design policies"]),
    ("3. Build", ["Configure cloud services", "Firewall setup", "Key management"]),
    ("4. Migration", ["Execute migration", "Monitor security", "Approve checkpoints"]),
    ("5. Validation", ["Test coordination", "Penetration & compliance testing", "Sign-off UAT"]),
    ("6. Closure", ["Document lessons learned", "Decommission test environments", "Confirm compliance"]),
]

SWIMLANE_ROLES = ["Project Coordinator", "Cloud Engineer", "Security Engineer", "Client IT Lead"]
SWIMLANE_PHASES = ["Discovery", "Design", "Build", "Migration", "Validation", "Closure"]

SWIMLANE_TASKS = {
    "Discovery": {
        "Project Coordinator": ["Inventory of applications and data"],
        "Cloud Engineer": ["Cloud readiness assessment"],
        "Security Engineer": ["Security Deliverables: Identity audit, sensitive data mapping"],
        "Client IT Lead": ["Risk assessment & compliance gaps"],
    },
    "Design": {
        "Project Coordinator": ["Ensure timelines & compliance"],
        "Cloud Engineer": ["Architecture design"],
        "Security Engineer": ["Encryption & network planning"],
        "Client IT Lead": ["Validate design policies"],
    },
    "Build": {
        "Project Coordinator": ["Progress reporting"],
        "Cloud Engineer": ["Configure cloud services"],
        "Security Engineer": ["Firewall/ACL setup", "Key management"],
        "Client IT Lead": ["Review configs"],
    },
    "Migration": {
        "Project Coordinator": ["Migration status tracking"],
        "Cloud Engineer": ["Execute migration"],
        "Security Engineer": ["Monitor for suspicious activity"],
        "Client IT Lead": ["Approve migration checkpoints"],
    },
    "Validation": {
        "Project Coordinator": ["Test coordination"],
        "Cloud Engineer": ["Support testing"],
        "Security Engineer": ["Conduct penetration & compliance tests"],
        "Client IT Lead": ["Sign-off on UAT"],
    },
    "Closure": {
        "Project Coordinator": ["Document lessons learned"],
        "Cloud Engineer": ["Decommission test environments"],
        "Security Engineer": ["Deprovision access", "Finalize security logs"],
        "Client IT Lead": ["Confirm closure & compliance"],
    },
}

# ---------------------------
# Diagram implementations
# ---------------------------
# ---------------------------
# Flow Diagram
# ---------------------------
def render_flow_diagram():
    st.subheader("Flow Diagram (Lifecycle)")
    # layout params (units)
    box_w = 3.0
    box_h = 3.6   # increased height to avoid collisions
    spacing = 1.2
    max_wrap = 22

    # Adjust colors for dark vs light
    if theme.startswith("Dark"):
        box_line = "#5FA8FF"
        box_fill = "#1A365D"     # darker, higher contrast for white text
        text_color = "#FFFFFF"
        arrow_color = "#DDDDDD"
    else:
        box_line = "#1F77B4"
        box_fill = "#A9C6EA"
        text_color = "#0B2540"
        arrow_color = "#0B2540"

    fig = go.Figure()
    x0 = 0
    y0 = 0

    for idx, (phase_title, tasks) in enumerate(PHASES_FLOW):
        x1 = x0 + box_w
        y1 = y0 + box_h

        # Rectangle for phase
        fig.add_shape(
            type="rect",
            x0=x0, x1=x1, y0=y0, y1=y1,
            line=dict(color=box_line, width=1.8),
            fillcolor=box_fill,
        )

        # Phase title
        fig.add_annotation(
            x=(x0 + x1) / 2,
            y=y1 - 0.25,
            text=f"<b>{phase_title}</b>",
            showarrow=False,
            font=dict(size=14, color=text_color),
            xanchor="center",
            yanchor="top",
        )

        # Tasks wrapped and distributed inside box
        wrapped = []
        for t in tasks:
            wrapped.extend(wrap_lines(t, max_wrap))
        if wrapped:
            n = len(wrapped)
            usable = box_h - 0.8
            line_spacing = usable / max(n, 1)
            for i, line in enumerate(wrapped):
                y_line = y1 - 0.8 - (i + 0.5) * line_spacing
                fig.add_annotation(
                    x=(x0 + x1) / 2,
                    y=y_line,
                    text=line,
                    showarrow=False,
                    font=dict(size=12, color=text_color),
                    xanchor="center",
                    yanchor="middle",
                )

        # Arrow to next phase
        if idx < len(PHASES_FLOW) - 1:
            arrow_x = x1
            arrow_x_to = x1 + spacing
            fig.add_annotation(
                x=arrow_x_to - spacing / 2,
                y=y0 + box_h / 2,
                ax=arrow_x,
                ay=y0 + box_h / 2,
                xref="x",
                yref="y",
                axref="x",
                ayref="y",
                showarrow=True,
                arrowhead=3,
                arrowsize=1.3,
                arrowwidth=1.8,
                arrowcolor=arrow_color,
                standoff=4,
            )

        x0 = x1 + spacing

    fig.update_xaxes(visible=False, range=[-0.5, x0 - spacing + box_w + 0.5])
    fig.update_yaxes(visible=False, range=[-0.5, box_h + 0.5])
    fig.update_layout(
        height=460,  # slightly taller chart to fit boxes
        margin=dict(l=10, r=10, t=10, b=10),
        plot_bgcolor=PLOT_BG,
        paper_bgcolor=PLOT_BG,
    )
    st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# WBS Tree
# ---------------------------
def render_wbs_tree():
    st.subheader("Hierarchical WBS Tree")

    phase_spacing_x = 300
    root_y = 600
    level_gap = 140  # spacing between boxes
    box_w = 240
    box_h = 110  # taller boxes to fit multi-line tasks
    max_wrap = 22

    fig = go.Figure()
    root_x = phase_spacing_x * (len(WBS_PHASES) - 1) / 2

    # Theme colors with better contrast for dark mode
    if theme.startswith("Dark"):
        root_fill = "#234E70"
        node_fill = "#1A4A80"  # darker blue for contrast
        text_color = "#FFFFFF"
        line_color = "#CCCCCC"
    else:
        root_fill = PROFESSIONAL_PALETTE["wbs_root"]
        node_fill = PROFESSIONAL_PALETTE["wbs_node"]
        text_color = "#0b2540"
        line_color = "#0b2540"

    # Helper: draw a box with wrapped text
    def add_box(xc, yc, label, fill=node_fill, font_size=14, bold=False):
        fig.add_shape(
            type="rect",
            x0=xc - box_w / 2,
            x1=xc + box_w / 2,
            y0=yc - box_h / 2,
            y1=yc + box_h / 2,
            line=dict(color=line_color, width=1),
            fillcolor=fill,
        )
        wrapped = wrap_lines(label, max_wrap)
        usable = box_h - 16
        line_spacing = usable / max(len(wrapped), 1)
        for i, line in enumerate(wrapped):
            y_line = yc + box_h / 2 - (i + 0.5) * line_spacing
            fig.add_annotation(
                x=xc,
                y=y_line,
                text=f"<b>{line}</b>" if bold else line,
                showarrow=False,
                font=dict(size=font_size, color=text_color),
                xanchor="center",
                yanchor="middle",
            )

    # Draw root
    root_h = box_h  # <<< define root_h to fix NameError
    add_box(root_x, root_y, "Cloud Migration", fill=root_fill, font_size=16, bold=True)

    # Draw phases and tasks
    for i, (phase_name, tasks) in enumerate(WBS_PHASES):
        px = i * phase_spacing_x
        py = root_y - root_h / 2 - level_gap
        add_box(px, py, phase_name, font_size=15, bold=True)

        # connector root -> phase
        fig.add_shape(
            type="line",
            x0=root_x,
            y0=root_y - root_h / 2,
            x1=px,
            y1=py + box_h / 2,
            line=dict(color=line_color, width=1),
        )

        # draw tasks below phase
        prev_bottom = py - box_h / 2
        for j, task in enumerate(tasks):
            ty = prev_bottom - level_gap
            add_box(px, ty, task, font_size=14)
            # connector from previous box
            fig.add_shape(
                type="line",
                x0=px,
                y0=prev_bottom,
                x1=px,
                y1=ty + box_h / 2,
                line=dict(color=line_color, width=1),
            )
            prev_bottom = ty - box_h / 2

    # Layout
    fig.update_xaxes(visible=False, range=[-150, phase_spacing_x * (len(WBS_PHASES) - 1) + 150])
    fig.update_yaxes(visible=False, range=[-(len(WBS_PHASES) + 4) * level_gap, root_y + 150])
    fig.update_layout(
        height=800,
        margin=dict(l=10, r=10, t=10, b=10),
        plot_bgcolor=PLOT_BG,
        paper_bgcolor=PLOT_BG,
    )
    st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# Swim Lane
# ---------------------------
def render_swimlane():
    st.subheader("Swimlane Chart")

    roles = SWIMLANE_ROLES
    phases = SWIMLANE_PHASES
    tasks = SWIMLANE_TASKS

    # grid layout
    box_w = 1.9
    h_spacing = 0.28
    v_spacing = 0.5
    max_wrap = 20          # force wrapping at a reasonable width
    font_size = 12.5
    n_phases = len(phases)
    n_roles = len(roles)

    # colors (balanced)
    if theme.startswith("Dark"):
        lane_colors = {
            "Project Coordinator": "#1E3A5F",
            "Cloud Engineer": "#155E75",
            "Security Engineer": "#2A744E",
            "Client IT Lead": "#3E4C59",
        }
        text_color = "#FFFFFF"
        border_color = "#CCCCCC"
    else:
        lane_colors = {
            "Project Coordinator": "#A9C7ED",
            "Cloud Engineer": "#A8DAF2",
            "Security Engineer": "#B5E0C1",
            "Client IT Lead": "#D3D9E0",
        }
        text_color = "#0B2540"
        border_color = "#0B2540"

    # 1) compute wrapped lines per cell and find the maximum lines needed
    wrapped_map = {}   # (phase_idx, role_idx) -> list of lines
    max_lines = 1
    for i, phase in enumerate(phases):
        for j, role in enumerate(roles):
            cell_tasks = tasks.get(phase, {}).get(role, [])
            wrapped_lines = []
            for t in cell_tasks:
                wrapped_lines.extend(wrap_lines(t, max_wrap))
            if not wrapped_lines:
                wrapped_lines = [""]  # keep one empty line so boxes aren't collapsed
            wrapped_map[(i, j)] = wrapped_lines
            if len(wrapped_lines) > max_lines:
                max_lines = len(wrapped_lines)

    # 2) compute even box height that fits the busiest cell (top-aligned)
    line_height = 0.45   # vertical unit per text line (tweak if needed)
    top_pad = 0.28
    bottom_pad = 0.28
    safety_margin = 0.2
    box_h = top_pad + bottom_pad + max_lines * line_height + safety_margin

    fig = go.Figure()

    # 3) draw grid and place top-aligned wrapped text
    for i, phase in enumerate(phases):
        x0 = i * (box_w + h_spacing)
        x1 = x0 + box_w
        for j, role in enumerate(roles):
            y_top = -j * (box_h + v_spacing)
            y_bottom = y_top - box_h

            fig.add_shape(
                type="rect",
                x0=x0, x1=x1, y0=y_bottom, y1=y_top,
                line=dict(color=border_color, width=1.1),
                fillcolor=lane_colors.get(role, "#99CCFF"),
            )

            # top-aligned cursor
            wrapped_lines = wrapped_map[(i, j)]
            y_cursor = y_top - top_pad
            for line in wrapped_lines:
                fig.add_annotation(
                    x=(x0 + x1) / 2,
                    y=y_cursor,
                    text=line,
                    showarrow=False,
                    font=dict(size=font_size, color=text_color),
                    xanchor="center",
                    yanchor="top",
                )
                y_cursor -= line_height

    # phase titles
    for i, phase in enumerate(phases):
        x_center = i * (box_w + h_spacing) + box_w / 2
        fig.add_annotation(
            x=x_center,
            y=1.12,
            text=f"<b>{phase}</b>",
            showarrow=False,
            font=dict(size=13.5, color=text_color),
            xanchor="center",
            yanchor="bottom",
        )

    # role labels (left)
    for j, role in enumerate(roles):
        y_center = -j * (box_h + v_spacing) - box_h / 2
        fig.add_annotation(
            x=-0.55,
            y=y_center,
            text=f"<b>{role}</b>",
            showarrow=False,
            font=dict(size=13.5, color=text_color),
            xanchor="right",
            yanchor="middle",
        )

    # layout
    fig.update_xaxes(visible=False, range=[-1.3, n_phases * (box_w + h_spacing)])
    fig.update_yaxes(visible=False, range=[- n_roles * (box_h + v_spacing) - 1.0, 1.4])
    fig.update_layout(
        height=900,
        margin=dict(l=110, r=30, t=40, b=40),
        plot_bgcolor=PLOT_BG,
        paper_bgcolor=PLOT_BG,
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# Render the selected diagram
# ---------------------------
if diagram_type == "Flow Diagram (Lifecycle)":
    render_flow_diagram()
elif diagram_type == "Hierarchical WBS Tree":
    render_wbs_tree()
elif diagram_type == "Swimlane Chart":
    render_swimlane()

