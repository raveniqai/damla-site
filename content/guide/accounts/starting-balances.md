---
title: Starting balances and adjustments
summary: How an account's opening figure works and how to correct it.
order: 60
---

# Starting balances and adjustments

A starting balance is the figure you enter for an account when you bring its books into Damla. It says where the account stood when you began, so nothing before that day has to be entered. An adjustment is an entry Damla writes to make your books agree with what your bank or a statement says. Both show as grey rows in Activity, with no plus or minus sign: they are neither income nor spending, so they never change what your reports say you earned or spent.

## When to use it

- You add a bank account, savings, wallet, card or loan and enter its balance today. If that figure is not zero, Damla records it as the account's starting balance.
- You import a statement and not all of the money was captured transaction by transaction — a card you started tracking mid-cycle, or a missed bank alert. Damla books the difference as an adjustment.
- A number in your books does not match your bank's app, and you want to bring it into line.
- You want to see the corrections Damla has made to its books.

## Step by step

1. Open Activity, the list of every transaction.
2. Tap **Filter** and choose **Starting balances** to see the opening figures, or **Adjustments** to see the rows Damla wrote: its corrections, with the opening figures among them.
3. Read a starting-balance row: it is named after the account, and the short line under it says **Starting balance**. Where Damla corrected what a holding cost, the row says **Cost corrected** and names the holding instead.
4. Read an adjustment row: it is titled **Adjustment**, and the short line under it names the account and the reason Damla wrote.

To bring an account into line, the fix is always an entry, never a figure you retype. Update the account with **Update from screenshots** using your bank app, or import a statement and let Damla reconcile. There is no field that overwrites the balance of an account you already use; Damla writes the correcting entry for you.

> **Note:** Every amount in Damla's books moves between two places. A starting balance or adjustment takes the difference from one reserved account named **Opening balances**. That is why it can sit outside spending and income without anything being counted twice.

## Good to know

### Why starting balances are hidden

Starting balances are hidden from the plain Activity list, because they are part of set-up and not something that happened. Searching, or choosing one account in the same **Filter** menu, shows them again.

### Adjustments have plain-word reasons

An adjustment's short line names the account and the reason, for example "Balance brought forward" or "Up to the statement". Damla stores each reason with the reserved opening "Reconciliation: " and leaves that opening off in the list. The entry is also marked as written by an import, so Damla can recognise its own adjustments later. Adjustments written by older versions of the app, which used the same words without the opening, are recognised too.

### A statement import tidies up the adjustments in its period

When you import a statement that states a closing balance, Damla reconciles the account:

- Earlier adjustments inside the statement's period are removed.
- At most two fresh ones are added: one so the books before the period equal the statement's opening balance, and one for anything still missing at the end.
- Afterwards your books match the statement's opening and closing balances, and every transaction counts once.

If a statement does not state a closing balance, nothing is reconciled: without that figure there is nothing to reconcile to. If every row of the statement is already recorded, the import button reads **Reconcile to the statement**, and the same tidy-up still runs.

> **Note:** A card owes money in two parts: the statement your bank has already issued, and what you have spent since it. **Reconciliation: last statement as shown by the bank** and **Reconciliation: spent since the last statement, as shown by the bank** are Damla's reserved words for that split, written when a card's figures are brought in from a screenshot of your bank app. When you set the amount still to pay on a card's **Details** instead, the split is written under the same reserved opening. Either way the total the card owes stays as it is.

> **Limit:** Damla counts these rows in an account's balance and in your forecast, but never as spending or income in your reports.

## Related

- [The Activity list](/guide/recording/the-activity-list/)
- [Importing a statement](/guide/capture/importing-statements/)
- [The Accounts page](/guide/accounts/accounts-page/)
