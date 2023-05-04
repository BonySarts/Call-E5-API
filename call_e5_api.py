name: Call E5 API

on:
  schedule:
    - cron: '0 0 * * *' # 每天 UTC 0 点触发任务
    # - cron: '0 12 * * 1' # 每周一 UTC 12 点触发任务

jobs:
  call_api_job:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v2

      - name: Set up Python 3.9
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install requests

      - name: Call API
        run: python call_e5_api.py
