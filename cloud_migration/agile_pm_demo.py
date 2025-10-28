# ---------------------------------------------------------
# # agile_pm_demo.py
# Author: Julia Wen (wendigilane@gmail.com)
# Date: 10-27-2025
#
# Description:
#   Top: project-level Kanban with one column per sprint (Sprint 1, Sprint 2, Sprint 3).
#   Bottom: sprint selector + detailed sprint board, metrics and charts.$
# ---------------------------------------------------------
import streamlit as st
import plotly.graph_objects as go
import random

def render_agile_board():
    """
    Agile PM demo module — call agile_pm_demo.render() from the main dashboard.
    """

    st.title("🟢 Agile Project Management — Sprint View")
    st.caption("Project-level Kanban (columns per sprint). Select a sprint below to drill into details.")

    # ---------------------------
    # Role color palette and helper
    # ---------------------------
    ROLE_COLORS = {
        "Project Coordinator": "#2B5D8A",
        "Cloud Engineer": "#16789B",
        "Security Engineer": "#1F8A70",
        "Client IT Lead": "#4C6A88",
    }

    def render_card(task, role, points, status):

        # Safely get theme, default to light
        try:
            base_theme = st.get_option("theme.base") or "light"
        except Exception:
            base_theme = "light"
        dark_mode = base_theme.lower() == "dark"

        ROLE_COLORS = {
            "Project Coordinator": "#2B5D8A",
            "Cloud Engineer": "#16789B",
            "Security Engineer": "#1F8A70",
            "Client IT Lead": "#4C6A88",
        }
        color = ROLE_COLORS.get(role, "#888888")

        # Card background & text
        card_bg = "#FFFFFF" if not dark_mode else "#111827"
        card_text = "#111827" if not dark_mode else "#F9FAFB"
        sub_text = "#374151" if not dark_mode else "#D1D5DB"

        # Status badge: clear contrast between light/dark
        if dark_mode:
            status_colors = {
                "To Do": ("#1E3A8A", "#FFFFFF"),         # dark blue bg, white text
                "In Progress": ("#78350F", "#FFFFFF"),   # dark amber bg, white text
                "Done": ("#14532D", "#FFFFFF"),          # dark green bg, white text
            }
        else:
            status_colors = {
                "To Do": ("#BFDBFE", "#1E3A8A"),         # light blue bg, dark text
                "In Progress": ("#FEF3C7", "#78350F"),   # light amber bg, dark text
                "Done": ("#DCFCE7", "#166534"),          # light green bg, dark text
            }

        badge_bg, badge_fg = status_colors.get(status, ("#E5E7EB", "#111827"))

        html = f"""
        <div style='
            border-radius:10px;
            padding:10px;
            margin-bottom:10px;
            background-color:{card_bg};
            border-left:5px solid {color};
            box-shadow:0 1px 3px rgba(0,0,0,0.1);
        '>
            <div style='display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;'>
                <div style='font-weight:600; font-size:14px; color:{card_text};'>{task}</div>
                <div style='
                    background-color:{badge_bg};
                    color:{badge_fg};
                    font-size:11px;
                    padding:3px 8px;
                    border-radius:8px;
                    font-weight:600;
                '>{status}</div>
            </div>
            <div style='font-size:12px; color:{sub_text};'>
                <span style='font-weight:600; color:{color};'>{role}</span>
                &nbsp;•&nbsp;
                <span>Points: {points}</span>
            </div>
        </div>
        """
        return html


    # ---------------------------
    # Master sprint data (sprint-centric, consistent progression)
    # ---------------------------
    # Sprint 1 = completed sprint (mostly Done)
    # Sprint 2 = active sprint (In Progress)
    # Sprint 3 = upcoming sprint (To Do)
    SPRINTS = {
        "Sprint 1": [
            # (task, role, points, status)
            ("CI/CD pipeline finalized", "Cloud Engineer", 3, "Done"),
            ("Initial infra hardening", "Security Engineer", 5, "Done"),
            ("Documentation & handoff", "Project Coordinator", 2, "Done"),
        ],
        "Sprint 2": [
            ("Implement logging & monitoring", "Cloud Engineer", 8, "In Progress"),
            ("Authentication module", "Cloud Engineer", 5, "In Progress"),
            ("Security requirements audit", "Security Engineer", 3, "To Do"),
            ("User acceptance preparation", "Project Coordinator", 2, "To Do"),
        ],
        "Sprint 3": [
            ("Data migration plan", "Cloud Engineer", 5, "To Do"),
            ("Load testing", "Project Coordinator", 3, "To Do"),
            ("Retention & archival policy", "Security Engineer", 4, "To Do"),
        ],
    }

    # Keep a deterministic sprint ordering
    sprint_order = ["Sprint 1", "Sprint 2", "Sprint 3"]

    # ---------------------------
    # Project-level Kanban: one column per sprint
    # ---------------------------
    st.subheader("📋 Project Overview — Sprints as Columns")
    st.caption("Each column is a sprint. Cards show status (To Do, In Progress, Done).")

    sprint_cols = st.columns(len(sprint_order))
    for col, sprint_name in zip(sprint_cols, sprint_order):
        with col:
            st.markdown(f"### {sprint_name}")
            tasks = SPRINTS.get(sprint_name, [])
            if not tasks:
                st.markdown("_(no tasks)_")
            else:
                # Group by status to show order: In Progress, To Do, Done (so active work is visible near top)
                status_order = ["In Progress", "To Do", "Done"]
                grouped = {s: [] for s in status_order}
                # also include any unexpected statuses
                for t in tasks:
                    s = t[3]
                    if s not in grouped:
                        grouped.setdefault(s, [])
                    grouped[s].append(t)
                for status in status_order + [s for s in grouped.keys() if s not in status_order]:
                    for task, role, points, _ in grouped.get(status, []):
                        st.markdown(render_card(task, role, points, status), unsafe_allow_html=True)

    st.markdown("---")

    # ---------------------------
    # Sprint selector: drill into detailed sprint board
    # ---------------------------
    st.subheader("🏃 Sprint Details (drilldown)")
    selected_sprint = st.selectbox("Select a sprint to inspect:", sprint_order, index=1)  # default to Sprint 2 (active)

    sprint_tasks = SPRINTS[selected_sprint]

    # Arrange detailed board as To Do / In Progress / Done columns for the selected sprint
    # Build status buckets
    detail_buckets = {"To Do": [], "In Progress": [], "Done": []}
    for task, role, points, status in sprint_tasks:
        detail_buckets.setdefault(status, []).append((task, role, points))

    st.markdown(f"### 📋 {selected_sprint} — Detailed Board")
    detail_cols = st.columns(3)
    for col, status in zip(detail_cols, ["To Do", "In Progress", "Done"]):
        with col:
            st.markdown(f"#### {status} ({len(detail_buckets.get(status, []))})")
            items = detail_buckets.get(status, [])
            if not items:
                st.markdown("_(no items)_")
            for task, role, points in items:
                st.markdown(render_card(task, role, points, status), unsafe_allow_html=True)

    # ---------------------------
    # Selected sprint metrics
    # ---------------------------
    st.markdown("---")
    st.subheader(f"📈 {selected_sprint} Metrics")

    total_points = sum(points for _, _, points, _ in sprint_tasks)
    done_points = sum(points for _, _, points, status in sprint_tasks if status == "Done")
    completion_rate = round(done_points / total_points * 100, 1) if total_points > 0 else 0.0
    in_progress_count = len([1 for _, _, _, status in sprint_tasks if status == "In Progress"])

    mcol1, mcol2, mcol3 = st.columns(3)
    with mcol1:
        st.metric("Total Story Points", total_points)
    with mcol2:
        st.metric("Completion Rate", f"{completion_rate}%")
    with mcol3:
        st.metric("Tasks In Progress", in_progress_count)

    # ---------------------------
    # Simulated Velocity & Burndown (for the selected sprint)
    # ---------------------------
    st.subheader("📊 Velocity (historical)")
    sprint_names_hist = [f"Sprint {i}" for i in range(1, 6)]
    velocity = [random.randint(15, 40) for _ in sprint_names_hist]
    fig_vel = go.Figure()
    fig_vel.add_trace(go.Bar(x=sprint_names_hist, y=velocity, text=[f"{v} pts" for v in velocity], textposition="outside"))
    fig_vel.update_layout(height=300, margin=dict(l=30, r=30, t=30, b=30))
    st.plotly_chart(fig_vel, use_container_width=True)

    st.subheader("🔥 Burndown (simulated)")
    days = [f"Day {i}" for i in range(1, 11)]
    if total_points > 0:
        step = total_points / (len(days) - 1)
        ideal = [round(max(total_points - i * step, 0)) for i in range(len(days))]
    else:
        ideal = [0] * len(days)
    actual = [max(0, v + random.randint(-2, 2)) for v in ideal]
    fig_burn = go.Figure()
    fig_burn.add_trace(go.Scatter(x=days, y=ideal, mode="lines+markers", name="Ideal", line=dict(dash="dot")))
    fig_burn.add_trace(go.Scatter(x=days, y=actual, mode="lines+markers", name="Actual", line=dict(width=3)))
    fig_burn.update_layout(height=340, margin=dict(l=30, r=30, t=30, b=30))
    st.plotly_chart(fig_burn, use_container_width=True)

    # ---------------------------
    # Role Legend
    # ---------------------------
    st.markdown("---")
    st.subheader("🎨 Role Color Legend")
    legend_cols = st.columns(len(ROLE_COLORS))
    for col, (role, color) in zip(legend_cols, ROLE_COLORS.items()):
        with col:
            st.markdown(
                f"<div style='background:{color}; padding:8px; border-radius:6px; text-align:center; color:#fff; font-weight:600;'>{role}</div>",
                unsafe_allow_html=True,
            )

    st.caption("Top: project-level sprint columns. Drill down to any sprint using the selector above.")

