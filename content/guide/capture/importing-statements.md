---
title: Importing a statement
summary: PDF or CSV statements, checked against your balances.
order: 50
---

# Importing a statement

Importing a bank or card statement brings its transactions into your books in one go, checked against the balances the statement itself reports. Use it to start Damla with history, to catch up after a gap, or to make your books agree with the bank.

## When to use it

- You are setting up and want several months of history added at once.
- Bank alerts missed some days, for example on a card or account you started using mid-month.
- You want to check your books against the bank: every transaction counted once, and the balances matching.

## Step by step

1. Open Accounts, tap the plus button, then Import statements.
2. Choose the statement files (PDF or CSV). You can import several accounts and months together.
3. For each file, check what Damla set up: the account name, whether it is a Bank account or a Credit card, and the currency.
4. Turn on "Charges are printed as positive numbers" if the card prints its charges without a minus, and "Dates are month/day (US style)" if your dates are written that way.
5. Review what Damla found for each file: how many rows, whether it matches an account you already have, and the balance after the last row.
6. If a statement does not state a balance, enter what that account holds (or owes, for a card) today, so the starting point can be worked out.
7. Answer each unknown payee once: choose a category, mark it as one of your own accounts, or skip it. Every matching row follows your answer, and next time the payee is remembered.
8. Tap Import. Rows already recorded are skipped, so nothing is counted twice, and repeated rows from overlapping files are counted once.

> **Tip:** Open the rows skipped line on the review screen to see what each one was taken to be.

A row that came in earlier as a bank alert counts as the same transaction when the amounts are the same, the shop names fit, and the dates are up to three days apart. Banks post a few days later than they charge.

## Good to know

- **Everything is read on the phone. The statement is never uploaded** anywhere: there is no account and no server.
- **Locked PDFs ask for the password once.** Many banks lock their statements. Damla asks for the password, and can keep it in this phone's Keychain so the next statement from the same bank opens by itself. Nothing is synced, and you can forget saved passwords in Settings.
- **Debit and Credit columns are read by position.** When a statement prints a Debit and a Credit column, a refund and a purchase of the same amount look the same as plain text. Damla therefore reads where each number sat on the page, under its column heading, before deciding the sign.
- **Where the iPhone has Apple Intelligence, and a card statement's summary box is written in a way the rules cannot read**, the on-device model reads only that summary box — not the transaction rows and not the whole file, and nothing leaves the phone. Damla accepts nothing on the model's word: code checks that every figure it returned is printed in the statement, and that the summary's own arithmetic closes, before the figures are used. Any figure that fails a check is dropped, not fixed. Nothing is added until you confirm the import. On phones without Apple Intelligence, the transaction rows are still read; if the statement's balances are missing, Damla asks you for today's figure instead.

## What happens at the end

- If every row is already in your books, the button reads Reconcile to the statement and still makes the balances agree exactly.
- If you did not record some of the money one by one, it is filled in from the statement. Earlier reconciliation adjustments inside that period are replaced. At most two clearly labelled adjustments are added: the balance brought forward and anything still missing at the end. Both are reconciliation lines, not spending, and afterwards your books match the statement's opening and closing balances. If the statement does not state a closing balance, nothing is reconciled.
- **Rows that say which payment of how many they are** (instalment markers on a card statement) are listed under Instalments found, and nothing is added until you confirm. They go under the Instalments category, not as spending. The payments still to come are added to your instalment plans on the card's later due dates.
- Purchases in another currency are updated to the amount the bank really billed.

## Related

- [Screenshots of your bank app](/guide/capture/screenshots-of-your-bank-app/)
- [Starting balances and adjustments](/guide/accounts/starting-balances/)
- [Payees and categories](/guide/planning/payees-and-categories/)
- [Bank texts and emails](/guide/capture/bank-texts-and-emails/)
