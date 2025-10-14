# ---------------------------------------------------------
# cmmc_free_tools.py
# Author: Julia Wen
# Date: 2025-10-12
#
# Description: CMMC related free or low cost tools
# ---------------------------------------------------------
import pandas as pd

def get_free_tools():
    data = [
        {
            "Tool Name": "HTTP Security Headers Scanner",
            "URL": "https://securityheaders.com/",
            "CMMC Level": "Level 2",
            "Cost": "Free",
            "Notes": "Checks security headers (CSP, HSTS, X-Frame-Options). Supports SC.L2-3.13.8, SI.L2-3.14.1, SC.L2-3.13.2."
        },
        {
            "Tool Name": "SSL/TLS Configuration Tester",
            "URL": "https://www.ssllabs.com/ssltest/",
            "CMMC Level": "Level 2",
            "Cost": "Free",
            "Notes": "Validates TLS setup, cipher suites, certificates. Supports SC.L2-3.13.1, SC.L2-3.13.5, SC.L2-3.13.8."
        },
        {
            "Tool Name": "OWASP ZAP",
            "URL": "https://www.zaproxy.org/",
            "CMMC Level": "Level 2",
            "Cost": "Free / Open Source",
            "Notes": "Web vulnerability scanning (SQLi, XSS, CSRF). Supports SI.L2-3.14.1, SI.L2-3.14.2, SC.L2-3.13.2."
        },
        {
            "Tool Name": "ModSecurity WAF",
            "URL": "https://modsecurity.org/",
            "CMMC Level": "Level 2",
            "Cost": "Free / Open Source",
            "Notes": "Web Application Firewall to block attacks. Supports SC.L2-3.13.2, SI.L2-3.14.5."
        },
        {
            "Tool Name": "ELK Stack (Elasticsearch, Logstash, Kibana)",
            "URL": "https://www.elastic.co/elk-stack",
            "CMMC Level": "Level 2",
            "Cost": "Free / Open Source",
            "Notes": "Logging and monitoring web app security events. Supports AU.L2-3.3.1, AU.L2-3.3.2, SI.L2-3.14.5."
        },
        {
            "Tool Name": "Dependabot (GitHub)",
            "URL": "https://github.com/dependabot",
            "CMMC Level": "Level 2",
            "Cost": "Free for public repos",
            "Notes": "Dependency scanning for vulnerabilities. Supports SI.L2-3.14.1, SI.L2-3.14.2."
        },
        {
            "Tool Name": "OWASP Dependency-Check",
            "URL": "https://owasp.org/www-project-dependency-check/",
            "CMMC Level": "Level 2",
            "Cost": "Free / Open Source",
            "Notes": "Scan project dependencies for known vulnerabilities. Supports SI.L2-3.14.1, SI.L2-3.14.2."
        },
        {
            "Tool Name": "Ansible",
            "URL": "https://www.ansible.com/",
            "CMMC Level": "Level 2",
            "Cost": "Free / Open Source",
            "Notes": "Configuration management to enforce secure web server setups. Supports CM.L2-3.4.1, CM.L2-3.4.2."
        },
        # Add more free/low-cost tools here if needed
    ]
    df = pd.DataFrame(data)
    return df

