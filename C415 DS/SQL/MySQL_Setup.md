# MySQL Installation and Setup on Windows
## Complete Step-by-Step Guide

**Operating System:** Windows 10 / Windows 11  
**Database:** MySQL Community Server  
**Installation Type:** MSI Installer  
**Cost:** Free (Community Edition)

---

# 1. Requirements

Before installing MySQL, make sure you have:

- Windows 10 or Windows 11 (64-bit).
- Administrator access to your computer.
- Internet connection.
- At least 2 GB of free disk space.
- Microsoft Visual C++ Redistributable if required by your MySQL version.

# 2. Download MySQL Server

Download MySQL from the official website:

https://dev.mysql.com/downloads/mysql/

### Steps

1. Open the official MySQL download page.
2. Select MySQL Community Server.
3. Select Windows as your operating system.
4. Select the Windows 64-bit MSI Installer.
5. Click Download.
6. Save the downloaded `.msi` file.

**Official download:**

https://dev.mysql.com/downloads/mysql/

**Screenshot 1:** MySQL Community Server download page.
![MySQL download reference](https://dev.mysql.com/common/logos/mysql-logo.svg)


# 3. Install MySQL Server

1. Open your Downloads folder.
2. Double-click the downloaded MSI file.
3. Allow Windows to make changes if prompted.
4. Follow the installation wizard.
5. Complete the installation.

**Screenshot 2:** Windows MySQL installation wizard.

# 4. Configure MySQL Server

After installation, open MySQL Configurator.

Use these settings where available:

| Setting | Value |
|---|---|
| Server Type | Development Computer |
| TCP/IP | Enabled |
| Port | 3306 |
| Authentication | Strong Password Encryption |
| Windows Service | Enabled |
| Start at System Startup | Enabled |

Click Next to continue.

**Screenshot 3:** MySQL Configurator networking settings.

# 5. Create Root Password

During configuration:

1. Select the root account.
2. Enter a strong password.
3. Confirm the password.
4. Save the password securely.

Example username:

`root`

Example password format:

`YourStrongPassword123!`

Do not use the example password as your actual password.

Click Next and apply the configuration.

**Screenshot 4:** MySQL root account configuration.

# 6. Install MySQL Workbench

MySQL Workbench provides a graphical interface to write and execute SQL queries.

Official download:

https://dev.mysql.com/downloads/workbench/

### Installation steps

1. Open the official Workbench download page.
2. Select Windows.
3. Download the MSI installer.
4. Run the installer.
5. Follow the installation instructions.
6. Open MySQL Workbench.

Note: Check the Workbench release compatibility with your installed MySQL Server version.

**Screenshot 5:** MySQL Workbench download page.

# 7. Connect to MySQL Server

1. Open MySQL Workbench.
2. Find MySQL Connections.
3. Click the plus (+) icon if you need to create a connection.
4. Enter the following details:

| Field | Value |
|---|---|
| Connection Name | Local MySQL |
| Hostname | 127.0.0.1 |
| Port | 3306 |
| Username | root |
| Password | Your MySQL root password |

5. Click Test Connection.
6. Enter your password if prompted.
7. Click OK after a successful connection.

**Screenshot 6:** MySQL Workbench connection setup.

# 8. Create Your First Database

Open a new SQL query tab.

Execute:

```sql
CREATE DATABASE college;

USE college;
```

This creates a database named college.

# 9. Create Your First Table

Execute the following SQL:

```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(50)
);
```

This creates a students table.

# 10. Insert Data into the Table

Execute:

```sql
INSERT INTO students
(id, name, age, course)
VALUES
(1, 'Rahul', 21, 'BCA'),
(2, 'Priya', 22, 'BTech'),
(3, 'Amit', 20, 'BCA');
```

# 11. Display the Records

Execute:

```sql
SELECT * FROM students;
```

Expected output:

| id | name | age | course |
|---|---|---|---|
| 1 | Rahul | 21 | BCA |
| 2 | Priya | 22 | BTech |
| 3 | Amit | 20 | BCA |

**Screenshot 7:** SQL query editor and output table.

# 12. Test MySQL Using Command Prompt

You can also test MySQL through Windows Command Prompt.

Open CMD and enter:

```bash
mysql --version
```

If MySQL is added to PATH, this displays the installed version.

To connect:

```bash
mysql -u root -p
```

Enter your root password.

To check the databases:

```sql
SHOW DATABASES;
```

# 13. Common Problems and Solutions

### Problem 1: Port 3306 Already in Use

Solution:
- Check whether another MySQL service is running.
- Open Windows Services.
- Check the MySQL service.
- Resolve any port conflict before changing configuration.

### Problem 2: Access Denied for User root

Solution:
- Verify your username.
- Check your password.
- Make sure you are connecting to the correct server.

### Problem 3: MySQL Server Is Not Running

Solution:
1. Press Windows + R.
2. Type `services.msc`.
3. Press Enter.
4. Find the MySQL service.
5. Right-click and select Start.

### Problem 4: mysql Is Not Recognized

Solution:
- Add the MySQL Server `bin` folder to Windows PATH.
- Open a new Command Prompt.
- Run `mysql --version` again.

# 14. Important Official Links

| Resource | Official Link |
|---|---|
| MySQL Community Server | https://dev.mysql.com/downloads/mysql/ |
| MySQL Installer | https://dev.mysql.com/downloads/installer/ |
| MySQL Workbench | https://dev.mysql.com/downloads/workbench/ |
| MySQL Documentation | https://dev.mysql.com/doc/ |
| MySQL Windows Installation Guide | https://dev.mysql.com/doc/refman/26.7/en/windows-installation.html |
| MySQL Workbench Manual | https://dev.mysql.com/doc/workbench/en/ |

# 15. Final Checklist

- [ ] MySQL Server installed.
- [ ] MySQL Server configured.
- [ ] Root password created.
- [ ] MySQL Workbench installed.
- [ ] Localhost connection successful.
- [ ] Database created.
- [ ] Students table created.
- [ ] Records inserted successfully.
- [ ] SELECT query executed successfully.

---

## Congratulations!

MySQL is now installed and configured on your Windows computer.

You are ready to start learning SQL and practicing database queries.
