# Bidirectional-Data-Ingestion-Tool
Author: Ayantika Nandi
Role: Software Engineer Intern Applicant
Submission Date: 16th April 2025

📘 Project Overview
This project implements a web-based data ingestion tool that allows bidirectional data transfer between a ClickHouse database and Flat Files (CSV). It provides an intuitive interface to select source/target, configure connections, select specific columns, and monitor the ingestion process.

✨ Features
🔄 Bidirectional Data Flow:

ClickHouse ➡️ Flat File

Flat File ➡️ ClickHouse

🔐 JWT-Based Authentication for ClickHouse

📋 Schema Discovery & Column Selection

⚙️ Efficient ingestion with batching support

📊 Real-time record count & status display

❌ Friendly error handling & user feedback

🛠️ Tech Stack

Component	Tech Used
Backend	Java (Spring Boot)
Frontend	HTML, CSS, JavaScript
DB	ClickHouse (via JDBC)
File I/O	OpenCSV / Java I/O
Auth	JWT Token Handling
Build Tool	Maven
🧪 Testing Scenarios

Test Case #	Scenario	Expected Result
✅ TC-1	ClickHouse table ➝ Flat File (CSV)	CSV created with selected columns & count shown
✅ TC-2	Flat File ➝ ClickHouse table creation	New table with uploaded data
✅ TC-3	Multi-table JOIN in ClickHouse ➝ Flat File	Joined output in CSV
✅ TC-4	Invalid JWT Token / Connection	User-friendly error
✅ TC-5	Data Preview (first 100 rows before ingestion)	Preview table rendered in UI
📦 How to Run
🔧 Prerequisites
Java 11+

Maven

ClickHouse running (local/docker)

CSV files for ingestion testing

📥 Clone the Repo
bash
Copy
Edit
git clone https://github.com/ayantikanandi/zeotap-assignment.git
cd zeotap-assignment/assignment-clickhouse-flatfile
⚙️ Build the Application
bash
Copy
Edit
mvn clean install
▶️ Run
bash
Copy
Edit
java -jar target/bidirectional-data-ingestion-tool.jar
🌐 Access UI
Open your browser and visit:
http://localhost:8080

🖥️ UI Highlights
Source & Target Dropdown (ClickHouse / Flat File)

ClickHouse Config Panel (Host, Port, DB, JWT Token, etc.)

Column Checkboxes

Preview Button

Start Ingestion Button

Record Count / Error Message Display

🔐 JWT Handling
JWT is passed directly via header in ClickHouse client connection

JWT validation handled via secure ClickHouse config
