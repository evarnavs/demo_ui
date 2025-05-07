# Demo UI Automation

This repository contains an automated UI testing framework using **Selenium**, **Pytest**, and **Allure** for the client platform.

🔗 **Target URL:** [https://staging.usupport.online/client/](https://staging.usupport.online/client/)  
📊 **Live Allure Report:** [https://evarnavs.github.io/demo_ui](https://evarnavs.github.io/demo_ui)

---

## 🚀 Features

- End-to-end login flow automation
- Page Object Model (POM) structure
- Secure credentials via `.env` and GitHub Secrets
- Allure test reporting with **trend tracking**
- CI/CD using **GitHub Actions**
- Automatically deployed reports to **GitHub Pages**

---

## 📂 Project Structure

```
demo_ui/
├── tests/                  # Test scripts
│   └── test_login_flow.py
├── pages/                  # Page Object Models
│   ├── pre_login_page.py
│   └── login_page.py
├── locators/               # XPath locators (optional modularization)
├── conftest.py             # Fixtures and setup
├── requirements.txt
├── run_all.sh              # Local test runner script
├── .env                    # Environment variables (not committed)
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

1. **Clone the repo:**
   ```bash
   git clone https://github.com/evarnavs/demo_ui.git
   cd demo_ui
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.env` file**:
   ```env
   BASE_URL=https://staging.usupport.online
   EMAIL=your@email.com
   PASSWORD=your_password
   ```

---

## ✅ Running Tests Locally

You can run all tests and generate an Allure report with:

```bash
bash run_all.sh
```

This will:
- Run all tests via pytest
- Generate Allure report with trend support
- Open the report in your browser

---

## 📊 CI & GitHub Pages

Allure reports are automatically generated and published to **GitHub Pages** on every push to `main`.

### GitHub Actions includes:
- Running tests in CI
- Saving test results
- Publishing trends from `gh-pages` branch

✅ GitHub Secrets are used for credentials: `EMAIL`, `PASSWORD`, `BASE_URL`

🔐 **Note**: If you fork this repo, you'll need to [add your own secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets) to make CI work.

---

## 📎 Notes

- XPath locators are centralized for maintainability.
- Test trends are stored in the `history/` folder by Allure.
- `.env` is excluded from version control via `.gitignore`.
- Add Teardown with logout

---

## 📬 Author

Created by [@evarnavs](https://github.com/evarnavs)
