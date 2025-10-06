# PM_Demos

**Author:** Julia Wen ([wendigilane@gmail.com](mailto:wendigilane@gmail.com))
**License:** MIT

This repository contains **project and product management demos**, currently including a **Cloud Migration Dashboard**. Each demo 
is organized in its own directory under the repository.

## Current Structure

```
PM_Demos/
├── requirements.txt             # Python dependencies
├── cloud/                        # Cloud Migration Dashboard demo
│   └── cloud_pm_dashboard.py    # Main Streamlit dashboard for cloud migration
```

> More demo directories can be added here in the future.

## Cloud Migration Dashboard Features

* Interactive diagrams:

  * **Flow Diagram**: Migration lifecycle phases and tasks.
  * **Hierarchical WBS Tree**: Phase and task breakdown.
  * **Swimlane Chart**: Roles, phases, and tasks.
* **Theme support**: Dark and Light modes with professional palette.
* **Responsive layout** for different screen widths.
* Role-based colors in Swimlane chart.

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd PM_Demos
```

2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run a dashboard with Streamlit (example for the cloud demo):

```bash
streamlit run cloud/cloud_pm_dashboard.py
```

* Use the sidebar to select:

  * **Theme**: Dark / Light
  * **Diagram type**: Flow, WBS, or Swimlane
* Diagrams are interactive and automatically scale.

## Notes

* AI tools were used in assisting with reviewing, refining, and enhancing portions of the python codebase.

## License
MIT License  
© 2025 Julia Wen (wendigilane@gmail.com)

