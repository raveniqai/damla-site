---
title: Backup and restore
summary: Encrypted backups to a folder you choose, and how to restore.
order: 20
---

# Backup and restore

A backup is a single encrypted file with everything Damla holds: your accounts, transactions, plans and settings. You make one to keep your books safe, and to restore them if you delete the app.

## When to use it

- Before you delete the app. Deleting the app erases its data.
- Before any big change to your records, or before installing a test or pre-release version of the app.
- When you want a copy Damla makes every day, without being asked.
- When you want a complete copy of your books, held outside the app and in your hands.

Backups live in Settings. Open Today, tap the gear at the top right, then **Backup and your data**. Everything under **Backup** happens on the phone; you choose where each file is saved.

## Step by step

### Make a backup file

1. Open Settings, then **Backup and your data**.
2. Tap **Export an encrypted backup**.
3. Type a passphrase of at least 8 characters and tap **Export**.
4. Tap the share button that appears. Save the file to Files or iCloud Drive, or send it to your Mac.

> **Careful:** The passphrase is the only key to the file. Nobody, including Damla's developer, can open the backup without it, and Damla cannot recover it. Keep a copy of the phrase somewhere safe, separate from the file.

> **Note:** Restoring replaces everything on this phone with the backup. You cannot merge a backup with what is already there.

### Restore a backup

1. Open Settings, then **Backup and your data**.
2. Tap **Restore from a backup** and choose the `damlabackup` file.
3. Type that backup's passphrase.
4. Damla warns you that this replaces all data on this phone. Tap **Replace everything** to go ahead.

A manual backup and an automatic one are the same kind of file, and **Restore from a backup** opens both. Restoring works from any encrypted backup file.

### Let Damla back up on its own

Automatic backups write the same kind of encrypted file to a folder you pick, at most once a day.

1. Open Settings, then **Backup and your data**, then **Automatic backup**.
2. Tap **Choose a folder and start** and pick a folder in the Files picker.
3. Type a passphrase of at least 8 characters and tap **Start**. Damla writes the first file at once.

From then on, an encrypted copy is saved to that folder once a day, when you leave the app.

> **Note:** The automatic backup keeps its passphrase in this phone's Keychain, so you do not have to type it again. You still need it to restore, so keep a copy of it somewhere outside the phone as well.

Turning it off with **Stop automatic backups** does not delete the files already written.

## Good to know

> **Limit:** An automatic backup runs only when you leave the app. If you do not open Damla for several days, nothing is backed up in that time.

- A backup you export by hand gets a name that starts with `Damla-`, then today's date, ending in `.damlabackup`.
- An automatic backup's file name starts with `Damla-auto-`, then the date, ending in `.damlabackup`. Today's file replaces the earlier one for the same day.
- A folder in iCloud Drive keeps the automatic backup off this phone too.
- On the **Automatic backup** screen you can see the folder and when the last backup ran, and tap **Back up now** to run one straight away.
- The newest 7 automatic backups are kept; older ones are removed automatically.
- If the last automatic backup is at least three days old, Damla shows a reminder on Today. If you have never set up an automatic backup and have been recording for a while, Today shows a "Back up your data" row instead.
- If a trial or subscription has ended, Damla becomes read-only, but exporting and restoring a backup still work.
- If the passphrase of an existing backup is lost, the file cannot be opened. Check that you still remember it before you rely on the file.

## Related

- [Settings, page by page](/guide/data/settings-map/)
- [Export and the family snapshot](/guide/data/export-and-family-snapshot/)
- [Privacy and your data](/guide/data/privacy-and-your-data/)
- [Troubleshooting](/guide/help/troubleshooting/)
