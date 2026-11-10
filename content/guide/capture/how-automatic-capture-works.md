---
title: How automatic capture works
summary: Bank texts, emails, Wallet payments and statements, and what Damla does with each.
order: 10
---

# How automatic capture works

Automatic capture is how a bank message becomes a transaction without you typing anything. Damla reads the texts, emails, Wallet payments and statement files that reach it, works out what each one is, and then either adds it, asks you about it, or leaves it alone.

## How messages reach Damla

iOS gives apps no access to messages or mail, so Damla never reads them on its own. Something reaches Damla only when you send it, in one of three ways:

- **A Shortcut you set up** passes each new text, email or Wallet payment to Damla as it arrives.
- **The share sheet**: you select a message and share it to Damla.
- **The file picker**: you choose statement files to import.

Everything is read on the phone. Nothing is uploaded.

## What happens to a message

Damla checks each message against the same list of rules, in this order, and stops at the first one that fits.

1. **One-time and approval codes are dropped.** The words of the message are never stored, so a code cannot be read back later. All that stays is one line in the log saying "One-time code: never kept".
2. **A bill notice is remembered as a bill.** "Your bill is ready" is not a payment: the money has not moved. Damla keeps it as an expected bill, and the card charge that pays it later is the one real transaction.
3. **Adverts, limit and rate notices, reminders and announced future charges are skipped.** They name an amount, but no money moved. When such a message is about money, Damla logs its first words, so you can see a wrong call.
4. **A clear bank alert is added at once.** A purchase, refund or income whose card or account digits match one of your accounts becomes a transaction straight away. Card payments, refunds and transfers are recognised. The category comes from how you filed that payee before, falling back to **Other** for spending and **Other income** for money in.
5. **Anything unclear waits in the Inbox** for one tap. Nothing that creates a commitment — a bill, a loan, an instalment plan — is added without your confirmation.
6. **A message that is not about money at all is dropped.** It is not kept and not logged, so a private message never lands in the inbox or the log.

## Where to check what happened

- **Recent alerts** (Settings > Bank messages and statements) is a log of the last 50 alerts, newest first, each with a short reason: Added, Waiting in the inbox (and why), Already recorded, Ignored, or a bill noted as coming. If a bank message arrives and nothing shows up here, the Shortcut did not run.
- **The Inbox** shows on Today as **N waiting for your OK**. Tap an item to open it in **Add by sentence**, where it is read again for you to check. It leaves the Inbox when you save it, and **Discard** takes it out without adding anything.
- An alert Damla acted on can be taken back: in Recent alerts, swipe right on the line and tap **Undo**. The transaction it added is deleted, or the bill it noted is forgotten.

## Good to know

- **The same alert twice is added once.** A purchase reported again by the bank's text, its email or Wallet shows as already recorded. A second report of the same amount within a few minutes waits in the Inbox for you to decide.
- **The first alert from a new card waits in the Inbox**, because Damla does not know that card's last digits yet. Complete it once and Damla learns them.
- **A message that arrives while the phone is locked** waits, and is added the next time you open the app after unlocking the phone. If your books are read-only, it stays in that queue until you can edit again.
- **A statement PDF** sent by a Shortcut is queued. Today shows **N waiting to review** with the note "Statements or screenshots. Nothing is added until you confirm", and you review it before anything is added.
- **Where the phone has Apple Intelligence**, the model may only read fields from the text. Every number and name it returns must appear in the text or it is ignored, and what it reads is never saved without you seeing it.
- **Reading is by wording and is not perfect.** An offer worded like a payment can occasionally get through, and an unusual wording can wait in the Inbox instead of being added. Limit each Shortcut to your bank's sender or subject, so unrelated messages are never sent to Damla.

> **Limit:** iOS runs your Shortcuts, not Damla, and can occasionally skip one. Check Recent alerts now and then.

## Related

- [The automation setup wizard](/guide/capture/setup-wizard/)
- [The inbox](/guide/recording/the-inbox/)
- [What Damla ignores, and undoing an alert](/guide/capture/what-damla-ignores/)
- [Importing a statement](/guide/capture/importing-statements/)

![Settings > Bank messages and statements > Automations.](damla-automations.png)

