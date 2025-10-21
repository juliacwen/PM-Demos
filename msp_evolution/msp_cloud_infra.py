def render_msp_vs_cloud_security_comparison():
    import streamlit as st
    import pandas as pd

    # --- 1️⃣ AI / ML Impact First ---
    st.markdown("## 🤖 AI / ML Impact on MSP & Cybersecurity")
    st.markdown("""
### MSP Operations
- Predictive monitoring & anomaly detection (e.g., via RMM analytics dashboards)
- AI-assisted threat detection and alert prioritization (EDR/SOCaaS platforms)
- Automated remediation and policy enforcement (PowerShell / RMM scripts with AI suggestions)
- Intelligent workflow automation and compliance tracking (SOP / PSA integrations)

### Microsoft Ecosystem
- ML-driven security analytics (Microsoft Sentinel, Defender XDR)
- AI-assisted incident response and risk scoring
- Intelligent identity and access management (Azure AD / Entra ID risk-based MFA)
- AI-enhanced automation for cloud and hybrid environments (Azure Logic Apps, Power Automate AI)

### AWS Cloud
- AI-powered threat detection and anomaly scoring (GuardDuty, Security Hub insights)
- Intelligent prioritization of security events
- Predictive operations and capacity optimization (CloudWatch, AWS Compute Optimizer)
- AI-driven monitoring for multi-tenant cloud environments

### VMware Stack
- AI-based infrastructure monitoring and predictive modeling (vRealize AI Ops)
- Endpoint and workload threat detection using ML (Carbon Black / VMware Security)
- Behavioral analytics for security and compliance (Workspace ONE Intelligence)
- Workload optimization and operational insights via AI (vRealize / Aria Operations)
""")


    st.divider()

    # --- 2️⃣ 4-Column Stack Snapshot ---
    col_msp, col_ms, col_aws, col_vmware = st.columns(4)

    # --- MSP Column ---
    with col_msp:
        st.markdown("### 🧩 MSP Tools")
        st.markdown("""
        - Auvik (Network Monitoring)
        - Arctic Wolf (SOCaaS / MDR)
        - IT Glue (Documentation / PSA)
        - Datto RMM (Remote Management)
        - ConnectWise, NinjaOne
        - Focus: Multi-tenant monitoring, cost optimization, RMM/PSA integration, SOPs and runbooks
        """)

    # --- Microsoft Column ---
    with col_ms:
        st.markdown("### 🏢 Microsoft Ecosystem")
        st.markdown("**Virtualization Layer (On-Prem)**")
        st.markdown("- Hyper-V (VM host, multi-tenant capable)")
        st.markdown("- SCVMM / SCOM (Central management & monitoring)")
        st.markdown("")
        st.markdown("**Hybrid Cloud Layer**")
        st.markdown("- Azure Stack HCI (Hyper-V integrated hybrid compute)")
        st.markdown("- Azure Arc / Lighthouse (Multi-tenant management)")
        st.markdown("")
        st.markdown("**Public Cloud Layer**")
        st.markdown("- Azure Cloud (VMs, App Services, Storage)")
        st.markdown("- Azure Monitor, Defender for Cloud, Sentinel")
        st.markdown("")
        st.markdown("**AI & Automation Layer**")
        st.markdown("- Copilot, Fabric, Azure OpenAI, Azure ML / MLOps")

    # --- AWS Column ---
    with col_aws:
        st.markdown("### ☁️ AWS Stack")
        st.markdown("""
        - EC2 (Compute / Virtualization)
        - CloudWatch (Monitoring)
        - GuardDuty, Inspector, Macie (Security)
        - Control Tower / Organizations (Multi-account mgmt)
        - SageMaker, Bedrock (AI / ML)
        - CloudTrail, Config, Security Hub (Auditing & posture)
        """)

    # --- VMware Column ---
    with col_vmware:
        st.markdown("### 🧱 VMware Stack")
        st.markdown("**On-Prem Layer**")
        st.markdown("- vSphere / ESXi (Virtualization Hosts)")
        st.markdown("- vCenter Server (Cluster Management)")
        st.markdown("")
        st.markdown("**Hybrid Layer**")
        st.markdown("- VMware Cloud Foundation (Integrated Management Stack)")
        st.markdown("- NSX (Network Virtualization & Security), HCX (Migration / Hybrid Connectivity)")
        st.markdown("")
        st.markdown("**Cloud Layer**")
        st.markdown("- VMware Cloud on AWS / Azure VMware Solution / Google VMware Engine")
        st.markdown("")
        st.markdown("**Security & AI**")
        st.markdown("- Carbon Black (EDR / XDR), Aria Operations, Tanzu (Containers / AI Ops)")

    st.divider()

    # --- 3️⃣ MSP & Cloud Platforms vs AI Tools Comparison DataFrame ---
    st.markdown("### 🧠 MSP & Cloud Platforms vs AI Tools Comparison")
    st.caption(
        "Comprehensive comparison across MSP, Microsoft, AWS, VMware, Google, and Open Source/Community AI tools "
        "covering operations, security, cloud infrastructure, identity management, compliance, and AI/ML pipelines."
    )

    data = {
        "Category": [
            "Monitoring & Management",
            "Network Visibility",
            "Documentation & Knowledge Base",
            "IT Service Management (ITSM)",
            "Endpoint / Device Management",
            "Automation & Scripting",
            "Cloud Infrastructure",
            "Identity & Access Management (IAM)",
            "Authentication / Authorization / SSO",
            "Security / Compliance (CMMC, NIST, ISO)",
            "Threat Detection & Response",
            "Configuration & Policy Management",
            "Model Development & Training",
            "Generative AI / LLMs",
            "Code / Dev AI",
            "MLOps / Deployment",
            "Analytics & AI-assisted Operations",
        ],
        "MSP Tools": [
            "RMM (NinjaOne, Datto, Kaseya)",
            "Auvik",
            "IT Glue (Runbooks, SOPs, Password Vault)",
            "PSA Tools (ConnectWise Manage, Autotask)",
            "NinjaOne / Syncro RMM",
            "RMM scripts, PowerShell automation",
            "Client-hosted or reseller-managed clouds",
            "Active Directory / Azure AD Connect",
            "RMM-based auth, shared credentials, MFA add-ons",
            "CMMC guidance, manual tracking",
            "EDR, SOCaaS (Datto, Huntress), Arctic Wolf MDR",
            "Policy enforcement via RMM/PSA templates",
            "Custom ML pipelines, Python scripts",
            "External APIs (OpenAI, LangChain)",
            "Limited; mostly automation scripts",
            "Custom workflow automation via RMM",
            "Predictive alerts using Datto EDR, Huntress ML",
        ],
        "Microsoft Stack": [
            "Azure Monitor, Azure Arc, Intune",
            "Azure Network Watcher, Traffic Analytics",
            "SharePoint, Confluence integration",
            "ServiceNow + OMS",
            "Intune, Endpoint Manager",
            "Power Automate, Azure Functions, Logic Apps",
            "Microsoft Azure (IaaS, PaaS, SaaS)",
            "Azure AD / Entra ID, RBAC",
            "Azure AD SSO, Conditional Access, OAuth2",
            "Microsoft Purview, Defender Suite, CMMC alignment",
            "Microsoft Sentinel, Defender XDR",
            "Azure Policy, Defender posture management",
            "Azure ML, Cognitive Services",
            "Azure OpenAI Service, GPT models",
            "GitHub Copilot (MS-owned), Power Automate AI features",
            "Azure ML pipelines, Azure DevOps integration",
            "Sentinel analytics, Defender ML insights",
        ],
        "AWS Stack": [
            "AWS Systems Manager, CloudWatch",
            "VPC Flow Logs, Network Manager, GuardDuty",
            "Confluence, ServiceNow integration",
            "ServiceNow + AWS Service Management Connector",
            "AWS Systems Manager Inventory",
            "Lambda, Step Functions, Systems Manager Automation",
            "AWS Cloud (EC2, ECS, EKS, S3, etc.)",
            "AWS IAM, IAM Identity Center",
            "Cognito, IAM Policies, SAML 2.0 federation",
            "AWS Artifact, Security Hub, Audit Manager",
            "GuardDuty, Inspector, Macie, Security Hub",
            "AWS Config, Control Tower, SCPs",
            "SageMaker, Comprehend, Rekognition, Bedrock",
            "Bedrock LLMs, CodeWhisperer",
            "CodeWhisperer, GPT integrations via Bedrock",
            "SageMaker pipelines, deployment automation",
            "GuardDuty ML, Security Hub anomaly detection",
        ],
        "VMware Stack": [
            "vCenter, Aria Operations",
            "Aria Operations for Networks",
            "Confluence, Aria Automation Config",
            "ServiceNow (integrated with Aria Automation)",
            "Horizon, Workspace ONE",
            "vRealize Orchestrator, Aria Automation",
            "VMware Cloud Foundation, VMware Cloud on AWS / Azure VMware Solution",
            "VMware Identity Manager, Workspace ONE Access",
            "SSO via vCenter, SAML, OAuth, OIDC",
            "CMMC readiness templates in Aria Ops",
            "Carbon Black Cloud, NSX IDS/IPS, vSphere Trust Authority",
            "vRealize / Aria Automation Config, NSX Policy",
            "vRealize AI, AI Ops, workload optimization",
            "vRealize AI Ops predictive modeling",
            "Workspace ONE Intelligence predictive analytics",
            "vRealize AI Ops pipelines",
            "Carbon Black ML, NSX AI-driven analytics",
        ],
        "Google AI Tools": [
            "Vertex AI monitoring, Cloud Operations Suite",
            "VPC Flow Logs, Chronicle Security Analytics",
            "Confluence / internal documentation integrations",
            "ServiceNow integration",
            "Google Endpoint Management",
            "Cloud Functions, Cloud Run automation",
            "Google Cloud Platform",
            "Google IAM, Cloud Identity",
            "SSO via Google Workspace, SAML 2.0",
            "CMMC/FedRAMP compliance via templates & controls",
            "Security Command Center, Chronicle",
            "Organization policies, Config Connector",
            "Vertex AI, TensorFlow, Vertex Training",
            "Grok LLMs, PaLM models",
            "Copilot-style tools via AI Hub",
            "Vertex pipelines, MLOps",
            "Security insights via Chronicle / AI Ops",
        ],
        "Open Source / GitHub AI Tools": [
            "LangChain, Hugging Face, custom Python scripts",
            "Open-source network analytics or monitoring scripts",
            "Markdown, GitHub Wiki, internal documentation repos",
            "Jira, Redmine, or other OSS ITSM",
            "OS-level management scripts, Ansible, SaltStack",
            "Python, Bash, Ansible, MLflow automation",
            "On-prem or cloud-agnostic deployment",
            "LDAP, Keycloak, OpenID Connect",
            "SAML, OAuth2, OIDC implementations",
            "Compliance check scripts, OpenSCAP",
            "Prometheus + AI alerting, custom ML monitoring",
            "Terraform / Ansible / policy-as-code",
            "LangChain, Hugging Face Transformers",
            "OpenAI API, LLaMA, GPT models",
            "GitHub Copilot, CodeWhisperer, CodeGPT",
            "MLflow, BentoML, Flyte pipelines",
            "Custom anomaly detection, predictive analytics",
        ],
    }

    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

    st.markdown(
        """
        **Summary:**  
        - **MSPs** rely on RMM, SOCaaS, and Arctic Wolf MDR for operations and security.  
        - **Microsoft** provides Sentinel, Defender XDR, and Azure ML/OpenAI integrations.  
        - **AWS** provides GuardDuty, Inspector, Macie, Security Hub, and SageMaker/Bedrock AI.  
        - **VMware** provides Carbon Black Cloud, NSX IDS/IPS, Aria AI Ops, and Workspace ONE Intelligence.  
        - **Google** offers Vertex AI, Grok LLMs, and Chronicle analytics.  
        - **Open Source / GitHub** provides flexible AI/ML pipelines, LangChain, Hugging Face, and Copilot tools.
        """
    )

    st.divider()

    # --- 4️⃣ On-Prem → Hybrid → Cloud Flow at End ---
    st.markdown("## ☁️ On-Prem, Hybrid, and Cloud Architecture (Microsoft & VMware)")

    st.markdown("""
    <style>
    .flow-box {
        border: 1px solid #444;
        border-radius: 10px;
        padding: 8px 12px;
        margin: 4px;
        display: inline-block;
        background-color: rgba(30, 41, 59, 0.06);
    }
    .arrow {
        display: inline-block;
        margin: 0 10px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🏢 Microsoft Stack (On-Prem → Hybrid → Cloud)")
        st.markdown("""
        <div style='text-align:center'>
            <div class='flow-box'>Hyper-V / SCVMM (On-Prem)</div>
            <span class='arrow'>➡️</span>
            <div class='flow-box'>Azure Stack HCI / Azure Arc (Hybrid)</div>
            <span class='arrow'>➡️</span>
            <div class='flow-box'>Azure Cloud (Public)</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("### 🧱 VMware Stack (On-Prem → Hybrid → Cloud)")
        st.markdown("""
        <div style='text-align:center'>
            <div class='flow-box'>vSphere / ESXi (On-Prem)</div>
            <span class='arrow'>➡️</span>
            <div class='flow-box'>vCenter / Cloud Foundation (Hybrid)</div>
            <span class='arrow'>➡️</span>
            <div class='flow-box'>VMware Cloud on AWS / Azure / GCP (Public)</div>
        </div>
        """, unsafe_allow_html=True)
