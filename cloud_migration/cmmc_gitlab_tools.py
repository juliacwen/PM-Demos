# ---------------------------------------------------------
# cmmc_gitlab_tools.py
# Author: Julia Wen
# Date: 2025-10-13
#
# Description: gitlab security related tools
# ---------------------------------------------------------
import pandas as pd

def get_gitlab_tools():
    data = [
        {
            "Tool Name": "SAST (Static Application Security Testing)",
            "URL": "https://docs.gitlab.com/ee/user/application_security/sast/",
            "CMMC Level": "Level 2",
            "Cost": "GitLab Ultimate / Premium",
            "Notes": "Analyzes code and binaries for vulnerabilities. Supports SI.L2-3.14.1, SI.L2-3.14.2, CM.L2-3.4.7."
        },
        {
            "Tool Name": "DAST (Dynamic Application Security Testing)",
            "URL": "https://docs.gitlab.com/ee/user/application_security/dast/",
            "CMMC Level": "Level 2",
            "Cost": "GitLab Ultimate / Premium",
            "Notes": "Simulates attacks on running web apps. Supports SI.L2-3.14.2, SI.L2-3.14.1, SC.L2-3.13.2."
        },
        {
            "Tool Name": "Dependency Scanning",
            "URL": "https://docs.gitlab.com/ee/user/application_security/dependency_scanning/",
            "CMMC Level": "Level 2",
            "Cost": "GitLab Ultimate / Premium",
            "Notes": "Scans third-party libraries for vulnerabilities. Supports SI.L2-3.14.1, SI.L2-3.14.2, CM.L2-3.4.7."
        },
        {
            "Tool Name": "Secret Detection",
            "URL": "https://docs.gitlab.com/ee/user/application_security/secret_detection/",
            "CMMC Level": "Level 2",
            "Cost": "GitLab Ultimate / Premium",
            "Notes": "Detects exposed credentials, API keys, and tokens. Supports IA.L2-3.5.1, SI.L2-3.14.1, AC.L2-3.1.1."
        },
        {
            "Tool Name": "Container Scanning",
            "URL": "https://docs.gitlab.com/ee/user/application_security/container_scanning/",
            "CMMC Level": "Level 2",
            "Cost": "GitLab Ultimate / Premium",
            "Notes": "Analyzes Docker images for vulnerabilities and misconfigurations. Supports SI.L2-3.14.2, SI.L2-3.14.1, SC.L2-3.13.8."
        },
        {
            "Tool Name": "IaC (Infrastructure as Code) Scanning",
            "URL": "https://docs.gitlab.com/ee/user/application_security/iac_scanning/",
            "CMMC Level": "Level 2",
            "Cost": "GitLab Ultimate / Premium",
            "Notes": "Checks IaC templates for misconfigurations. Supports CM.L2-3.4.1, SI.L2-3.14.1, CM.L2-3.4.2."
        },
        {
            "Tool Name": "License Compliance Scanning",
            "URL": "https://docs.gitlab.com/ee/user/application_security/license_management/",
            "CMMC Level": "Level 2",
            "Cost": "GitLab Ultimate / Premium",
            "Notes": "Scans dependencies for license conflicts. Supports SA.L2-3.15.1, CM.L2-3.4.7."
        },
        {
            "Tool Name": "Fuzz Testing",
            "URL": "https://docs.gitlab.com/ee/user/application_security/fuzz_testing/",
            "CMMC Level": "Level 2",
            "Cost": "GitLab Ultimate / Premium",
            "Notes": "Generates arbitrary inputs to test web app robustness. Supports SI.L2-3.14.2, SI.L2-3.14.1."
        }
    ]
    df = pd.DataFrame(data)
    return df


