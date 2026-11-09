---
title: Export and the family snapshot
summary: A spreadsheet of your transactions, and a read-only picture for family.
order: 30
---

# Export and the family snapshot

Two ways to hand your numbers to others: a spreadsheet of every transaction, and a read-only picture of today's numbers for a family member. Both files are made on the phone — no server is involved — and you pass them on yourself.

## When to use it

- You want your transactions in a spreadsheet, for your own sorting or for an accountant.
- Someone in your household — a partner, a grown-up child — wants to see where the money stands, without running the books.
- You are moving out of the app and want a copy of the raw data (for a complete copy, encrypted, see [Backup and restore](/guide/data/backup-and-restore/)).

Everything is in Settings. Open Today, tap the gear at the top right, then **Backup and your data**.

## Step by step

### Export your transactions as a spreadsheet

1. Open Settings, then **Backup and your data**.
2. In the **Backup** section, find **Export transactions**. Choose **All**, or a single year.
3. Tap **Make a CSV file**.
4. When it says the file is ready, tap the share button that appears. Save the file to Files, or send it to your Mac.

The file is ordinary CSV with one row per transaction, oldest first. Each row has the date, the type (`Spent`, `Received`, `Transfer`, `Adjustment` or `Opening balance`), the payee, the category and the account. It also has a second account column for transfers, the amount with its currency, any note, and where the record came from. Money spent is negative and money received positive. A transfer between your own accounts shows both accounts and is not counted as spending.

> **Tip:** Pick a single year if you only need part of the history. Choose **All** to get everything.

### Make a snapshot for family

1. Open Settings, then **Backup and your data**, then the **Family** section.
2. Tap **Make a snapshot for family**.
3. Type a passphrase of at least 6 characters and tap **Create**. You will give this phrase to the person who opens the file.
4. When the snapshot is ready, use the share button to send the file to them — Messages, Mail, AirDrop, whatever you already use.

### How they open it

They open the file on a phone that has Damla installed. On the first welcome screen they tap **Open a family snapshot**; once a snapshot is already open, the button is called **Open a newer snapshot**. They pick the file, type the passphrase you told them, and tap **Open**.

What they see is a read-only screen titled **Family view**. A note on it says when the picture was made and which day it is a picture of ("as of …"). On the screen:

- **Safe to spend**, with a headline such as the day of the next income, or a warning that money may run short.
- **Balance** today, **Lowest point ahead**, and **Minimum kept**.
- A small chart under **Next 90 days**, showing the balance over the coming days.
- **Next to leave**: the payments coming up.
- **Accounts**: each account with its balance (a card shows what is owed on it).

They can open a newer snapshot when you send one, and tap **Stop viewing** to close it.

## Good to know

- The snapshot is a picture of one moment. It does not update by itself; send a fresh one when the numbers change.
- It is encrypted with the passphrase, and it is read-only: the other person can look but cannot change anything, and their phone does not receive your books.
- The snapshot is much smaller than a backup: it holds today's numbers and the 90-day picture, not your whole history and not your backups.
- Passphrase lengths differ: at least 6 characters for a snapshot, at least 8 for an encrypted backup.

> **Note:** Exporting a CSV, and making and opening snapshots, work even when a trial or subscription has ended, because they are read-only actions.

## Related

- [Backup and restore](/guide/data/backup-and-restore/)
- [Settings, page by page](/guide/data/settings-map/)
- [Privacy and your data](/guide/data/privacy-and-your-data/)
