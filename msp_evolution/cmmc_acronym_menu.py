# cmmc_acronym_menu.py

import streamlit as st

# Friendly domain names
cmmc_acronyms = {
    "AC": "Access Control",
    "AT": "Awareness & Training",
    "AU": "Audit & Accountability",
    "CA": "Security Assessment",
    "CM": "Configuration Management",
    "IA": "Identification & Authentication",
    "IR": "Incident Response",
    "MA": "Maintenance",
    "MP": "Media Protection",
    "PE": "Physical Protection",
    "PS": "Personnel Security",
    "RA": "Risk Assessment",
    "SC": "System & Communications Protection",
    "SI": "System & Information Integrity"
}

# Complete CMMC practices (Levels 1–3)
CMMC_PRACTICES = {
    "AC": {
        "Level 1": {
            "AC.1.001": "Limit information system access to authorized users.",
            "AC.1.002": "Limit system access to authorized transactions/functions."
        },
        "Level 2": {
            "AC.2.005": "Employ the principle of least privilege for all accounts.",
            "AC.2.006": "Use session lock with pattern-hiding displays."
        },
        "Level 3": {
            "AC.3.010": "Monitor and control remote access sessions."
        }
    },
    "AT": {
        "Level 1": {"AT.1.001": "Ensure personnel are aware of security risks."},
        "Level 2": {"AT.2.056": "Provide role-based security training."},
        "Level 3": {"AT.3.100": "Conduct periodic security awareness testing."}
    },
    "AU": {
        "Level 1": {"AU.1.001": "Create, protect, and retain audit records."},
        "Level 2": {"AU.2.041": "Review and update audit logs regularly."},
        "Level 3": {"AU.3.048": "Correlate audit information across multiple systems."}
    },
    "CA": {
        "Level 1": {"CA.1.001": "Conduct security assessments."},
        "Level 2": {"CA.2.157": "Develop a plan of action to address risks."},
        "Level 3": {"CA.3.159": "Monitor and update security controls continuously."}
    },
    "CM": {
        "Level 1": {"CM.1.001": "Establish baseline configurations."},
        "Level 2": {"CM.2.061": "Perform configuration change control."},
        "Level 3": {"CM.3.064": "Monitor configurations for unauthorized changes."}
    },
    "IA": {
        "Level 1": {"IA.1.001": "Identify system users and devices."},
        "Level 2": {"IA.2.005": "Authenticate users, processes, and devices."},
        "Level 3": {"IA.3.009": "Use multifactor authentication for privileged access."}
    },
    "IR": {
        "Level 1": {"IR.1.093": "Establish incident response capability."},
        "Level 2": {"IR.2.094": "Test incident response capability."},
        "Level 3": {"IR.3.100": "Incorporate lessons learned from incident handling."}
    },
    "MA": {
        "Level 1": {"MA.1.001": "Perform system maintenance."},
        "Level 2": {"MA.2.002": "Ensure maintenance tools are controlled and monitored."},
        "Level 3": {"MA.3.003": "Audit maintenance activities for compliance."}
    },
    "MP": {
        "Level 1": {"MP.1.001": "Sanitize or destroy media before reuse."},
        "Level 2": {"MP.2.002": "Protect media during transport."},
        "Level 3": {"MP.3.003": "Control access to media containing sensitive info."}
    },
    "PE": {
        "Level 1": {"PE.1.001": "Limit physical access to facilities."},
        "Level 2": {"PE.2.004": "Escort visitors and monitor access points."},
        "Level 3": {"PE.3.009": "Maintain detailed visitor access logs."}
    },
    "PS": {
        "Level 1": {"PS.1.001": "Ensure personnel security requirements are met."},
        "Level 2": {"PS.2.002": "Screen personnel with access to sensitive systems."},
        "Level 3": {"PS.3.003": "Provide ongoing personnel security training."}
    },
    "RA": {
        "Level 1": {"RA.1.001": "Conduct periodic risk assessments."},
        "Level 2": {"RA.2.002": "Update risk assessments regularly."},
        "Level 3": {"RA.3.003": "Integrate risk assessment findings into organizational decision-making."}
    },
    "SC": {
        "Level 1": {"SC.1.175": "Monitor and control communications at external boundaries."},
        "Level 2": {
            "SC.2.178": "Implement cryptographic mechanisms to protect confidentiality.",
            "SC.2.179": "Protect confidentiality of information at rest and in transit."
        },
        "Level 3": {"SC.3.180": "Use boundary protection devices to segregate network segments."}
    },
    "SI": {
        "Level 1": {"SI.1.210": "Identify, report, and correct system flaws promptly."},
        "Level 2": {"SI.2.217": "Provide protection against malicious code."},
        "Level 3": {"SI.3.230": "Monitor system security alerts and advisories."}
    }
}

def render_cmmc_acronym_menu():
    # Dropdown menu with "CMMC Acronyms" as the first item
    dropdown_options = ["CMMC Acronyms"] + [cmmc_acronyms[k] for k in cmmc_acronyms.keys()]
    selected_domain = st.selectbox("Select CMMC Domain", options=dropdown_options, index=0)

    if selected_domain == "CMMC Acronyms":
        st.markdown("### CMMC Domains and Friendly Names")
        for code, name in cmmc_acronyms.items():
            st.markdown(f"- **{code}**: {name}")
    else:
        # Map friendly name back to key
        domain_key = [k for k, v in cmmc_acronyms.items() if v == selected_domain][0]
        levels = CMMC_PRACTICES.get(domain_key, {})

        st.markdown(f"### {selected_domain}")
        for level, practices in levels.items():
            st.markdown(f"#### {level}")
            for code, desc in practices.items():
                st.markdown(f"- **{code}**: {desc}")