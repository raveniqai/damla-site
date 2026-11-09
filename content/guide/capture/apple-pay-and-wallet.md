---
title: Apple Pay and Wallet payments
summary: Add card payments as they happen.
order: 40
---

# Apple Pay and Wallet payments

When you pay with Apple Pay or tap your card, Wallet knows the payment at once. A Wallet Transaction automation sends each payment to Damla as it happens, so it is recorded for you.

## When to use it

- Your cards are added to Apple Wallet and Damla should record every payment as you make it.
- Your bank's message about the payment arrives late, or not at all, and you want it recorded anyway.
- You want the merchant recorded as Wallet reports it.

## Which actions to use

Both of these are Damla actions in the Shortcuts app, and both do the same job:

- **Add to Damla**, with its Text set to a one-line sentence about the payment and its Source set to Wallet payment.
- **Add card payment to Damla**, which takes the merchant, the amount and the card direct from the Wallet transaction.

The amount arrives with its currency already in it, so there is no separate currency field and no conversion is guessed.

## Step by step

One automation per card, for cards you added to Apple Wallet.

1. Open Damla, then Settings, then Bank messages and statements, then Automations (Shortcuts).
2. Under "Apple Pay payments", type the last 4 digits of your card and tap Add.
3. Tap the card's entry in the list to see the exact steps for it. You can copy the steps, or copy a prompt to paste into the Shortcuts app's Apple Intelligence.
4. Open Shortcuts, tap Automation, then the plus button, then choose Wallet Transaction and pick the card.
5. Choose Run Immediately, then Next.
6. Choose New Blank Automation, tap Add Action, search for **Add to Damla** and pick it.
7. Set its Text to the sentence the steps show you: *Purchase of [Amount] with Card ending (your digits) at [Merchant].* Damla has already written your card's digits into that sentence, so only **Amount** and **Merchant** are left in brackets.
8. Tap into the Text field and insert the Amount and the Merchant from the Wallet transaction where the brackets are.
9. Set Source to Wallet payment.
10. Tap Done.

> **Tip:** The sentence names the card by its digits, the same way a bank text does. If the digits match the last digits you saved for that card in its account details, Damla files the payment under it straight away.

If you prefer, use the **Add card payment to Damla** action instead of Add to Damla. Its three fields — Merchant, Amount and Card — take their values from the Wallet transaction.

## What happens to each payment

- A payment on a card Damla knows is added as a transaction at once.
- A payment on an unknown card, or anything Damla cannot read, waits in the Inbox for one tap.
- If the same payment also reaches Damla from a bank text, it is recorded once. A second report with a matching shop name is answered **Already in Damla**. If the shop is named differently and it arrives within 15 minutes of the first, the second report waits in the Inbox as a possible duplicate for you to discard.

> **Note:** With the phone locked the books cannot be read, so Damla keeps the payment and adds it the next time you unlock the app.

## Good to know

- **Send a test payment through** after setting up. The Automations screen shows when the last message reached Damla, and **Recent alerts** lists each one with what was done. If it did not arrive, the automation is probably not set to Run Immediately.
- **The digits matter.** A card whose last digits you saved in its account details is matched automatically. A card Damla does not know waits for you to tell it which one it was; you do this once per card.
- **If Damla is read-only** because a trial or subscription has ended, the action says so and nothing is added until you subscribe again.

## Related

- [Bank texts and emails](/guide/capture/bank-texts-and-emails/)
- [How automatic capture works](/guide/capture/how-automatic-capture-works/)
- [The inbox](/guide/recording/the-inbox/)
- [Credit cards](/guide/accounts/credit-cards/)
