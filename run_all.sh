#!/bin/bash

echo "Running UI tests and collecting Allure results..."

# Step 1: Run tests
pytest --alluredir=allure-results
test_status=$?

# Step 2: Preserve trend history if available
if [ -d "allure-report/history" ]; then
  echo "Copying history to preserve trend..."
  mkdir -p allure-results/history
  cp -R allure-report/history/* allure-results/history/
else
  echo "ℹNo previous Allure history found — trend tracking will start fresh."
fi

# Step 3: Generate Allure report only if tests passed
if [ $test_status -eq 0 ]; then
  echo "Generating new Allure report..."
  allure generate allure-results -o allure-report --clean

  echo "Opening Allure report..."
  allure open allure-report
else
  echo "Tests failed — skipping report generation."
fi
