---
title: Bills coming
summary: How a bill announced by a message is remembered and then settled by the card charge.
order: 50
---

# Bills coming

Bills coming is where Damla keeps a bill from the moment a message announces it ("your bill is ready") until the charge that pays it arrives. The announcement itself is not spending: no money has moved. The card or bank charge that pays the bill is the one real transaction, and it settles the bill here, so nothing is counted twice.

![Bills coming.](damla-bills.png)

## When to use it

- A utility or other provider sends a "your bill is ready" message and you want it remembered without recording it as spending.
- You want to see everything announced but not yet charged, with amounts and due dates.
- A bill was noted by mistake and you want to take it away.

## Step by step

1. Let the bill notice reach Damla through your Shortcut automation (or paste the message into **Add by sentence**).
2. Open the Plan tab and tap **Bills coming**. The page's title reads **Bills**; Today shows a notice with the words **bills coming** that opens this same list.
3. Tap a bill to see its details: the amount, the due date, the customer account it is for, the breakdown, and, once known, which card or account usually pays that provider.
4. When the charge arrives (a card alert or a statement row), Damla matches it to the bill and the bill moves down to **Paid**. You do not have to do anything.
5. Check the settled transaction in Activity: when the bill had a breakdown, the provider's charge now carries the bill's categories.

## How the bill settles

- The matched charge is the one transaction for the bill. If the bill's breakdown adds up exactly to its total, that one charge is split across categories by the breakdown lines. Electricity, water, cooling, gas, internet, phone and sewerage go to **Bills & utilities** (or **Utilities** if you have no such category). Housing goes to **Housing** (or **Rent**, or **Bills & utilities**). A line none of these fits keeps the category the charge was filed under.
- The bill is then marked paid, and Damla remembers which card paid that provider.
- Reminders of the same bill ("is due", "overdue") only refresh the bill's due date; they never add a second one.
- Once Damla knows which card pays a provider, an open bill from that provider is already in your forecast: for a card, the cash leaves the account that pays that card on the card's due date, not when the notice arrived.

## Where to see it

- **Today**: the notice with the words **bills coming** opens this page.
- **Plan, Bills coming**: the same bills, each with its breakdown and what has been paid. When the open bills are all in one currency, a card at the top totals them.
- **Settings, Recent alerts**: each notice and reminder, with the reason it was noted.
- The forecast (from Today, **Your balance ahead**) shows the bill as a payment when the paying account is known.

## The shape of a bill

The bills and amounts you see are your own, so no worked figures are given here. The shape is this: a notice arrives with a total and an optional breakdown; the bill waits under **Coming**; one charge pays it; the charge is split across the breakdown's categories; the bill moves to **Paid**.

## Good to know

> **Careful:** The first charge from a provider may not match its bill if the card statement gives the company a very different name than the bill message does. The charge is then added as an ordinary transaction. You can correct its category in Activity.

> **Note:** A wrongly noted bill can be undone in **Settings, Recent alerts**: the bill is forgotten and no transaction was involved. A mistake caught before any charge arrives can also be swiped away in **Plan, Bills coming**.

> **Limit:** A charge is matched only while the window runs: from just before the notice arrived until up to 45 days after the due date, for the same amount and the same business. A different bill, or a charge months later, is not matched.

- Until it is charged, a bill is not a transaction: the spending reports do not count it.
- If you undo the alert that added a settled charge (in Settings, Recent alerts), the transaction is deleted and the bill is owed again.
- If the bill repeats, set it up in **Income & bills** instead: anything there that repeats every 3 months or less often is counted in Set aside, which works out what to put aside each month.

## Related

- [Income and bills that repeat](/guide/planning/income-and-bills/)
- [How automatic capture works](/guide/capture/how-automatic-capture-works/)
- [What Damla ignores, and undoing an alert](/guide/capture/what-damla-ignores/)
- [Credit cards](/guide/accounts/credit-cards/)
