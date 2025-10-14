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
#   - Legit Free / Low-Cost Security Tools (with cost and level tabs)
# ---------------------------------------------------------

import streamlit as st
import pandas as pd

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
# TOOL TABLE (with Cost & CMMC Level)
# ---------------------------------------------------------
TOOLS_DATA = [
    ("Security Headers", "Checks HTTP security headers like CSP, HSTS, and X-Frame-Options.", 
     "Web Header Configuration", "Free", "Level 1", "https://securityheaders.com/"),
    ("SSL Labs Server Test", "Grades your SSL/TLS configuration and identifies weak ciphers or expired certs.", 
     "Encryption / SSL Configuration", "Free", "Level 1", "https://www.ssllabs.com/ssltest/"),
    ("OWASP ZAP", "Dynamic web vulnerability scanner maintained by OWASP.", 
     "Web Application Scanning", "Free", "Level 1–2", "https://www.zaproxy.org/"),
    ("OpenVAS / Greenbone", "Open-source vulnerability scanner for web and network assessments.", 
     "Vulnerability Scanning", "Free", "Level 2", "https://www.greenbone.net/en/community-edition/"),
    ("Qualys Community Edition", "Free vulnerability scanning for up to 16 IPs or assets.", 
     "Vulnerability Scanning", "Free (limited)", "Level 2", "https://www.qualys.com/community-edition/"),
    ("Nikto", "Simple open-source web server scanner for outdated or insecure components.", 
     "Web Server Testing", "Free", "Level 1–2", "https://cirt.net/Nikto2"),
    ("Mozilla Observatory", "Analyzes web headers, TLS setup, and external scripts.", 
     "Web Configuration Review", "Free", "Level 1–2", "https://observatory.mozilla.org/"),
    ("Sucuri SiteCheck", "Free online malware and vulnerability scanner for websites.", 
     "Malware / Integrity Checking", "Free", "Level 1", "https://sitecheck.sucuri.net/"),
    ("Detectify", "Web vulnerability scanner with DevSecOps integrations (free trial).", 
     "Vulnerability Scanning", "Low-Cost (Trial)", "Level 2", "https://detectify.com/"),
    ("UpGuard BreachSight", "Monitors external attack surface and website exposures.", 
     "External Risk Monitoring", "Low-Cost (Free Tier)", "Level 2", "https://www.upguard.com/"),
    ("Let's Encrypt", "Provides free SSL/TLS certificates for secure HTTPS connections.", 
     "Encryption / Certificates", "Free", "Level 1", "https://letsencrypt.org/"),
    ("CIS CAT Lite", "Free tool for configuration assessment using CIS Benchmarks.", 
     "Configuration Compliance", "Free", "Level 2", "https://www.cisecurity.org/cis-cat-lite"),
]
df_tools = pd.DataFrame(TOOLS_DATA, columns=["Tool Name", "Description", "Category", "Cost", "CMMC Level", "URL"])

# Convert tool names to clickable links
df_tools["Tool Name"] = df_tools.apply(lambda x: f"[{x['Tool Name']}]({x['URL']})", axis=1)

# ---------------------------------------------------------
# MAIN RENDER FUNCTION
# ---------------------------------------------------------
def render_cmmc_acronyms():
    """Display acronym glossary, PM tasks, and vetted free tools."""
    st.subheader("🔐 CMMC 2.0 — Web Development Compliance Hub")

    section = st.radio(
        "Select View",
        ["Acronyms & Definitions", "PM Tasks & Responsibilities", "Free & Low-Cost Tools"],
        horizontal=True,
    )

    # --- ACRONYMS ---
    if section == "Acronyms & Definitions":
        st.markdown("Explore common **CMMC 2.0** and **web security** terms.")
        search_term = st.text_input("Search Acronym or Definition", "").strip().lower()
        filtered_df = df_acronyms.copy()
        if search_term:
            filtered_df = filtered_df[
                filtered_df["Acronym"].str.lower().str.contains(search_term)
                | filtered_df["Definition"].str.lower().str.contains(search_term)
            ]
        st.dataframe(filtered_df, use_container_width=True, hide_index=True)

    # --- PM TASKS ---
    elif section == "PM Tasks & Responsibilities":
        st.markdown("Web project tasks aligned with **CMMC 2.0** compliance goals.")
        st.dataframe(df_pm_tasks, use_container_width=True, hide_index=True)
        st.info("Interns should work under supervision. Document findings for CMMC audit readiness.")

    # --- FREE TOOLS ---
# --- FREE TOOLS ---
    elif section == "Free & Low-Cost Tools": st.markdown("Search for vetted **security tools** supporting CMMC 2.0 web compliance.")
    search = st.text_input("🔍 Search Tool, Category, or CMMC Level").lower()
    filtered_tools = df_tools.copy()
    if search:
        filtered_tools = filtered_tools[
            filtered_tools.apply(lambda row: search in row.to_string().lower(), axis=1)
        ]

    # Ensure all columns are strings to prevent truncation
    filtered_tools = filtered_tools.astype(str)

    # Render the full table reliably
    st.table(filtered_tools)

    st.caption("All listed tools are legitimate, free, or community-backed resources verified by OWASP, CIS, and NIST contributors.")
