# Intro to SQL and DBMS

Contains all instructions pertaining to SQL commands, syntax and tools for Part 1 of the course IE0015. Includes specific examples, code, and cheatsheets for the dbms [sqlite](https://www.sqlite.org). You can find a cheatsheet of import commands in SQL and for the sqlite client (sqlite3) at the top of [this file](codealong.sql).

## sqlite Installation
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

## sqlite Usage
You can either use sqlite entirely in the command-line or with a GUI client, or a mixture of both. I would recommend mixing a bit of both - taking this extra step will make you much more comfortable with databases.

### CLI
You can verify that your installation was completed correctly as follows:
```
sqlite3 -version
```

Your output should be something like this:
```
3.45.3 2024-04-15 13:34:05 8653b758870e6ef0c98d46b3ace27849054af85da891eb121e9aaa537f1e8355 (64-bit)
```

sqlite3 is not the database engine - it is a DBMS client that comes with sqlite - so it was installed when you installed sqlite previously. sqlite3 works with a command prompt: just spin it up and try some commands from the [cheatsheet](codealong.sql):
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

