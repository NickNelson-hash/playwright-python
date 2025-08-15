import pytest
from datetime import datetime
import os

# Generate timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
report_dir = f"reports/report_{timestamp}"
os.makedirs(report_dir, exist_ok=True)

# Define report path
report_path = os.path.join(report_dir, "report.html")

# Run pytest with HTML report
pytest.main([
    "tests",  # or your test folder
    f"--html={report_path}",
    "--self-contained-html",
    "--capture=tee-sys"
])
