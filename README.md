Insurance Data Analysis & Data Versioning Project

Author: Yosef Maregn
Repository: insurance-week-3
Course Focus: Insurance Analytics / Data Engineering
Tools: Python, Git, Git LFS, DVC, Pandas, Matplotlib

1. Project Overview

This project focuses on building a reproducible, auditable, and version-controlled data analysis pipeline for an insurance-related dataset.
It demonstrates industry-standard practices used in financial and insurance organizations, where data traceability, reproducibility, and compliance are critical.

Two major goals were achieved in this project:

Task 1 – Exploratory Data Analysis (EDA) and Git + LFS

Task 2 – Data Version Control (DVC) implementation

2. Folder Structure
insurance-week-3/
│
├── data/
│   └── MachineLearningRating_v3/
│       └── MachineLearningRating_v3.txt  (tracked by DVC)
│
├── notebooks/
│   └── insurance_analysis.ipynb
│
├── scripts/
│
├── outputs/
│   └── saved graphs and analysis results
│
├── .dvc/
│
├── dvc-storage/     # Local DVC remote
│
├── README.md
├── .gitignore
├── .gitattributes
└── insurance_analysis.ipynb

3. Task 1 – Exploratory Data Analysis (EDA)

In this task, the main objective was to understand the dataset, inspect its structure, and extract initial insights.

✔ Key steps performed:

Loaded the dataset using Pandas

Inspected:

Data shape

Data types

Missing values

Generated summary statistics:

Mean

Median

Standard deviation

Min / Max

Created visualizations:

Histograms

Bar charts

Distribution plots

Compared selected attributes related to:

Risk

Claim

Rating patterns

✔ Main EDA findings (Summary)

The dataset contains structured numerical and categorical insurance features

Some attributes are highly skewed, indicating outliers

Certain features show strong variation, which is useful for:

Modeling

Risk assessment

Premium prediction

The data quality is acceptable for further modeling and analysis

All graphs were generated inside:

insurance_analysis.ipynb


These visualizations help support business insight and model development.

4. Task 1 – Git LFS Implementation

The dataset size exceeded GitHub’s 100MB limit:

MachineLearningRating_v3.txt ≈ 503 MB

✔ Solution:

Git LFS (Large File Storage) was implemented.

Tracked as:

data/MachineLearningRating_v3/MachineLearningRating_v3.txt


In .gitattributes:

filter=lfs diff=lfs merge=lfs -text


This allows version control of large files safely and efficiently.

✅ Large file now works with GitHub
✅ No push/pull errors
✅ Version controlled correctly

5. Task 2 – Data Version Control (DVC)

To ensure full reproducibility, even for data, DVC (Data Version Control) was installed and configured.

✔ Steps completed:

DVC initialized:

dvc init


Local remote storage created and connected:

dvc remote add -d localstorage ./dvc-storage


Data added to DVC:

dvc add data/MachineLearningRating_v3/MachineLearningRating_v3.txt


Data pushed to DVC storage:

dvc push


DVC tracking files committed to Git.

This ensures:

✅ Complete data versioning
✅ Reproducible results
✅ Audit-ready workflow
✅ Industry compliance practice

6. Branching Strategy Used
Branch	Purpose
main	Stable version
task-1	EDA + Git/LFS
task-2	DVC setup & data tracking

Each task was developed in a separate branch and merged correctly.

7. How To Reproduce This Project

Follow these steps:

1. Clone the repository
git clone https://github.com/yosefmaregn2017-droid/insurance-week-3.git
cd insurance-week-3

2. Set up environment
pip install pandas matplotlib seaborn dvc

3. Pull the data (from DVC remote)
dvc pull

4. Run the notebook

Open:

insurance_analysis.ipynb


And run all cells to regenerate the results and graphs.

8. Conclusion

This project successfully demonstrates:

✅ Real-world data engineering workflow

✅ Version control for code and data

✅ Reproducible analytics

✅ Use of Git + LFS + DVC

✅ Exploratory analysis for insurance decision-making

These practices align with regulated industry standards in:

Banking

Insurance

Finance

Risk Management

AI/ML Compliance Projects
