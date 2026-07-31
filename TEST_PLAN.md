# Test Plan: Django Shopping Cart Application

## 1. Scope

This test plan covers the Django Shopping Cart application located in this repository. The application allows users to browse grocery products, manage categories, stores, products, and prices, compare prices across stores, and manage a shopping cart.

Testing will cover functional behavior, validation rules, user workflows, database interactions, UI behavior, and regression coverage for the current Django app and its existing pytest-based automation.

In scope:

- Homepage dashboard and navigation.
- User authentication pages and access control for cart actions.
- Category create, read, update, and delete workflows.
- Product create, read, update, and delete workflows.
- Store create, read, update, and delete workflows.
- Price creation, update, deletion, duplicate validation, and price comparison.
- Dynamic product loading by category.
- Shopping cart add, view, update quantity, and remove item workflows.
- Form validation, model constraints, and expected redirects.
- Template rendering and basic responsive UI checks.
- SQLite-backed local development and test execution.
- Existing pytest and browser automation coverage in the `tests/` directory.

Out of scope:

- Payment processing, checkout, order fulfillment, shipping, tax, and inventory reservation because they are not implemented.
- Production infrastructure, deployment pipelines, autoscaling, backups, and monitoring.
- Third-party live retailer price accuracy beyond scraper integration boundaries.
- Native mobile applications.
- Full accessibility certification or formal WCAG audit, though basic usability and keyboard checks should be included.
- Full performance/load testing at production traffic levels.

## 2. Test Objectives

- Verify that users can complete the main shopping workflows without errors.
- Confirm that Django models, views, forms, templates, and URLs work together correctly.
- Validate that product, category, store, and price data is created, displayed, updated, and deleted correctly.
- Confirm shopping cart actions are limited to authenticated users and isolated per user.
- Ensure duplicate product and duplicate product-store price combinations are handled correctly.
- Verify price comparison identifies and displays the cheapest store and price per product.
- Confirm form validation handles invalid, missing, duplicate, and boundary inputs.
- Detect regressions in existing automated browser tests.
- Ensure test data can be created, reset, and reused consistently.
- Provide enough coverage to support future refactoring and feature additions.

## 3. Features To Test

### 3.1 Homepage And Navigation

- Homepage loads successfully at `/`.
- Product, store, and category counts display correctly.
- Category links navigate to category-specific product pages.
- Navigation links route to product list, store list, category list, price comparison, login, logout, and cart pages as applicable.
- Empty-state behavior is clear when no categories, products, stores, or prices exist.

### 3.2 Authentication And Access Control

- Login page renders correctly.
- Valid users can log in.
- Logged-in users can log out and return to the configured page.
- Anonymous users are redirected when accessing protected cart actions.
- Cart contents are tied to the authenticated user.
- One user cannot update or remove another user's cart items.
- Register page renders correctly.

### 3.3 Category Management

- Category list displays all categories.
- Category creation succeeds with a valid unique name.
- Category creation supports optional image upload.
- Duplicate category names are rejected by the model/database constraint.
- Category edit updates name and image.
- Category delete removes the category and handles related products according to model behavior.
- Category product page shows only products belonging to the selected category.
- Invalid category IDs return the expected error response.

### 3.4 Product Management

- Product list displays all products.
- Product creation succeeds with valid category, name, quantity, unit, and optional image.
- Product names are unique case-insensitively through form validation.
- Product edit updates category, name, quantity, unit, and image.
- Product delete removes the product and related dependent data according to model behavior.
- Product quantity accepts valid decimals within model precision.
- Product quantity rejects invalid numeric values.
- Product unit selection only allows supported units: `kg`, `g`, `l`, `ml`, and `pcs`.
- Product string representation includes name, quantity, and unit.

### 3.5 Store Management

- Store list displays all stores.
- Store creation succeeds with valid name and optional location, logo, address, and website.
- Store names are unique.
- Store edit updates all editable fields.
- Store delete removes the store and related prices according to model behavior.
- Website field accepts valid URLs and rejects invalid URLs.
- Missing optional fields do not block store creation.

### 3.6 Price Management

- Price creation succeeds for an existing product and store.
- Price creation can create a new product from `product_name` when no matching product exists.
- Price creation associates the new product with the selected category.
- Duplicate price entries for the same product and store are rejected.
- Price edit prepopulates category and product name from the existing price.
- Price edit updates store and price correctly.
- Price delete removes the price record.
- Price field accepts valid decimal values within model precision.
- Price field rejects blank, non-numeric, negative if business rules require it, and over-precision values.
- Success messages display after successful price creation.

### 3.7 Price Comparison

- Price comparison page loads at `/compare/`.
- Stores appear as comparison columns or headings.
- Products appear with their available store prices.
- Missing prices are displayed clearly.
- Cheapest price and cheapest store are calculated correctly.
- Products with no prices do not break the comparison page.
- Multiple stores with the same price are handled consistently.
- Edit and delete links for prices route to the correct price record.

### 3.8 Dynamic Product Loading

- `load-products/` returns products filtered by category.
- Returned products are ordered by name.
- Empty categories return an empty dropdown/list state.
- Missing or invalid category query parameters are handled gracefully.
- The price form product selector/search behavior works with the returned partial template.

### 3.9 Shopping Cart

- Authenticated users can add a product to the cart.
- Adding a product creates a cart if the user does not already have one.
- Adding the same product again increments the cart item quantity.
- Cart page displays all items for the current user.
- Updating quantity to a positive integer changes the cart item quantity.
- Updating quantity to zero or a negative number removes the item.
- Invalid quantity input does not change the item and shows an error message.
- Removing an item deletes it from the cart.
- Cart totals, item counts, and displayed quantities are correct where implemented in templates.
- Cart actions redirect to the expected pages.

### 3.10 Templates And UI

- All major templates render without missing context variables.
- Forms show field-level and non-field validation errors.
- Buttons, links, and forms use valid URLs.
- Uploaded product, category, and store images display when present.
- Layout is usable on desktop and mobile viewport widths.
- No obvious text overlap or broken navigation occurs on supported screen sizes.

### 3.11 Admin And Data Management

- Models can be managed through Django admin if registered.
- Migrations apply cleanly on a fresh database.
- Seed command creates usable sample data.
- Scrape products command can run in a controlled test mode or with mocked network responses.

### 3.12 Scraper Integration

- Scraper parsing logic handles expected HTML responses.
- Network failures, timeouts, malformed responses, and missing product data are handled safely.
- Scraped prices do not create duplicate invalid records.
- External HTTP calls are mocked in automated tests.

### 3.13 Automated Regression Tests

- Existing tests in `tests/` execute with `pytest`.
- Page Object Model classes under `tests/pages/` perform stable navigation and interactions.
- Browser tests cover homepage loading, product browsing, price editing, and cart behavior.
- HTML reports are generated in `reports/report.html`.
- Screenshots, traces, and logs are captured for failed browser scenarios where configured.

## 4. Features Not To Test

- Checkout, payments, refunds, and invoices.
- Real-time inventory sync.
- Email notifications.
- Production authentication hardening such as MFA, SSO, password reset email delivery, and account verification.
- Browser/device combinations outside the agreed support matrix.
- Production-scale load, stress, soak, and disaster recovery tests.
- Search engine optimization.
- Visual design approval beyond basic UI correctness.
- Accuracy of third-party store websites or third-party price data.
- Security penetration testing beyond basic access-control and validation checks.

## 5. Entry Criteria

Testing may begin when:

- Code for the target feature or release is merged or available in the test branch.
- Dependencies from `requirements.txt` are installed in a virtual environment.
- Database migrations apply successfully.
- Test database or local SQLite database can be created and reset.
- Required seed data or fixtures are available.
- Django development server can start successfully.
- Browser automation dependencies are installed if running Playwright/Selenium tests.
- Test environment variables and media directories are configured.
- Known blockers are documented before execution begins.

## 6. Exit Criteria

Testing may be considered complete when:

- All planned high-priority functional test cases have been executed.
- All critical and high-severity defects are fixed and retested.
- Medium-severity defects are fixed or explicitly accepted.
- Automated regression tests pass consistently.
- Database migrations pass from a clean state.
- No unresolved access-control defects remain for cart ownership or protected routes.
- Test evidence is available, such as pytest output, HTML report, screenshots, traces, or defect IDs.
- Product owner or project stakeholder accepts any remaining known issues.

## 7. Risks

- Current register view renders a page but may not persist new users unless additional registration handling exists elsewhere.
- Some CRUD views may not require login, which could allow unauthorized data changes if that is not intentional.
- Duplicate URL names for adding to cart could cause routing confusion.
- SQLite behavior may differ from a production database if the app later moves to PostgreSQL or MySQL.
- Image upload behavior depends on local media settings and file permissions.
- Browser automation can be flaky if selectors depend on visible text or test data that changes.
- Scraper tests may become unstable if they call live external websites.
- Price comparison logic may not handle ties or products without prices according to stakeholder expectations.
- Deleting categories, products, or stores cascades related data and could remove more records than users expect.
- Decimal validation for quantity and price may allow values that are technically valid but not business-valid.
- Test reports and traces may grow over time if not cleaned up.

## 8. Test Environment

### 8.1 Local Environment

- Operating system: Windows development workstation.
- Project path: `C:\Users\larai\OneDrive\Documents\Shoppingcart`.
- Python: Python 3 compatible with Django 6.
- Framework: Django 6.0.4.
- Database: SQLite using `db.sqlite3` for local development.
- Browser automation: pytest with page objects; Playwright/Selenium dependencies should be installed as required by the active test suite.
- Reports: pytest HTML report generated at `reports/report.html`.
- Media: local `media/` directory for uploaded category, product, and store images.

### 8.2 Setup Steps

1. Create and activate a virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:

   ```bash
   python manage.py migrate
   ```

4. Create seed data if needed:

   ```bash
   python manage.py seed
   ```

5. Start the Django development server:

   ```bash
   python manage.py runserver 8007
   ```

6. Run automated tests:

   ```bash
   pytest tests -v
   ```

7. Generate the HTML report:

   ```bash
   pytest tests --html=reports/report.html --self-contained-html
   ```

### 8.3 Test Data

- At least two user accounts to validate cart isolation.
- At least three categories, including one empty category.
- At least five products across multiple categories.
- At least three stores, with varied optional fields.
- Prices for the same product across multiple stores.
- Products with no prices.
- Duplicate product and duplicate product-store price scenarios.
- Valid and invalid image files for upload checks.
- Boundary values for quantity and price fields.

### 8.4 Supported Browsers And Viewports

- Chromium or default Playwright/Selenium browser for automated tests.
- Manual smoke checks in Chrome or Edge.


## 9. Test Deliverables

- This test plan.
- Manual test cases or checklist derived from the features listed above.
- Automated pytest tests and Page Object Model updates.
- Test execution report in `reports/report.html`.
- Defect reports with reproduction steps, expected result, actual result, severity, and evidence.
- Screenshots, traces, and logs for failed UI tests where available.

## 10. Test Execution Strategy

- Run unit and form-level tests first for fast feedback.
- Run view and URL tests next to validate Django routing, templates, redirects, and permissions.
- Run browser-based end-to-end tests for the most important user workflows.
- Mock network calls for scraper-related tests.
- Use isolated test data for each automated test to avoid order dependency.
- Re-run impacted tests after every defect fix.
- Run the full regression suite before release or submission.

