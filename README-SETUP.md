# Kosatka Finance 2.0 — Cloud Accounts

This upgrade keeps your existing dashboard sections and asset paths while replacing browser-only username/password accounts with Supabase email accounts and private cloud storage.

## Included
- `index.html` — updated dashboard with cloud authentication and sync
- `supabase-config.js` — add your Supabase Project URL and publishable key
- `supabase-schema.sql` — private cloud table with Row Level Security

## Setup
1. Create a project at https://supabase.com/dashboard.
2. Open **SQL Editor**, paste `supabase-schema.sql`, and run it.
3. In **Project Settings → API** (or the Connect dialog), copy the Project URL and **publishable** key.
4. Replace the two placeholders in `supabase-config.js`.
5. In **Database → Publications** (or the Realtime settings for your project), enable the `user_data` table for the `supabase_realtime` publication so open sessions can receive cross-device updates.
6. In **Authentication → URL Configuration**, add this redirect URL:
   `https://baufunt.github.io/kosatka-dashboard/`
7. Keep your existing `assets/` folder in your GitHub repository.
8. Replace the repository `index.html` with this package's `index.html`; add `supabase-config.js` and `supabase-schema.sql` to the repository root.
9. Commit and push to `main`, then wait for GitHub Pages to deploy.

## What syncs
Balances, ledger transactions, and operation progress are saved to a row belonging to the signed-in Auth user. Row Level Security restricts each user to their own row. Realtime updates refresh the dashboard when that same account changes data in another open browser/device.

Built-in images continue loading from the existing `assets/images/` paths. Custom image overrides remain local in this version.

## Safety
The browser may contain the Supabase **publishable** key; that is expected. Never place a `service_role` key, secret key, or database password in website files. Cloud sync is not active until the Supabase project is created, the SQL is run, and `supabase-config.js` is filled in.

If you have data in an old browser-only account, export a JSON backup from the old site before replacing it, then import it after signing into the new cloud account.

Fan-made tracker; not affiliated with Rockstar Games.
