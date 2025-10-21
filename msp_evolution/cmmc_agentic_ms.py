# cmmc_agentic_ms.py

import streamlit as st
import pandas as pd

# Detailed CMMC → Agentic → Microsoft mapping (30+ rows for demo purposes)
CMMC_AGENTIC_MS = [
    {"CMMC Practice": "AC.1.001: Limit system access to authorized users", 
     "Agentic Concept": "User Access Governance", "Microsoft Tool": "Azure AD Conditional Access"},
    {"CMMC Practice": "AC.2.005: Employ least privilege for accounts", 
     "Agentic Concept": "Role-Based Access Control", "Microsoft Tool": "Azure AD RBAC"},
    {"CMMC Practice": "AC.2.006: Use session lock with pattern-hiding displays", 
     "Agentic Concept": "Workstation Security", "Microsoft Tool": "Windows Security Policies"},
    {"CMMC Practice": "IA.2.005: Authenticate users, processes, and devices", 
     "Agentic Concept": "Identity Verification", "Microsoft Tool": "Azure AD MFA"},
    {"CMMC Practice": "IA.3.009: Use multifactor authentication for privileged access", 
     "Agentic Concept": "Privileged Access Management", "Microsoft Tool": "Azure AD PIM"},
    {"CMMC Practice": "SI.2.217: Provide protection against malicious code", 
     "Agentic Concept": "Threat Detection & Response", "Microsoft Tool": "Microsoft Defender Antivirus"},
    {"CMMC Practice": "IR.2.094: Test incident response capability", 
     "Agentic Concept": "Incident Management", "Microsoft Tool": "Microsoft Sentinel"},
    {"CMMC Practice": "SC.2.178: Implement cryptographic mechanisms", 
     "Agentic Concept": "Data Protection & Encryption", "Microsoft Tool": "Azure Key Vault, BitLocker"},
    {"CMMC Practice": "AU.2.041: Review and update audit logs regularly", 
     "Agentic Concept": "Continuous Monitoring", "Microsoft Tool": "Microsoft Sentinel, Azure Monitor"},
    {"CMMC Practice": "RA.2.002: Update risk assessments regularly", 
     "Agentic Concept": "Risk Management", "Microsoft Tool": "Microsoft Compliance Manager"},
    {"CMMC Practice": "CM.2.061: Perform configuration change control", 
     "Agentic Concept": "Configuration Governance", "Microsoft Tool": "Intune, Azure Policy"},
    {"CMMC Practice": "PE.2.004: Escort visitors and monitor access points", 
     "Agentic Concept": "Physical Security Awareness", "Microsoft Tool": "Teams Visitor Management (demo)"},
    {"CMMC Practice": "MP.2.002: Protect media during transport", 
     "Agentic Concept": "Data Handling & Transport", "Microsoft Tool": "Azure Information Protection"},
    {"CMMC Practice": "PS.2.002: Screen personnel with access to sensitive systems", 
     "Agentic Concept": "Personnel Security Screening", "Microsoft Tool": "HR Background Check Integration"},
    {"CMMC Practice": "MA.2.002: Ensure maintenance tools are controlled and monitored", 
     "Agentic Concept": "Maintenance Governance", "Microsoft Tool": "Intune, Endpoint Manager"},
    {"CMMC Practice": "SC.3.180: Use boundary protection devices to segregate network segments", 
     "Agentic Concept": "Network Segmentation", "Microsoft Tool": "Azure Firewall, NSGs"},
    {"CMMC Practice": "SI.3.230: Monitor system security alerts and advisories", 
     "Agentic Concept": "Security Operations Monitoring", "Microsoft Tool": "Microsoft Sentinel"},
    {"CMMC Practice": "AT.2.056: Provide role-based security training", 
     "Agentic Concept": "Security Awareness", "Microsoft Tool": "Microsoft Learn / Security Training"},
    {"CMMC Practice": "AU.3.048: Correlate audit information across multiple systems", 
     "Agentic Concept": "Integrated Auditing", "Microsoft Tool": "Microsoft Sentinel Workbooks"},
    {"CMMC Practice": "IR.3.100: Incorporate lessons learned from incident handling", 
     "Agentic Concept": "Continuous Improvement", "Microsoft Tool": "Microsoft Sentinel Incident Analytics"},
    {"CMMC Practice": "CM.3.064: Monitor configurations for unauthorized changes", 
     "Agentic Concept": "Configuration Integrity", "Microsoft Tool": "Azure Policy, Intune Compliance"},
    {"CMMC Practice": "RA.3.003: Integrate risk assessment findings into decision-making", 
     "Agentic Concept": "Enterprise Risk Governance", "Microsoft Tool": "Microsoft Compliance Manager"},
    {"CMMC Practice": "MP.3.003: Control access to media containing sensitive info", 
     "Agentic Concept": "Media Security Controls", "Microsoft Tool": "Azure Information Protection"},
    {"CMMC Practice": "PE.3.009: Maintain detailed visitor access logs", 
     "Agentic Concept": "Physical Security Logging", "Microsoft Tool": "Teams/SharePoint Logs (demo)"},
    {"CMMC Practice": "PS.3.003: Provide ongoing personnel security training", 
     "Agentic Concept": "Continuous Personnel Security", "Microsoft Tool": "Microsoft Learn / Security Modules"},
    {"CMMC Practice": "SI.1.210: Identify, report, and correct system flaws promptly", 
     "Agentic Concept": "Vulnerability Management", "Microsoft Tool": "Microsoft Defender Vulnerability Management"},
    {"CMMC Practice": "SC.2.179: Protect confidentiality of information at rest and in transit", 
     "Agentic Concept": "Data Encryption & Privacy", "Microsoft Tool": "Azure Storage Encryption, TLS"},
    {"CMMC Practice": "AC.1.002: Limit system access to authorized transactions/functions", 
     "Agentic Concept": "Access Control Policies", "Microsoft Tool": "Azure AD Conditional Access Policies"},
    {"CMMC Practice": "IA.1.001: Identify system users and devices", 
     "Agentic Concept": "Identity Inventory & Management", "Microsoft Tool": "Azure AD User & Device Management"},
    {"CMMC Practice": "MA.3.003: Audit maintenance activities for compliance", 
     "Agentic Concept": "Maintenance Auditing", "Microsoft Tool": "Intune Compliance Reports"},
]

def render_cmmc_agentic_ms():
    """Render a side-by-side table of CMMC practices, Agentic concepts, and Microsoft tools."""
    
    df = pd.DataFrame(CMMC_AGENTIC_MS)
    
    st.markdown("### CMMC Practices ↔ Agentic Concepts ↔ Microsoft Tools")
    
    # Render each row as side-by-side columns
    for idx, row in df.iterrows():
        col1, col2, col3 = st.columns([3, 3, 3])
        with col1:
            st.markdown(f"**CMMC**: {row['CMMC Practice']}")
        with col2:
            st.markdown(f"**Agentic**: {row['Agentic Concept']}")
        with col3:
            st.markdown(f"**Microsoft**: {row['Microsoft Tool']}")
