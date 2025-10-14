# ---------------------------------------------------------
# cmmc_webdev.py
# CMMC 2.0 Web Development + PM Tasks + Tool Search + Cost & Level Tabs
# Author: Julia Wen
# Date: 2025-10-10
#
# Description:
#   Streamlit dashboard for:
#   - CMMC 2.0 Acronyms
#   - Project Management (PM) Web Compliance Tasks
#   - Security Tools (Free, Paid, GitLab) with cost and CMMC level
# ---------------------------------------------------------

import streamlit as st
import pandas as pd
from cmmc_free_tools import get_free_tools
from cmmc_paid_tools import get_paid_tools
from cmmc_gitlab_tools import get_gitlab_tools

# ---------------------------------------------------------
# ACRONYMS TABLE
# ---------------------------------------------------------
ACRONYM_DATA = [
    ("CMMC", "Cybersecurity Maturity Model Certification – DoD standard ensuring contractors protect CUI.", "CMMC Framework"),
    ("CUI", "Controlled Unclassified Information – sensitive data requiring safeguarding but not classified.", "CMMC Framework"),
    ("FCI", "Federal Contract Information – data generated for government contracts not intended for public release.", "CMMC Framework"),
    ("NIST SP 800-171", "Defines security controls required to protect CUI.", "Compliance"),
    ("NIST SP 800-218", "Secure Software Development Framework (SSDF).", "Compliance"),
    ("OWASP", "Open Web Application Security Project – provides top-10 web security best practices.", "Web Security"),
    ("MFA", "Multi-Factor Authentication – verifies identity using two or more factors.", "Access Control"),
    ("RBAC", "Role-Based Access Control – restricts system access based on user roles.", "Access Control"),
    ("TLS", "Transport Layer Security – encrypts data in transit.", "Encryption"),
    ("HTTPS", "HTTP Secure – HTTP protocol layered over TLS.", "Encryption"),
    ("SIEM", "Security Information and Event Management – monitors and analyzes security events.", "Monitoring"),
    ("IAM", "Identity and Access Management – ensures appropriate access for users and systems.", "Access Control"),
    ("IR", "Incident Response – detects, investigates, and mitigates security events.", "Incident Response"),
    ("AC", "Access Control – governs permissions and access policies.", "CMMC Domain"),
    ("CM", "Configuration Management – ensures systems and apps are securely configured.", "CMMC Domain"),
    ("IA", "Identification and Authentication – verifies identity of users before access.", "CMMC Domain"),
    ("SC", "System and Communications Protection – network security, encryption, and data isolation.", "CMMC Domain"),
    ("SI", "System and Information Integrity – focuses on vulnerability detection and response.", "CMMC Domain"),
    ("AU", "Audit and Accountability – requires secure audit log generation and review.", "CMMC Domain"),
]
df_acronyms = pd.DataFrame(ACRONYM_DATA, columns=["Acronym", "Definition", "Domain"])

# ---------------------------------------------------------
# PM TASKS TABLE
# ---------------------------------------------------------
PM_TASKS = [
    ("Inventory and Documentation",
     "Maintain inventory of website assets (servers, domains, SSL, plugins, third-party services).",
     "CMMC Level 1 — Asset Management."),
    ("Vulnerability Scanning",
     "Use tools (e.g., Nessus, OpenVAS, Qualys) to scan for vulnerabilities and report findings.",
     "CMMC Level 2 — SI.2.214."),
    ("Patch Management",
     "Check for updates to CMS, plugins, and libraries; report outdated components.",
     "CMMC Level 1 — SI.1.210."),
    ("Access Control Review",
     "Review admin and backend user accounts; flag unnecessary or outdated access.",
     "CMMC Level 1 — AC.1.001."),
    ("Backup Verification",
     "Verify website backups are performed regularly and restoration is tested.",
     "CMMC Level 1 — RE.1.131."),
    ("Password Policy Enforcement",
     "Ensure strong passwords and MFA are enforced.",
     "CMMC Level 1 — AC.1.002."),
    ("Third-Party Vendor Tracking",
     "Document third-party services (analytics, payments) and verify compliance.",
     "CMMC Level 2 — SR.2.213."),
    ("Security Awareness Training",
     "Assist in creating/updating basic security awareness materials for admins.",
     "CMMC Level 1 — AT.1.001."),
    ("Log Monitoring",
     "Review logs for suspicious activity (failed logins, unauthorized access).",
     "CMMC Level 2 — AU.2.041."),
    ("Policy and Procedure Updates",
     "Update website-related security policies (incident response, access control).",
     "CMMC Level 2 — Policy Documentation."),
    ("SSL/TLS Certificate Management",
     "Monitor SSL/TLS expiration and validate proper configuration.",
     "CMMC Level 1 — SC.1.175."),
    ("Content Review",
     "Review public website content for exposure of PII or CUI.",
     "CMMC Level 1 — SC.1.175."),
]
df_pm_tasks = pd.DataFrame(PM_TASKS, columns=["Task", "Description", "CMMC Reference"])

# ---------------------------------------------------------
# MAIN RENDER FUNCTION
# ---------------------------------------------------------
def render_cmmc_acronyms():
    """Display acronym glossary, PM tasks, and all tool categories with colored navbar buttons."""
    import streamlit as st

    st.subheader("🔐 CMMC 2.0 — Web Development Compliance Hub")

    # Colored buttons styled as nav
    button_style = """
        <style>
            div.stRadio > label > div[data-baseweb="radio"] > div:first-child {
                background-color: #D6EAF8;
                padding: 8px 12px;
                border-radius: 5px;
                font-weight: bold;
                font-size: 16px;
            }
            div.stRadio > label:hover > div[data-baseweb="radio"] > div:first-child {
                background-color: #85C1E9;
            }
        </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)

    section = st.radio(
        "Select View",
        ["Acronyms & Definitions", "PM Tasks & Responsibilities", 
         "Free & Low-Cost Tools", "Commercial Paid Tools", "GitLab Security Tools"],
        horizontal=True
    )

    # --- Acronyms ---
    if section == "Acronyms & Definitions":
        st.markdown("### Acronyms & Definitions")
        search_term = st.text_input("Search Acronym or Definition", "").strip().lower()
        filtered_df = df_acronyms.copy()
        if search_term:
            filtered_df = filtered_df[
                filtered_df["Acronym"].str.lower().str.contains(search_term) |
                filtered_df["Definition"].str.lower().str.contains(search_term)
            ]
        st.table(filtered_df)

    # --- PM Tasks ---
    elif section == "PM Tasks & Responsibilities":
        st.markdown("### PM Tasks & Responsibilities")
        st.table(df_pm_tasks)
        st.info("Interns should work under supervision. Document findings for CMMC audit readiness.")

    # --- Free Tools ---
    elif section == "Free & Low-Cost Tools":
        st.markdown("### Free & Low-Cost Tools")
        df_display = get_free_tools()
        df_display.index = df_display.index + 1
        st.table(df_display)

    # --- Paid Tools ---
    elif section == "Commercial Paid Tools":
        st.markdown("### Commercial Paid Tools")
        df_display = get_paid_tools()
        df_display.index = df_display.index + 1
        st.table(df_display)

    # --- GitLab Tools ---
    elif section == "GitLab Security Tools":
        st.markdown("### GitLab Security Tools")
        df_display = get_gitlab_tools()
        df_display.index = df_display.index + 1
        st.table(df_display)
