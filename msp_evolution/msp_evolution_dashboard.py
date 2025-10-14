# ---------------------------------------------------------
# msp_evolution_dashboard.py
# MSP Evolution Dashboard — Streamlit + Plotly
# Author: Julia Wen (wendigilane@gmail.com)
# Date: 10-0810-2025
#
# Description:
#   Interactive dashboard illustrating MSP evolution across eras:
#     * Flow Diagram (Lifecycle)
#     * Hierarchical Service Tree
#     * Role Evolution Swimlane
#     * Azure and AWS Comparison
#     * IT Acronym Glossary with dynamic highlighting
# Usage:
#   1. Run: streamlit run msp_evolution_dashboard.py
# ---------------------------------------------------------
# msp_evolution_dashboard.py
# msp_evolution_dashboard.py
import streamlit as st
import plotly.graph_objects as go
import textwrap
from msp_cloud_acronyms import ACRONYMS  # import your full acronyms

# ---------------------------
# New Import for OAuth 2.0 Waterfall Example
# ---------------------------
from waterfall_oauth_demo import render_waterfall_oauth_demo
from waterfall_pm_demo import render_waterfall_pm_demo
from oauth2_gantt_demo import render_oauth2_gantt

from streamlit.components.v1 import html

# --- Acronym Tooltip Helpers ---
def explain_acronym(acronym, acronyms_dict):
    """Return acronym with tooltip if definition is found."""
    definition = acronyms_dict.get(acronym)
    if definition:
        return f"<span title='{definition}' style='text-decoration: underline dotted; cursor: help;'>{acronym}</span>"
    else:
        return acronym

def expand_acronyms_in_text(text, acronyms_dict):
    """Replace acronyms in a text string with tooltip HTML."""
    for acro, definition in acronyms_dict.items():
        if acro in text:
            tooltip_html = explain_acronym(acro, acronyms_dict)
            text = text.replace(acro, tooltip_html)
    return text

st.set_page_config(page_title="🤖 MSP Evolution Dashboard", layout="wide")



# ---------------------------
# Sidebar
# ---------------------------
with st.sidebar:
    st.title("🤖 MSP Evolution Dashboard")
    theme = st.selectbox("Theme", ["Dark", "Light"])
    diagram_type = st.selectbox(
        "Select Diagram",
        [
            "Flow Diagram (Lifecycle)",
            "Hierarchical Service Tree",
            "Role Evolution Swimlane",
            "Cloud Security Comparison",
            "Waterfall PM",   # 👈 new option
            "OAuth 2.0 Waterfall Example",   # 👈 new option
            "OAuth 2.0 Project Plan",  # NEW ENTRY
            "IT Acronym Glossary"
        ],
    )
    all_acronyms = ["None"] + sorted(ACRONYMS.keys())
    acronym = st.selectbox("Highlight Acronym", all_acronyms)
# Automatically switch to OAuth 2.0 diagram if relevant acronym is selected
    oauth_related_terms = {"OAUTH", "OAUTH2", "OAUTH2.0", "OIDC", "OPENID CONNECT"}

    if acronym.upper() in oauth_related_terms:
        st.info("💡 This acronym relates to OAuth 2.0 — switching to the Waterfall Example diagram.")
        diagram_type = "OAuth 2.0 Waterfall Example"


# ---------------------------
# Theme Colors
# ---------------------------
dark = theme == "Dark"
BG = "#0f1720" if dark else "#FFFFFF"
TEXT = "#FFFFFF" if dark else "#0B2540"
LINE = "#E2E8F0" if dark else "#1E293B"

ERA_COLORS = {
    "Legacy MSP": "#93C5FD",
    "Cloud MSP": "#3B82F6",
    "AI-Driven MSP": "#1E3A8A"
}

ERA_COLORS_DARK = {
    "Legacy MSP": "#4A79E7",
    "Cloud MSP": "#1F44A9",
    "AI-Driven MSP": "#082569"
}

# ---------------------------
# Helper Functions
# ---------------------------
def wrap_lines(text, width):
    out = []
    for para in str(text).splitlines():
        if para.strip() == "":
            out.append("")
        else:
            out.extend(textwrap.wrap(para, width=width) or [""])
    return out

def highlight_text(text):
    if acronym != "None" and acronym in text:
        return text.replace(acronym, f"<b style='color:#FACC15'>{acronym}</b>")
    return text


# ---------------------------
# Flow Diagram
# ---------------------------
def render_flow_diagram():
    st.subheader("Flow Diagram — MSP Evolution")

    phases = [
        ("Legacy MSP", [
            "On-prem servers & infrastructure",
            "Manual backups & recovery",
            "Patch & incident management",
            "Network monitoring (basic, reactive)",
            "Endpoint management",
            "Helpdesk & ticketing (manual)",
            "Limited automation",
            "Hardware lifecycle management",
            "Reactive security monitoring"
        ]),
        ("Cloud MSP", [
            "Cloud migration & hybrid setups",
            "Infrastructure as Code (IaC)",
            "CI/CD pipelines for automation",
            "FinOps for cloud cost optimization",
            "IAM & compliance management",
            "Cloud-native monitoring & logging (proactive)",
            "Security automation (SecOps)",
            "Data backup to cloud",
            "Virtualization & container management",
            "Automated incident detection vs manual"
        ]),
        ("AI-Driven MSP", [
            "AIOps & predictive analytics",
            "Automated remediation",
            "AI copilots for IT tasks",
            "Self-healing infrastructure",
            "Proactive threat detection",
            "ML-driven resource optimization",
            "Intelligent ticket triage",
            "Automated compliance reporting",
            "Advanced cloud orchestration",
            "Autonomous monitoring & anomaly detection"
        ])
    ]

    n = len(phases)
    fig = go.Figure()
    w = 0.28
    h = 0.78
    y0_base = 0.12

    for i, (title, tasks) in enumerate(phases):
        x0 = 0.05 + i * (w + 0.05)
        x1 = x0 + w

        # Phase title above the box
        fig.add_annotation(
            x=(x0 + x1) / 2,
            y=y0_base + h + 0.02,
            text=f"<b>{title}</b>",
            showarrow=False,
            font=dict(size=18, color=TEXT),
            xanchor="center",
            yanchor="bottom"
        )

        # Draw box
        fig.add_shape(
            type="rect",
            x0=x0, x1=x1,
            y0=y0_base, y1=y0_base + h,
            line=dict(color=LINE, width=2),
            fillcolor=ERA_COLORS_DARK[title],
        )

        # Wrapped text inside box
        wrapped = []
        for t in tasks:
            wrapped.extend(wrap_lines(highlight_text(t), 26))

        max_lines = len(wrapped)
        spacing = h / (max_lines + 1)
        for j, line in enumerate(wrapped):
            fig.add_annotation(
                x=(x0 + x1) / 2,
                y=y0_base + h - (j + 1) * spacing,
                text=line,
                showarrow=False,
                font=dict(size=13, color="#FFFFFF"),
            )

        # Arrow to next box
        if i < n - 1:
            fig.add_annotation(
                x=x1 + 0.015, y=y0_base + h / 2,
                ax=x1 - 0.005, ay=y0_base + h / 2,
                showarrow=True, arrowhead=3, arrowwidth=2, arrowcolor=TEXT,
            )

    fig.update_xaxes(visible=False, range=[0, 1])
    fig.update_yaxes(visible=False, range=[0, 1])
    fig.update_layout(
        height=600,
        plot_bgcolor=BG,
        paper_bgcolor=BG,
        margin=dict(l=40, r=40, t=40, b=40)
    )
    st.plotly_chart(fig, use_container_width=True)


# ---------------------------
# Hierarchical Service Tree
# ---------------------------
def render_wbs_tree():
    st.subheader("Hierarchical Service Tree — MSP Capabilities")
    services = {
        "Legacy MSP": [
            "Monitoring & patching",
            "Backup & DR",
            "Endpoint security",
            "Manual ticketing",
            "Reactive monitoring"
        ],
        "Cloud MSP": [
            "Cloud migration & architecture",
            "IaC & CI/CD",
            "IAM & compliance",
            "Cloud dashboards",
            "Automated alerts"
        ],
        "AI-Driven MSP": [
            "AIOps & automation",
            "Predictive analytics",
            "AI copilots",
            "Self-healing infrastructure",
            "Proactive monitoring"
        ],
    }

    fig = go.Figure()
    x_positions = [0.2, 0.5, 0.8]
    root_y = 0.95

    # Root node
    fig.add_annotation(
        x=0.5, y=root_y, text="<b>Managed Service Provider</b>",
        showarrow=False, font=dict(size=20, color=TEXT),
    )
    fig.add_shape(
        type="rect", x0=0.4, x1=0.6, y0=root_y - 0.05, y1=root_y + 0.02,
        line=dict(color=LINE, width=2), fillcolor="#134E4A" if dark else "#A7F3D0",
    )

    for i, (era, subs) in enumerate(services.items()):
        x = x_positions[i]
        y = 0.75
        fig.add_shape(
            type="rect", x0=x - 0.09, x1=x + 0.09, y0=y - 0.04, y1=y + 0.04,
            line=dict(color=LINE, width=1.5), fillcolor=ERA_COLORS_DARK[era],
        )
        fig.add_annotation(
            x=x, y=y, text=f"<b>{era}</b>", showarrow=False,
            font=dict(size=16, color="#FFFFFF"),
        )
        fig.add_shape(type="line", x0=0.5, y0=root_y - 0.05, x1=x, y1=y + 0.04, line=dict(color=LINE, width=1))
        for j, s in enumerate(subs):
            sy = 0.55 - j * 0.1
            fig.add_shape(
                type="rect", x0=x - 0.1, x1=x + 0.1, y0=sy - 0.035, y1=sy + 0.035,
                line=dict(color=LINE, width=1), fillcolor=ERA_COLORS_DARK[era],
            )
            fig.add_annotation(
                x=x, y=sy, text=highlight_text(s), showarrow=False,
                font=dict(size=14, color="#FFFFFF"),
            )
            fig.add_shape(type="line", x0=x, y0=y - 0.04, x1=x, y1=sy + 0.035, line=dict(color=LINE, width=1))

    fig.update_xaxes(visible=False, range=[0, 1])
    fig.update_yaxes(visible=False, range=[0, 1])
    fig.update_layout(height=750, plot_bgcolor=BG, paper_bgcolor=BG)
    st.plotly_chart(fig, use_container_width=True)


# ---------------------------
# Role Evolution Swimlane
# ---------------------------
def render_swimlane():
    st.subheader("Role Evolution Swimlane — MSP Roles Across Eras")
    roles = ["Ops Engineer", "Cloud Architect", "Security Engineer", "Client IT Lead"]
    phases = ["Legacy MSP", "Cloud MSP", "AI-Driven MSP"]
    tasks = {
        "Legacy MSP": {
            "Ops Engineer": [
                "Server monitoring (manual)",
                "Patch cycles & updates",
                "Backup & restore on-prem",
                "Incident triage & ticketing",
                "Basic network monitoring"
            ],
            "Cloud Architect": [
                "Minimal involvement",
                "Support on-prem deployment",
                "Assist with basic IT upgrades"
            ],
            "Security Engineer": [
                "Firewall & antivirus configuration",
                "Manual compliance checks",
                "User access review"
            ],
            "Client IT Lead": [
                "Request IT support",
                "Communicate system issues to MSP"
            ]
        },
        "Cloud MSP": {
            "Ops Engineer": [
                "Automated monitoring dashboards",
                "Cloud VM & storage management",
                "Patch automation via CI/CD",
                "Cloud backup & disaster recovery",
                "Proactive incident alerts"
            ],
            "Cloud Architect": [
                "Design multi-cloud architecture",
                "CI/CD pipeline setup",
                "IaC templates for deployments",
                "Cost optimization & FinOps",
                "Cloud migration support"
            ],
            "Security Engineer": [
                "IAM & role management",
                "Conditional Access policies",
                "Cloud-native SIEM monitoring",
                "Security automation (SecOps)",
                "Threat detection & logging"
            ],
            "Client IT Lead": [
                "Review SLA & cloud dashboards",
                "Coordinate cloud access requests",
                "Approve automation policies"
            ]
        },
        "AI-Driven MSP": {
            "Ops Engineer": [
                "AIOps predictive alerts",
                "Automated remediation",
                "Self-healing infrastructure",
                "ML-driven resource optimization",
                "Autonomous monitoring & anomaly detection"
            ],
            "Cloud Architect": [
                "MLOps & AI orchestration",
                "Advanced cloud optimization",
                "AI-driven provisioning & scaling",
                "Integration with AI copilots"
            ],
            "Security Engineer": [
                "Proactive threat hunting",
                "AI-based anomaly detection",
                "Automated compliance reporting",
                "Self-remediating security controls"
            ],
            "Client IT Lead": [
                "Receive predictive insights",
                "Approve AI-driven decisions",
                "Monitor KPIs via AI dashboards"
            ]
        },
    }

    fig = go.Figure()
    row_h = 1 / len(roles)
    label_width = 0.15
    left_margin = 0.01
    right_margin = 0.01
    remaining_width = 1 - left_margin - label_width - right_margin
    box_width = remaining_width / len(phases) * 0.95
    box_spacing = (remaining_width - box_width * len(phases)) / (len(phases) - 1)

    for i, role in enumerate(roles):
        y0 = 1 - (i + 1) * row_h
        fig.add_annotation(
            x=left_margin,
            y=y0 + row_h / 2,
            text=f"<b>{role}</b>",
            showarrow=False,
            font=dict(size=16, color=TEXT),
            xanchor="left",
            align="left"
        )
        for j, phase in enumerate(phases):
            x0 = left_margin + label_width + j * (box_width + box_spacing)
            x1 = x0 + box_width
            fig.add_shape(
                type="rect",
                x0=x0, x1=x1,
                y0=y0, y1=y0 + row_h * 0.85,
                line=dict(color=LINE, width=1),
                fillcolor=ERA_COLORS_DARK[phase],
            )
            txt = "<br>".join([highlight_text(t) for t in tasks[phase].get(role, [])])
            fig.add_annotation(
                x=(x0 + x1) / 2,
                y=y0 + row_h / 2,
                text=txt,
                showarrow=False,
                font=dict(size=14, color="#FFFFFF"),
            )

    # Headers
    for j, phase in enumerate(phases):
        x0 = left_margin + label_width + j * (box_width + box_spacing) + box_width / 2
        fig.add_annotation(
            x=x0,
            y=1.03,
            text=f"<b>{phase}</b>",
            showarrow=False,
            font=dict(size=16, color=TEXT),
        )

    fig.update_xaxes(visible=False, range=[0, 1])
    fig.update_yaxes(visible=False, range=[0, 1.1])
    fig.update_layout(
        height=650,
        plot_bgcolor=BG,
        paper_bgcolor=BG,
        margin=dict(l=10, r=10, t=60, b=40),
    )
    st.plotly_chart(fig, use_container_width=True)


# ---------------------------
# Cloud Security Comparison
# ---------------------------
def render_cloud_comparison():
    st.subheader("Cloud Security Comparison — Azure vs AWS")

    comparison_data = [
    {"Category": "Identity & Access Management",
     "Azure": "Entra ID (Azure AD), Conditional Access, RBAC, MFA, SSO, Privileged Identity Management (PIM)",
     "AWS": "IAM, AWS Identity Center (SSO), IAM Roles, Policy-Based Access Control, MFA"},

    {"Category": "Authentication & Authorization",
     "Azure": "OAuth, OIDC, SAML, Conditional Access, Azure AD B2C for application authentication",
     "AWS": "OAuth, OIDC, SAML, IAM Policies for application authentication, Cognito for app auth"},

    {"Category": "Compute / Virtual Machines",
     "Azure": "Virtual Machines (VMs), VM Scale Sets (VMSS), Managed Disks, integration with Defender for Cloud, EDR agents",
     "AWS": "EC2, Auto Scaling Groups, Elastic Block Store (EBS), Security Hub integration, GuardDuty agents for EDR"},

    {"Category": "Containerization & Orchestration",
     "Azure": "AKS with Defender for Containers, ACI, ACR with image scanning, automated security policies",
     "AWS": "EKS with GuardDuty Container Insights, ECS, ECR with image scanning, Fargate security profiles, automated security alerts"},

    {"Category": "Storage Security",
     "Azure": "Blob Storage with encryption, Storage Account firewalls, Data Lake, Customer-managed keys in Key Vault, soft delete, immutable blobs",
     "AWS": "S3 with bucket policies, Glacier, KMS-managed keys, versioning & MFA delete, SSE-C/SSE-KMS/SSE-S3"},

    {"Category": "Network Isolation & Virtual Networking",
     "Azure": "VNet, Subnets, NSGs, Azure Firewall, Private Endpoints, Service Endpoints, ExpressRoute, VNet Peering",
     "AWS": "VPC, Subnets, Security Groups, NACLs, PrivateLink, Transit Gateway, Direct Connect, VPC Peering"},

    {"Category": "Endpoint & Threat Detection",
     "Azure": "Microsoft Defender for Endpoint (EDR), Sentinel (SIEM), XDR across endpoints, identities, apps, and cloud, MDR via Microsoft 365 Defender",
     "AWS": "Inspector (vulnerability scanning), GuardDuty (EDR for cloud workloads), Security Hub (aggregated alerts), XDR across workloads and accounts, MDR via AWS Managed Detection and Response"},

    {"Category": "AI-Driven Security",
     "Azure": "AI/ML analytics in Defender for Cloud and Sentinel, predictive threat detection, automated remediation, anomaly detection in user and entity behavior",
     "AWS": "AI/ML in GuardDuty and Security Hub, anomaly detection for workloads and accounts, automated remediation using Lambda and Security Hub insights"},

    {"Category": "Monitoring & Logging",
     "Azure": "Log Analytics, Activity Logs, Azure Monitor, Security Center alerts, integration with SIEM",
     "AWS": "CloudWatch, CloudTrail, Macie, Security Hub alerts, GuardDuty findings, integration with SIEM"},

    {"Category": "Encryption & Key Management",
     "Azure": "Key Vault, Disk Encryption, Customer-managed keys (BYOK), Transparent Data Encryption for SQL, Azure Storage Service Encryption",
     "AWS": "KMS, CloudHSM, SSE-S3/SSE-KMS/SSE-C, EBS encryption, RDS encryption, S3 encryption at rest"},

    {"Category": "Compliance & Frameworks",
     "Azure": "CMMC 2.0 (Cybersecurity Maturity Model Certification), ISO 27001, FedRAMP, HIPAA, SOC 2",
     "AWS": "CMMC 2.0 (Cybersecurity Maturity Model Certification), ISO 27001, FedRAMP, HIPAA, SOC 2"}
    ]


    selected = acronym
    if selected != "None":
        for row in comparison_data:
            for col in ["Azure", "AWS"]:
                if selected in row[col]:
                    row[col] = row[col].replace(selected, f"<b style='color:#FACC15'>{selected}</b>")

    html = "<table style='width:100%; border-collapse: collapse;'>"
    html += "<tr><th style='border:1px solid #999; padding:5px'>Category</th>"
    html += "<th style='border:1px solid #999; padding:5px'>Azure</th>"
    html += "<th style='border:1px solid #999; padding:5px'>AWS</th></tr>"

    for row in comparison_data:
        html += f"<tr><td style='border:1px solid #999; padding:5px; vertical-align:top'><b>{row['Category']}</b></td>"
        html += f"<td style='border:1px solid #999; padding:5px; vertical-align:top'>{row['Azure']}</td>"
        html += f"<td style='border:1px solid #999; padding:5px; vertical-align:top'>{row['AWS']}</td></tr>"

    html += "</table>"

    st.markdown(html, unsafe_allow_html=True)


def render_network_visualization():
    st.subheader("Cloud Network Architecture — Azure VNet vs AWS VPC")

    # --- Define node coordinates (Azure left, AWS right) ---
    nodes = {
        # Azure side
        "Azure Cloud": (-2, 3),
        "Azure VNet": (-2, 2),
        "Azure Subnet A": (-3, 1),
        "Azure Subnet B": (-1, 1),
        "Azure NSG": (-3, 0),
        "Azure Firewall": (-1, 0),
        "Azure Private Endpoint": (-2, -1),
        "Azure ExpressRoute": (-2, -2),

        # AWS side
        "AWS Cloud": (2, 3),
        "AWS VPC": (2, 2),
        "AWS Subnet A": (1, 1),
        "AWS Subnet B": (3, 1),
        "AWS Security Group": (1, 0),
        "AWS NACL": (3, 0),
        "AWS PrivateLink": (2, -1),
        "AWS Internet Gateway": (2, -2),
    }

    # --- Define edges (connections) ---
    edges = [
        # Azure connections
        ("Azure Cloud", "Azure VNet"),
        ("Azure VNet", "Azure Subnet A"),
        ("Azure VNet", "Azure Subnet B"),
        ("Azure Subnet A", "Azure NSG"),
        ("Azure Subnet B", "Azure Firewall"),
        ("Azure NSG", "Azure Private Endpoint"),
        ("Azure Firewall", "Azure Private Endpoint"),
        ("Azure Private Endpoint", "Azure ExpressRoute"),

        # AWS connections
        ("AWS Cloud", "AWS VPC"),
        ("AWS VPC", "AWS Subnet A"),
        ("AWS VPC", "AWS Subnet B"),
        ("AWS Subnet A", "AWS Security Group"),
        ("AWS Subnet B", "AWS NACL"),
        ("AWS Security Group", "AWS PrivateLink"),
        ("AWS NACL", "AWS PrivateLink"),
        ("AWS PrivateLink", "AWS Internet Gateway"),
    ]

    # --- Plot edges ---
    edge_x, edge_y = [], []
    for (src, dst) in edges:
        x0, y0 = nodes[src]
        x1, y1 = nodes[dst]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        line=dict(width=1, color='gray'),
        hoverinfo='none',
        mode='lines'
    )

    # --- Plot nodes ---
    node_x = [coord[0] for coord in nodes.values()]
    node_y = [coord[1] for coord in nodes.values()]
    node_labels = list(nodes.keys())

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode='markers+text',
        text=node_labels,
        textposition='bottom center',
        marker=dict(
            showscale=False,
            color=['#0078D4'] * 8 + ['#FF9900'] * 8,  # Azure blue, AWS orange
            size=20,
            line_width=2
        )
    )

    # --- Build the figure ---
    fig = go.Figure(data=[edge_trace, node_trace])
    fig.update_layout(
        showlegend=False,
        title="Azure VNet vs AWS VPC — Network Isolation and Connectivity",
        title_x=0.5,
        margin=dict(l=20, r=20, t=60, b=20),
        plot_bgcolor='white',
        xaxis=dict(showgrid=False, zeroline=False, visible=False),
        yaxis=dict(showgrid=False, zeroline=False, visible=False),
        height=600
    )

    # --- Render in Streamlit ---
    st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# Acronym Glossary
# ---------------------------
def render_glossary():
    st.subheader("IT Acronyms Glossary")
    if acronym == "None":
        st.write("Select an acronym from the sidebar to see its definition.")
    else:
        st.markdown(f"**{acronym}**: {ACRONYMS.get(acronym, 'Definition not found')}")

# ---------------------------
# Layout
# ---------------------------

# For full-width diagrams like OAuth Gantt, render above the columns
if diagram_type == "OAuth 2.0 Project Plan":
    render_oauth2_gantt()  # full-width chart

# Columns for other diagrams / Acronym Info
col1, col2 = st.columns([3, 1])

with col1:
    if diagram_type == "Flow Diagram (Lifecycle)":
        render_flow_diagram()
    elif diagram_type == "Role Evolution Swimlane":
        render_swimlane()
    elif diagram_type == "Hierarchical Service Tree":
        render_wbs_tree()
    elif diagram_type == "Cloud Security Comparison":
        render_cloud_comparison()
        render_network_visualization()
    elif diagram_type == "Waterfall PM":
        render_waterfall_pm_demo()
    elif diagram_type == "OAuth 2.0 Waterfall Example":
        render_waterfall_oauth_demo()
    elif diagram_type == "IT Acronym Glossary":
        render_glossary()
    # OAuth 2.0 already rendered above, so no need here

with col2:
    st.markdown("### 📘 Acronym Info")
    # Show selected acronym definition regardless of diagram
    if acronym == "None":
        st.info("Select an acronym from the sidebar to see its definition.")
    else:
        meaning = ACRONYMS.get(acronym, "Definition not found")
        st.markdown(
            f"""
            <div style='background-color:{'#1E293B' if dark else '#F8FAFC'};
                        border:1px solid {LINE};
                        border-radius:0.6rem;
                        padding:1rem;
                        margin-top:0.5rem;
                        font-size:1.1rem;
                        color:{TEXT};'>
                <b style='color:#FACC15'>{acronym}</b>: {meaning}
            </div>
            """,
            unsafe_allow_html=True,
        )
