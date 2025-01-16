# Intro to SQL and DBMS

Contains all instructions pertaining to SQL commands, syntax and tools for Part 1 of the course IE0015. Includes specific examples, code, and cheatsheets for the dbms [SQLite](https://www.sqlite.org). You can find a cheatsheet of import commands in SQL and for the SQLite client (sqlite3) at the top of [this file](cheatsheet.sql).

## SQLite Installation
macOS:
```
brew install sqlite
```

Windows:
```
winget install SQLite.SQLite
```

Linux (debian):
```
sudo apt install sqlite
```

## SQLite Usage
You can either use SQLite entirely in the command-line or with a GUI client, or a mixture of both. I would recommend mixing a bit of both - taking this extra step will make you much more comfortable with databases.

### CLI
You can verify that your installation was completed correctly as follows:
```
sqlite3 -version
```

Your output should be something like this:
```
3.45.3 2024-04-15 13:34:05 8653b758870e6ef0c98d46b3ace27849054af85da891eb121e9aaa537f1e8355 (64-bit)
```

sqlite3 is not the database engine - it is a DBMS client that comes with SQLite - so it was installed when you installed SQLite previously. sqlite3 works with a command prompt: just spin it up and try some commands from the [cheatsheet](cheatsheet.sql):
```
sqlite3
```

All sqlite3 commands are the ones that start with a dot, for example:
```
sqlite3> .open ~/airbnb/airbnb.db
```

Notice the prompt `sqlite3>` that shows that you are in the DBMS client shell. Though the command line may seem unfriendly at first - you may appreciate its elegance - you can just type in SQL commands (even for big complex operations) all in the same prompt, just end your commands with a semicolon, for example:

```
sqlite3> .open ~/airbnb/airbnb.db
sqlite3> CREATE TABLE listings;
```

### GUI
[DB4S](https://sqlitebrowser.org) (DB Browser For SQLite) is a GUI browser to access and manage databases in SQLite. It works the same way as the command line but it can be more intuitive and more similar to excel and spreadsheets for viewing the tables. My recommendation is to install it and use it to double-check your database after operations, or even to try and repeat some operations in the command line and then in DB4S for reinforce it. Eventually, you can choose whichever client works best for you, which may be a mixture a both! For example, I use the command line, but I will keep DB4S installed for debugging and troubleshooting in the data.

DB4S is available for windows and mac, installation instructions are on their website.
