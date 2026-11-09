---
title: Prices and exchange rates
summary: What Damla looks up online, when, and how to type your own.
order: 40
---

# Prices and exchange rates

Market data is the only look-up Damla does on its own: exchange rates for the currencies you use, and prices for the holdings you choose to track. Both are optional, and Damla works fully offline.

## When to use it

- You have an account or a card in another currency and want the rate it is converted at to stay current.
- You track a stock or fund and want its price fetched instead of typing it each time.
- A rate or price looks wrong, and you want to see what a refresh brought, or type your own for the day.

## What is sent, and nothing more

- For rates, Damla sends only currency codes.
- For prices, Damla sends only the ticker symbols you set for your holdings.
- No amounts, names or personal data are sent. A bank-name logo search elsewhere in the app runs only when you tap it.

## When it refreshes

- About once a day: when you open the app if the data is older than a day, and again when you come back to it after a day.
- In the background while the app is closed, when iOS allows it. iOS decides if and when this happens, so the refresh on open is the one to rely on.
- Whenever you tap **Refresh now** in Settings, with a short minimum wait between taps and a longer one after failures.

Each source is fetched on its own: if one fails, the other keeps its data.

## Step by step

### Switch prices on

1. Open the holding's page and enter its ticker. You can also set tickers in Settings, **Currencies and prices**, under **Tickers**.
2. Turn on **Look up prices for holdings** (in the same Settings page, under **Market data**). Price lookup starts off.

### Check a refresh, or type your own value

1. Open Settings, then **Currencies and prices**.
2. Tap **Refresh now**. A report titled **What changed** lists each source — **Exchange rates** and **Prices** — each marked **Updated**, **Skipped** or **Failed**:
   - **Updated**, with a line per item: the new rate or price, and what it was before (or *new*, or *unchanged*).
   - **Skipped**, with the reason: price lookup is off, no tickers are set, daily rate updates are off, or you only use your main currency.
   - **Failed**, with the error. If a service is busy, wait a moment and try again.
3. The end of the report shows what the refresh did to your numbers: net worth and the lowest point in 90 days, before and after.
4. Under **Exchange rates**, each foreign currency shows the rate in force and whether it was **Fetched** or is **Your rate**, with its date. To set your own rate, type it under **Set your own rate** and tap **Save**.

Under the toggles, Damla shows when each source was last updated, or **Never updated**; the prices line also shows **Off** while price lookup is switched off.

## Which value wins

- The newest rate or price is the one in force.
- A rate or price you type wins on the day you enter it. The next refresh replaces it with a newer fetched one. The report says when your own value is still being used.
- Prices quoted in pence are converted to pounds.

## Good to know

> **Note:** Card purchases in another currency are estimated from the latest exchange rate plus your bank's markup, 2.5% when you have not set one, and marked with ≈ until the statement makes the amount exact. The markup is set in Settings, **Currencies and prices**, under **Card purchases in another currency**.

> **Limit:** An automatic refresh runs at most once a day. Beyond that, refresh only when you tap **Refresh now**. If the rate or price did not change after a refresh, read the report: it says what was updated, skipped or failed, and whether a value you typed today is still being used.

> **Note:** Rates come from exchangerate-api.com. Prices come from a public quote service.

> **Note:** Damla gives information and estimates from your own books. It does not give investment or financial advice.

## Related

- [Investments and holdings](/guide/holdings/investments/)
- [Credit cards](/guide/accounts/credit-cards/)
- [Privacy and your data](/guide/data/privacy-and-your-data/)
- [Troubleshooting](/guide/help/troubleshooting/)
