---
title: Privacy and your data
summary: What stays on the phone, what is looked up online, and what is never sent.
order: 40
---

# Privacy and your data

Your books stay on your phone. The reading of your words happens on the phone. The few things that go online carry nothing about you. This page says what stays, what goes, and what never leaves.

## When to read this

- You want to know where your balances and transactions are stored before you trust the app with them.
- You want to know what, if anything, is sent over the internet.
- You are setting Damla up for someone who cares about privacy, and want the short version.

## What stays on the phone

- Your accounts, balances, transactions, notes and plans are stored only on this phone. There is no server they sit on.
- There is no account, no sign-in, no server, no advertising and no analytics. Damla declares to Apple that it does not track anyone, and lists no tracking domains.
- When you back up, the file is encrypted with a passphrase only you know, and you choose where it is saved — a folder in iCloud Drive, if you like, or anywhere else in Files.
- Passwords Damla keeps for locked statement PDFs stay in this phone's Keychain. They never leave the phone and are not in backups.
- Reminders about bills and about your balance dipping below your minimum are worked out on this phone, from your own data.
- A bank alert that arrives while the phone is locked waits on the phone and is added the next time you open and unlock the app.

## The lock

Damla locks with Face ID, or your passcode, when you leave it. In Settings under **Basics**, **Ask for Face ID**, you choose how soon it asks again: every time, or after 1, 5 or 15 minutes away. The automations you set up in the Shortcuts app do not need the lock.

## Reading your words, on the phone

Damla understands plain sentences — "school fees on the card, later paid in instalments" — so you do not have to fill in forms. The understanding is done by the language model built into your iPhone where it supports Apple Intelligence, and by a simple reader built into Damla where it does not. In both cases the work runs on the phone: nothing you type is sent anywhere. The maths — balances, forecasts, instalments — is done by ordinary code, and that never leaves the phone either.

## What is looked up online, and what it sends

Three look-ups exist. None is required, and the app works fully offline. Exchange-rate refresh is on by default and you can switch it off; the price lookup and the logo search happen only if you turn them on or tap them. The app's privacy declaration to Apple lists these three as the only data that ever leaves the phone.

| Look-up | What it sends | When |
| --- | --- | --- |
| Exchange rates | Currency codes only, for example "AED", "USD" | About once a day, if you leave **Update exchange rates daily** on, or when you tap **Refresh now** |
| Prices for holdings | The ticker symbols of holdings you choose to track, for example "AAPL" | Only if you turn on **Look up prices for holdings** — it is off by default |
| Find logo online | The bank name you typed | Only when you tap the button, for a bank missing from the built-in catalog |

The rates and prices come back with an as-of date, and the last one is shown in Settings under **Currencies and prices**, so you can always see where each number came from. You can also type your own rate or price, and a value you type wins on the day you enter it.

> **Note:** No amounts, account names, dates, notes or personal details are ever part of a look-up. Damla never connects to your bank, and nothing carries an account, device or advertising identifier, or is linked to you.

## What is never sent anywhere

- Balances and transactions.
- Anything you type: sentences, notes, and the questions you ask Damla.
- Bank messages and statement files. iOS gives apps no access to your messages; they reach Damla only through a Shortcut you set up, the share sheet or the file picker, and they are read on the phone.
- One-time codes that appear in messages. The code is never kept — it reaches neither the books nor the Inbox — and the log of recent alerts records only that a code was skipped, never the message.
- The content of a family snapshot shared with someone: the file is encrypted with a passphrase, and you pass it on yourself.

## Taking your data out

You are not locked in. In Settings, **Backup and your data**, you can export a CSV spreadsheet of all transactions, make an encrypted backup sealed with a passphrase that only you know, and make a read-only snapshot for family. And **Delete all data** erases everything on this phone at once.

> **Careful:** Damla shows estimates from the numbers you give it. It gives information, not financial, tax or investment advice.

## Related

- [Backup and restore](/guide/data/backup-and-restore/)
- [Export and the family snapshot](/guide/data/export-and-family-snapshot/)
- [Prices and exchange rates](/guide/holdings/prices-and-exchange-rates/)
- [Logos and account details](/guide/accounts/logos-and-account-details/)
