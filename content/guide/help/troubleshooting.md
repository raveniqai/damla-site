---
title: Troubleshooting
summary: When a number looks wrong or an alert does not arrive.
order: 10
---

# Troubleshooting

This page covers two kinds of problem: a bank message that never reached Damla, and a figure in your books that needs a correction. The checks below show which one you have. Each fix touches one record.

## When to use it

- A bank message was not added as a transaction, or you do not know where it went.
- An account's balance differs from what your bank shows.
- A holding's value or cost looks wrong, or a staged purchase payment has the wrong amount.
- The safe-to-spend number looks too high or too low, or a rate or price did not change after a refresh.

## Step by step

When a bank message did not arrive:

1. Open Settings, tap **Bank messages and statements**, then **Automations (Shortcuts)**, and look at the **Is it working?** section. It shows when the last bank message reached Damla, or says **Nothing has reached Damla yet**. It also tells you if statements are **waiting for your review**, and has a button to **Open the Shortcuts app**.
2. Send yourself a test message, as the note under that section suggests.
3. Tap **Recent alerts**. A test message should appear there within a minute. If it does not, the automation is not running.
4. Look at the reason shown next to the entry. If the message is listed but was not added, the reason is written there. For example, the card's last digits are not known yet: enter them once in the Inbox and Damla learns them.
5. If nothing is listed at all, open your automation in the Shortcuts app and check that it is set to **Run Immediately**, and that the trigger matches your bank's messages (the sender or keyword you chose).
6. Check the action itself too: its Text field must hold **Shortcut Input**, the blue pill suggestion above the keyboard, not words you typed yourself.

> **Tip:** While testing, you can leave **Notify When Run** switched on in the automation; the steps on the Automations screen tell you to switch it off if you see it.

> **Tip:** If one of Damla's actions is missing when you tap Add Action in Shortcuts, open Damla, force-quit Shortcuts and open it again. If it is still missing, restart the iPhone. The Automations screen lists the four actions to look for under **Damla's actions**.

## Good to know

### A balance is different from the bank

Correct the account to the balance your bank shows. Damla adds one adjustment that is not income or spending, so the correction is recorded without turning into earnings or costs.

### A holding's value or cost is wrong

Open the holding. Tap **What it cost** to correct what you paid for it. Under **Values on file**, tap a wrong value to correct it, or swipe it away to delete it. The newest value is the one in force, and a value you type on a day beats a fetched one from the same day.

### A staged payment has the wrong amount

Open the purchase and tap the payment to change its amount or date, or swipe the payment to delete it.

### The rate or price did not change after a refresh

Tap **Refresh now** in Settings and read the report: it says for each source whether it was **Updated**, **Skipped** (with the reason, such as price lookup being off or no tickers set) or **Failed** (with the error). A rate or price you typed today is used until the next refresh replaces it.

### The safe-to-spend number looks too high or low

Open the Forecast from **Your balance ahead** on Today and look at the lowest point. Then check that your income and bills are in Plan, Income & bills, that each card has a billing cycle and a paying account, and that the Look ahead setting is what you want: it sets how far ahead safe to spend looks, at least.

> **Note:** If something is still unclear after all this, it is probably a gap in the app, not a mistake of yours. Note what you did and what you expected to happen.

## Related

- [How automatic capture works](/guide/capture/how-automatic-capture-works/)
- [What Damla ignores, and undoing an alert](/guide/capture/what-damla-ignores/)
- [The inbox](/guide/recording/the-inbox/)
- [Forecast and safe to spend](/guide/planning/forecast-and-safe-to-spend/)
