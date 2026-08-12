# 🚀 TestPilot

A Python Selenium Automation Testing Framework built using the Page Object Model (POM).

TestPilot demonstrates a scalable UI automation framework with support for functional testing, accessibility validation, performance testing, broken link detection, HTML reporting, and GitHub Actions CI.

---

## ✨ Features

- ✅ Homepage Validation
- ✅ Search Functionality Testing
- ✅ Positive & Negative Search Scenarios
- ✅ Broken Link Detection
- ✅ Accessibility Testing (axe-core)
- ✅ Browser Performance Testing
- ✅ HTML Test Report
- ✅ Logging
- ✅ Configurable Test Settings
- ✅ GitHub Actions Continuous Integration

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.13 |
| UI Automation | Selenium WebDriver |
| Design Pattern | Page Object Model (POM) |
| Test Framework | Custom Test Runner |
| Accessibility | axe-selenium-python |
| HTTP Validation | requests |
| Reporting | HTML Report |
| CI/CD | GitHub Actions |
| Browser | Google Chrome |

---

## 📂 Project Structure

```
TestPilot
│
├── config/
│
├── core/
│   ├── browser.py
│   ├── logger.py
│   ├── report.py
│   ├── test_runner.py
│   └── utils.py
│
├── pages/
│
├── tests/
│   ├── homepage_test.py
│   ├── search_test.py
│   ├── broken_link_test.py
│   ├── accessibility_test.py
│   └── performance_test.py
│
├── reports/
├── screenshots/
│
├── main.py
└── requirements.txt
```

---

## 🧪 Implemented Tests

### Homepage Test

- Verify homepage URL
- Verify page title
- Capture screenshot

---

### Search Test

- Positive search validation
- Negative search validation
- Verify proper "Nothing found" message

---

### Broken Link Test

- Collect all page links
- Remove duplicate URLs
- Skip JavaScript, mailto and tel links
- Validate HTTP status codes
- Detect broken internal links

---

### Accessibility Test

Powered by **axe-core**

Checks for:

- Heading hierarchy
- Landmark structure
- List semantics
- WCAG accessibility violations

---

### Performance Test

Uses the browser **Performance API** to measure:

- Total Load Time
- DOM Ready Time
- Response Time
- HTTP Status

---

## ▶️ How to Run

Install dependencies

```bash
pip install -r requirements.txt
```

Run the framework

```bash
python main.py
```

---

## 📊 Sample Output

```
===== Homepage Test =====
PASSED

===== Search Test =====
PASSED

===== Broken Link Test =====
PASSED

===== Accessibility Test =====
PASSED

===== Performance Test =====
PASSED
```

---

## 🔄 Continuous Integration

GitHub Actions automatically:

- Install dependencies
- Launch Chrome (Headless)
- Execute all tests
- Display pass/fail status

---

## 📌 Future Improvements

- Parallel execution
- Cross-browser testing
- Screenshot on failure
- Allure Report integration
- Docker support
- Slack notifications

---
## Framework Architecture
          +----------------+
          |    main.py     |
          +-------+--------+
                  |
                  v
          +----------------+
          |  Test Runner   |
          +-------+--------+
                  |
     +------------+------------+
     |            |            |
     v            v            v
 Homepage     Search     Broken Link
     |            |            |
     +------------+------------+
                  |
                  v
        Accessibility Test
                  |
                  v
        Performance Test
                  |
                  v
      HTML Report + Logger
                  |
                  v
        GitHub Actions CI
        
## HTML Report
<img width="1018" height="528" alt="image" src="https://github.com/user-attachments/assets/60a6ece4-c132-44bc-a1b9-5ee7fa6521a3" />

## GitHub Actions
<img width="1206" height="576" alt="image" src="https://github.com/user-attachments/assets/971f611d-de74-4a51-89fd-82067bb798fa" />

## 👩‍💻 Author

**Eunbi (Abby) Lee**

QA Automation Engineer

Toronto, Canada
