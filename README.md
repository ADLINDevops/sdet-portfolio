# 🧪 SDET Portfolio — Adlin Xavier

![SDET Portfolio](https://github.com/ADLINDevops/sdet-portfolio/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Playwright](https://img.shields.io/badge/Playwright-latest-green)
![Tests](https://img.shields.io/badge/Tests-16%20passing-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

A production-grade test automation portfolio built to demonstrate SDET skills across **UI automation**, **REST API testing**, **security checks**, and **CI/CD integration** — all running on GitHub Actions.

---

## 🚀 What This Project Covers

| Layer | Tool | Target | Tests |
|---|---|---|---|
| UI Automation | Playwright + POM | books.toscrape.com | 8 |
| API Automation | Python requests + Pydantic | JSONPlaceholder API | 5 |
| Security Testing | OWASP Top 10 checks | books.toscrape.com | 3 |
| **Total** | | | **16 ✅** |

---
Screenshot of Actions:
<img width="1326" height="332" alt="image" src="https://github.com/user-attachments/assets/b8575e41-85e7-40b4-b73b-853dbfb150e1" />


## 🛠 Tech Stack

- **Language:** Python 3.11
- **UI Automation:** Playwright (Page Object Model)
- **API Testing:** Python `requests` + Pydantic schema validation
- **Security:** OWASP Top 10 based checks
- **Test Runner:** pytest
- **CI/CD:** GitHub Actions (runs on every push)
- **Containerisation:** Docker

---

## 📁 Project Structure

```
sdet-portfolio/
│
├── tests/
│   ├── ui/               # Playwright UI tests (POM)
│   ├── api/              # REST API tests with schema validation
│   └── security/         # OWASP-based security checks
│
├── pages/                # Page Object Model classes
├── .github/workflows/    # GitHub Actions CI pipeline
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## ✅ CI/CD Pipeline

Every push triggers the full test suite automatically on GitHub Actions.

```yaml
# .github/workflows/ci.yml
- Installs dependencies
- Installs Playwright browsers
- Runs all 16 tests via pytest
- Reports pass/fail status
```

➡ **All 16 tests currently passing** — see the badge above.

---

## 🖥 UI Tests — Playwright + Page Object Model

Tests written against [books.toscrape.com](http://books.toscrape.com) using POM pattern.

**What's tested:**
- Homepage loads and title is correct
- Book catalogue renders with expected items
- Filtering by category works correctly
- Book detail page shows price and availability
- Pagination navigates correctly
- Add to basket interaction works
- Search and navigation flows

**Run UI tests:**
```bash
pytest tests/ui/ -v
```

---

## 🔌 API Tests — REST Automation + Schema Validation

Tests written against [JSONPlaceholder](https://jsonplaceholder.typicode.com) using Python `requests` and **Pydantic** for response schema validation.

**What's tested:**
- GET /posts returns correct schema
- POST /posts creates resource and returns 201
- PUT /posts/:id updates resource correctly
- DELETE /posts/:id returns 200
- Schema validation catches missing/wrong field types

**Run API tests:**
```bash
pytest tests/api/ -v
```

---

## 🔒 Security Tests — OWASP Top 10

Basic OWASP-based security checks integrated as a dedicated test layer.

**Checks included:**
- SQL injection attempt detection
- XSS payload response handling
- Sensitive data exposure in response headers

**Run security tests:**
```bash
pytest tests/security/ -v
```

---

## ⚡ Run All Tests Locally

```bash
# 1. Clone the repo
git clone https://github.com/ADLINDevops/sdet-portfolio.git
cd sdet-portfolio

# 2. Create virtual environment
python -m venv venv
.\venv\Scripts\activate        # Windows PowerShell

# 3. Install dependencies
pip install -r requirements.txt
playwright install

# 4. Run all 16 tests
pytest --tb=short -v
```

---

## 📊 Test Results (Latest CI Run)

```
tests/ui/test_homepage.py          PASSED
tests/ui/test_catalogue.py         PASSED
tests/ui/test_book_detail.py       PASSED
tests/ui/test_pagination.py        PASSED
tests/ui/test_category_filter.py   PASSED
tests/ui/test_navigation.py        PASSED
tests/ui/test_basket.py            PASSED
tests/ui/test_search.py            PASSED
tests/api/test_get_posts.py        PASSED
tests/api/test_create_post.py      PASSED
tests/api/test_update_post.py      PASSED
tests/api/test_delete_post.py      PASSED
tests/api/test_schema_validation.py PASSED
tests/security/test_sqli.py        PASSED
tests/security/test_xss.py         PASSED
tests/security/test_headers.py     PASSED

========= 16 passed in 28.4s =========
```

---

## 👤 About

**Adlin Xavier** — Senior SDET with 11+ years in QA across Insurance and Life Sciences domains.  
Currently transitioning into full SDET / AI-integrated testing roles.

🔗 [LinkedIn](https://www.linkedin.com/in/adlinxavier-072191196) | 💻 [GitHub](https://github.com/ADLINDevops)
