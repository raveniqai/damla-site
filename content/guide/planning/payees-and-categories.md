---
title: Payees and categories
summary: How Damla learns where money goes and how to change it.
order: 60
---

# Payees and categories

A payee is the shop, company or person money went to. A category is the bucket its spending or income goes into, such as Groceries or Salary. This page explains how Damla files each payee the first time, what it remembers afterwards, and how you change any of it.

## When to use it

- A bank alert or pasted message was filed in the wrong category, and you want the next ones right.
- You want a category of your own, or a better name or icon for one.
- You imported a statement and Damla is asking "Who are these?" about some rows.
- You want to check how entries are being sorted before you trust the Insights tabs.

## Step by step

Tap the gear icon on the Today screen to open Settings, then tap **Categories**.

1. At the top, pick which list you want with the switch: **Spending** or **Income**.
2. Tap **Add** to make a new category.
3. Type the **Name**. The icon follows the name as you type: many kinds of spending (gym, pets, kids, insurance, repairs and more) get a matching picture on their own.
4. To choose your own picture, tap one in the grid headed **Icon**. The text under the name field then reads "Your own icon. Pick another, or tap the same one to go back to the suggestion."
5. Tap **Save**. Tap **Cancel** to leave without saving.

On this same screen:

- Tap any category to rename it or change its icon on the same sheet. It is the same sheet in both places, titled **New category** or **Category**.
- Swipe a category and tap **Remove** to retire it.

You can also make a category on the spot: under the Category picker in any entry form, tap **New category…**. It is selected right away.

## How Damla learns a payee

When you save a transaction that has a payee in a category, Damla records the pair. The next alert or message from the same shop or person is filed in that category by itself, with no question.

Two habits make this work:

- Fill in the payee field. The entry form labels it **Paid to (optional)** for spending and **From whom (optional)** for income.
- If the kind of payment changes, save it in the new category. If earlier transactions from the same payee sit in a different one, Damla asks before touching them: "Change the other N *payee*?" with **Change them to \<category\>** or **Only this one**. It explains that from now on new ones go to the new category by themselves.

Damla makes an exception for the catch-all: when you save in the form and the category is **Other** (or **Other income** for income), the pair is not remembered. An entry left there teaches it nothing.

## During an import: one question per payee

When you import a statement (a CSV file, a PDF or a screenshot), Damla groups the rows into unknown payees, so you answer once per payee, not once per row. The section is headed **Who are these? (N left)**, and it is answered before anything is imported.

Each question shows the payee's name, how many rows it covers, one example line, and a total of the money in or out. Tap **Choose…** on it and pick from:

- one of your **existing categories** (the list matches the direction of the money),
- **Use suggestion: …**, the pick Damla proposes,
- **A credit card of mine**, when the rows are payments to a card,
- **Another account of mine**, when it is money moving between your own accounts,
- **A property or asset I am paying for**,
- **A person (lend/borrow)**,
- **Do not import these**, to leave the rows out.

Suggestions come from plain wording rules for common lines: salary, cash withdrawal, bank charges, commission, EMI, direct debit, interest and so on. Where the iPhone supports Apple Intelligence, the on-device model may also propose a category. It reads the payee's wording, a few example lines, how many rows the payee covers, and whether the money mostly came in or went out — never balances or amounts. The code checks what the model says before using it. A card number in the payee text, or your own name from the statement header, is matched by code, not by the model.

Your answer counts as the truth for those rows, and Damla keeps the learned pairs for next time.

## Good to know

- Where two learned patterns both fit, the longest match wins, so "XYZ Grocery" beats a plain "Grocery" rule.
- Categories are yours to shape: nothing in the app depends on a particular name.
- Removing a category takes it out of your pickers. Old entries keep their category. The one category the app needs by name for instalment plan fees is recreated on its own if it is missing.
- The model step is optional and runs on your device. If the device cannot run it, the wording rules still do the job, and everything waits for your tap.
- Damla gives information and estimates. Which category money belongs in is your own bookkeeping.

## Related

- [Fill a form](/guide/recording/fill-a-form/)
- [Type a sentence](/guide/recording/type-a-sentence/)
- [Importing a statement](/guide/capture/importing-statements/)
- [Where the money went](/guide/insights/where-the-money-went/)
