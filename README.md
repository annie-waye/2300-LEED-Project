LEED Building Analysis
==============================
Analyzing LEED certified buildings in Massachusetts.

Project Organization
------------

    ├── LICENSE
    ├── Makefile            <- The Makefile with commands like `make data` or `make train`.
    ├── README.md           <- The top-level README for developers.
    │
    ├── docs                <- A default Sphinx project (see sphinx-doc.org)
    │
    ├── models              <- The trained and serialized models, model predictions, or model summaries.
    │
    ├── notebooks           <- Jupyter notebooks (Naming convention `1.0-jqp-initial-data-exploration`)
    │
    ├── references          <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports             <- The generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures         <- The generated graphics and figures
    │
    ├── requirements.txt    <- The requirements file for reproducing the analysis environment
    │
    ├── src                 <- Source code
    │   ├── __init__.py     <- Makes src a Python module
    │   │
    │   ├── common
    │   │
    │   ├── data            <- The scripts to download or generate data.
    │   │   ├── raw         <- The original, immutable data dump.
    │   │   └── make_dataset.py
    │   │   └── prepare.py  <- prep data for processing
    │   │   └── process.py  <- fit the data
    │   │   └── clean.py    <- clean data, remove duplicates
    │   │   └── plot.py     <- preliminary plotting
    │   │   └── usgbc.py    <- Project File (The U.S. Green Building Council)
    │   │
    │   ├── evaluation
    │   │
    │   ├── features        <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models          <- Scripts to train models and then use trained models to make predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization   <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    ├── test_environment.py
    │
    └── tox.ini             <- The tox file with settings for running tox (see tox.testrun.org)


--------

## Authors **Jay Myles and Annie Waye**: [J. Myles](https://github.com/j-Myles) , [A. Waye](https://github.com/annie-waye)  

Version Tracker
------------

0.1.1   Created repo and started Github (Oct 22)
0.1.2   Testing commit (Oct 22)
0.2.1   Merged pull request from Jay, adding raw data, metrics, pre-processing functions (Oct 24)
0.3.1   Updated README (Oct 24)
0.4.1   Merged pull request from Jay, adding data processing, preliminary polotting (Oct 27)
0.4.2   Updated README (Oct 28)
0.5.1   Moved raw data outside src (Nov 5)
0.5.2   Added file pointers to pass into function (Nov 5)
0.5.3   Prepare for docstrings on all functions (Nov 5)
0.5.4   add input arg to data.fetch_data to specify path (Nov 5)
0.5.5   Format improvements (Nov 5)
0.5.6   Added notebook for HW 3.2 (Nov 5)
0.5.7   Updated plot function (Nov 5)
0.5.8   Updated USGBC.py, main file  (Nov 5)
0.5.9   Merge branch "hw32", hw assignment 3.2 (Nov 5)
0.6.1   Merged pull request from Jay, adding linear regression (Dec 12)