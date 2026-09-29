# Project Statement: Bookstore Management System

---

## 1. Problem Statement

Traditional retail bookstores frequently struggle with manual record-keeping using paper ledgers or fragmented spreadsheets. These legacy workflows lead to:

* Inaccurate inventory tracking and frequent discrepancies between recorded and physical stock.


* Sluggish, inefficient catalog browsing and book search capabilities across expanding collections.


* Vulnerability to manual calculation mistakes during multi-item customer purchases.


* A lack of structured, automated invoicing and transaction receipts at the time of sale.



There is a distinct requirement for a centralized, lightweight, and responsive software solution to manage inventory cataloging, sales processing, and billing calculations accurately.

---

## 2. Scope of the Project

The scope of this project encompasses building a standalone terminal/command-line interface (CLI) application in Python 3 for single-store retail bookshops.

### In Scope:

* Managing an in-memory catalog containing book details (Title, Author, Publisher, Publication Year, Price, Stock).


* Performing full catalog CRUD operations (Create, Read, Update, Delete) via an administrative interface.


* Providing multi-criteria search capabilities across book metadata attributes.


* Managing customer order sessions, handling cart additions, and enforcing stock availability boundaries in real time.


* Automated invoice generation with itemized costs, order identification, and payable sums using ASCII tables (`PrettyTable`).



### Out of Scope:

* Persistent cloud/relational database storage (data operates transiently during runtime execution).


* Integrated online payment gateway processing or external merchant APIs.


* Multi-branch inventory tracking or network-synchronized user accounts.



---

## 3. Target Users

* **Bookstore Administrators / Managers**: Store staff responsible for tracking catalog additions, updating book prices, adjusting physical stock levels, and pruning discontinued titles.


* **Cashiers / Store Clerks**: Front-desk operators processing customer purchases, entering customer contact credentials, verifying available copies, and printing itemized invoices.


* **Walk-In Customers (Indirect Beneficiaries)**: Buyers who receive structured billing breakdowns and quick catalog checks on book availability.



---

## 4. High-Level Features

* **Administrative Catalog Control (CRUD)**:
* Insertion of newly stocked book items with automatic Book ID incrementing.


* Tabular display of the complete store catalog with single-border ASCII styling.


* Granular field-level record updates (Title, Author, Publisher, Year, Price, Stock).


* Direct deletion of book listings by unique Book ID.




* **Multi-Parametric Search Engine**:
* Case-insensitive substring matching for Book Titles and Publishers.


* Exact matching by unique Book ID, Author name, and Publication Year.


* Range-based numeric filtering across publication years (e.g., books published between 1950 and 2000).




* **Order & Inventory Transaction Manager**:
* Real-time stock guard logic that alerts clerks when requested order units exceed in-stock levels.


* Automatic deduction of purchased quantities from the active catalog upon sale completion.


* Multi-item purchasing per customer transaction session.




* **Tabular Invoicing & Billing Engine**:
* Sequential auto-generation of unique Order IDs.


* Production of itemized purchase bills detailing customer information, purchased titles, unit prices, ordered quantities, line totals, and grand payable amounts.