# ---------------------------------------------------------
# cmmc_paid_tools.py
# Author: Julia Wen
# Date: 2025-10-12
#
# Description: CMMC related commercial tools
# ---------------------------------------------------------
import pandas as pd

def get_paid_tools():
    data = [
        {
            "Tool Name": "Tenable.io / Nessus",
            "URL": "https://www.tenable.com/products/nessus",
            "CMMC Level": "Level 2",
            "Cost": "Commercial",
            "Notes": "Vulnerability scanning for web servers and apps. Supports SI.L2-3.14.1, SI.L2-3.14.2."
        },
        {
            "Tool Name": "Burp Suite Professional",
            "URL": "https://portswigger.net/burp",
            "CMMC Level": "Level 2",
            "Cost": "Commercial",
            "Notes": "Dynamic application security testing, including business logic flaws, session management, and APIs. Supports SI.L2-3.14.1, SI.L2-3.14.2, AC.L2-3.1.20."
        },
        {
            "Tool Name": "Netsparker (Invicti)",
            "URL": "https://www.invicti.com/",
            "CMMC Level": "Level 2",
            "Cost": "Commercial",
            "Notes": "Runtime vulnerability scanning for web apps, detects misconfigurations and injection flaws. Supports SI.L2-3.14.1, SI.L2-3.14.2, AC.L2-3.1.22."
        },
        {
            "Tool Name": "Acunetix",
            "URL": "https://www.acunetix.com/",
            "CMMC Level": "Level 2",
            "Cost": "Commercial",
            "Notes": "DAST for web apps and APIs, identifies runtime vulnerabilities. Supports SI.L2-3.14.1, SI.L2-3.14.2."
        },
        {
            "Tool Name": "SonarQube Enterprise",
            "URL": "https://www.sonarqube.org/",
            "CMMC Level": "Level 2",
            "Cost": "Commercial",
            "Notes": "Static code analysis for security flaws and coding standards. Supports SI.L2-3.14.1, CM.L2-3.4.7, SI.L2-3.14.2."
        },
        {
            "Tool Name": "Checkmarx",
            "URL": "https://checkmarx.com/",
            "CMMC Level": "Level 2",
            "Cost": "Commercial",
            "Notes": "Advanced SAST for web frameworks and APIs. Supports SI.L2-3.14.1, CM.L2-3.4.7."
        },
        {
            "Tool Name": "Splunk Enterprise",
            "URL": "https://www.splunk.com/",
            "CMMC Level": "Level 2",
            "Cost": "Commercial",
            "Notes": "Logs and monitoring for web servers and apps. Supports AU.L2-3.3.1, AU.L2-3.3.2, SI.L2-3.14.5."
        }
    ]
    df = pd.DataFrame(data)
    return df

