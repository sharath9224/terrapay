# Terrapay Data Management Tools

This repository consists of two main components designed to manage and analyze sales data for Terrapay: a Jupyter Notebook for data cleaning and insertion into an SQL database, and a Python CLI tool for querying this data.

## Description

The `sales.ipynb` Jupyter Notebook processes and cleans sales data, then inserts it into an SQL database, ensuring the data is primed for analysis. The `cli.py` script provides a command-line interface to run predefined SQL queries on this cleaned data, facilitating data retrieval and further analysis.

## Getting Started

### Dependencies

Ensure you have the following installed:

- Python 3.8 or higher
- Pandas for data manipulation
- SQLAlchemy for database interaction
- Jupyter to run and edit the notebook
- A SQL database (MySQL, PostgreSQL, etc.)

### Installation

Clone the repository to get started:

```bash
git clone https://github.com/yourusername/terrapay-analysis.git
cd terrapay-analysis
python cli.py "demand" "2010-01-12" "2011-01-10" "Hand Warmer Red Polka Dot"
