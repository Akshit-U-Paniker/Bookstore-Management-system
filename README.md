# Bookstore Management System

A robust, console-based application built in Python designed to streamline retail bookstore operations. The system simplifies catalog management, stock replenishment, book searching, customer purchase workflows, and instant invoice generation.

\---

## Overview of the Project

The **Bookstore Management System** replaces physical ledgers and fragmented spreadsheets with a centralized, terminal-driven solution. Built with Python and formatted using `PrettyTable`, it offers real-time inventory tracking, multi-criteria catalog search, safe inventory deduction logic, and detailed billing statements.

\---

## Features

* **Admin Panel**:

  * **Insert New Book**: Add books with Title, Author, Publisher, Year, Price, and Stock.
  * **Display Inventory**: View all book records in structured, bordered ASCII tables.
  * **Multi-Parametric Search**: Find books by Title, Book ID, Publisher, Publication Year, Year Range, or Author.
  * **Update Records**: Edit specific fields of an existing book in-place.
  * **Delete Books**: Remove obsolete book listings permanently from the catalog.
* **Purchase Processing**:

  * Multi-item customer cart handling.
  * Real-time stock verification with out-of-stock prompts.
  * Automatic deduction of purchased quantities from active stock.
* **Invoice \& Billing**:

  * Auto-generates unique Order IDs.
  * Formatted invoices displaying customer credentials, purchased line items, quantities, sub-totals, and total payable amounts.

\---

## Technologies \& Tools Used

* **Language**: Python 3.x
* **Libraries**: `prettytable` (for tabular terminal output)
* **Data Structures**: In-memory nested Dictionaries and Lists

\---

## Steps to Install \& Run the Project

### Prerequisites

* Python 3.8 or higher installed on your machine.
* `pip` package manager.

### 1\. Clone the Repository

```bash
git clone https://github.com/Akshit-U-Paniker/Bookstore-Management-system.git
cd bookstore-management-system
```

### 2\. Install Required Dependencies

Install the `prettytable` package using pip:

```bash
pip install prettytable
```

### 3\. Run the Application

Execute the Python script:

```bash
python bookstore\\\_management.py
```

\---

## Instructions for Testing

1. **Admin Panel Verification**:

   * Choose option `1` from the main menu.
   * Select `2` to display all initialized books and confirm table formatting.
   * Select `1` to add a test book, then display all books again to ensure the new entry appears.
   * Select `3` to perform searches across various parameters (e.g., search by author name or publication year range).
   * Select `4` and `5` to update and delete test records, ensuring data updates in-memory.
2. **Purchase Workflow Verification**:

   * Choose option `2` from the main menu.
   * Enter customer details (Name, Address, Phone, Email).
   * Input a valid Book ID and request a quantity within stock limits.
   * Input a quantity exceeding available stock to confirm the stock limit warning prompt triggers.
3. **Invoice Generation Verification**:

   * Choose option `3` from the main menu.
   * View the displayed list of completed Order IDs.
   * Enter your Order ID to verify that customer details, line items, and total payable amounts calculate accurately.

\---

