"""Google Cloud project configuration."""

from os import getenv, path
from dotenv import load_dotenv


# Load variables from .env
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


# Google GCP and BigQuery configurations.
GCP_PROJECT_ID: str = getenv("GCP_PROJECT_ID")
GCP_BIGQUERY_TABLE_ID: str = getenv("GCP_BIGQUERY_TABLE_ID")
GCP_BIGQUERY_DATASET_ID: str = getenv("GCP_BIGQUERY_DATASET_ID")
GCP_BIGQUERY_FULL_TABLE_ID: str = (
    f"{GCP_PROJECT_ID}.{GCP_BIGQUERY_DATASET_ID}.{GCP_BIGQUERY_TABLE_ID}"
)
GCP_BIGQUERY_URI = f'bigquery://{GCP_PROJECT_ID}/{GCP_BIGQUERY_DATASET_ID}'
