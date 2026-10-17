---
name: "urbook-commands"
description: "urbook command catalog: everything Shan can type to Claude or the agents. Use when Shan types help, help all or help with a topic, asks what to type, or is stuck; also to suggest a shortcut after a task."
---

# urbook command catalog – what Shan can type, and where

Owner rule (Shan, 9 Oct 2026): "I cannot remember all the commands. When I'm stuck I type **help** – show me the related commands. Suggest commands while we work. Keep this catalog updated." This is the single list of every command Shan can give Claude in chat and every agent. Read it at "hi" with the other skills. Commands are not case-sensitive; words in <angle brackets> are filled in by Shan; [square brackets] = optional.

## Shan's action hours (16 Oct 2026)
Anything you need to do is only asked for Mon–Sat 16:00–20:00; Sunday is status only (lesson a7efff96). UrBuddy's first action run is 16:10.

## How "help" works
- **In Claude chat:** `help` → show only the 1–3 sections that fit what we are doing right now (e.g. working on holidays → section 3; WhatsApp → section 6), as short tables (command · what it does), then one line: "Type `help all` for everything or `help <topic>` (holidays, whatsapp, wanote, campaignrun, apps, partners, commission, options, agents, urbuddy, calendar, social, instagram, seo, ads, traffic, funnel, mail, site, skills, photos, app)". `help all` → the whole catalog in short form. `help <topic>` → that section. `help wanote` → the 5 steps in section 6a, word for word. `help campaignrun` → the steps in section 9a, word for word. `help apps` → sections 9b + 9d. `help partners` → section 9c. `help options` / `help commission` → the matching rows in section 2. `help instagram` → section 7a.
- **In an UrBuddy run (07:30 / 08:37 status · 16:10 / 18:15 / ~21:00 actions):** `HELP` → UrBuddy shows section 2 (its own commands) + the 3 most useful for today (AgentLessons 1d18f2a3, reads Wix row `urbook-commands`). `HELP <topic>` → that section. `HELP wanote` → section 6a (AgentLessons d2604c05). `HELP campaignrun` → section 9a.
- **While working:** after finishing a task, if a catalog command would do it faster next time, add one line: "💡 Next time just type: `<command>`". Never more than one tip per reply.
- **Keeping it current (Shan, 10 Oct 2026 – ALWAYS):** the moment a command is added, changed or removed – typed to Claude in chat OR written into an agent's instructions (UrBuddy reply words, words an agent accepts in its own chat, new LEARN targets, new automatic report lines) – update this catalog IN THE SAME TASK: Wix row `urbook-commands` (PATCH body + version + lastVerified) and the Claude skill `urbook-commands` (propose_skills card – Shan taps **Save**). Don't wait for "thank you bye"; at "thank you bye" only double-check nothing was missed.

## 1. Session (Claude chat, laptop or phone)
| Type | What happens |
|---|---|
| `hi` | Claude reads all urbook skills + live status (approvals, overdue tasks, agent health) and says ready |
| `thank you bye` | Claude saves every changed skill (Wix rows + Claude cards – tap **Save**), logs the session, signs off |
| `help` / `help all` / `help <topic>` | This catalog (see above) |
| `status` | Agents' health, approvals waiting, tasks due today |
| `sync skills` | Claude brings the Claude skill cards in step with the Wix `UrbookSkills` rows (cards to Save) |
| `read the credentials` / `log in to <service>` | Claude checks the access route for that service (no passwords ever) |
| `review documents` | Monthly governance review (first Saturday): Claude checks the live systems, updates the Agents Handbook and the System Design deck, commits both to Urbookvelo `docs/` with a review-log row for your approval; then reply `DONE documents` to UrBuddy |

## 2. UrBuddy – reply in the UrBuddy run's chat (07:30 plan · 08:37 approvals · 16:10 midday · 18:15 report · ~21:00 funnel check)
| Type | What happens |
|---|---|
| `thank you` | Closes that update – stops the 30-minute resend (resends only Mon–Sat after 16:00) |
| `APPROVE <n>` / `APPROVE ALL` / `APPROVE WA` | Approve item n / everything / newest WhatsApp update |
| `REJECT <n> <reason>` | Reject item n (housekeeping: nothing deleted) |
| `CHANGE <n> <what>` | Ask for a change to item n |
| `APPROVE n` / `REJECT n <why>` on a 💷 commission proposal | (16 Oct 2026, lesson 8079ada8) Approve or reject a temporary commission increase from the `commission` agent – applied at 02:07 that night, reverted automatically on its end date |
| `DO S<n>` / `SKIP S<n> <why>` / `LATER S<n>` | (16 Oct 2026, lesson 6406dd96) 💡 Best options from all agents (top 3 daily at 16:10, top 5 Saturday 18:15): DO = task for you / Claude / the agent; SKIP = dropped and the agent learns why; LATER = back next week |
| `UNPUBLISH <page>` | Take a published SEO page down |
| `DONE <task>` | Mark a board task done |
| `TASK <what> <date> <time>` | New task on the board + calendar block (Mon–Sat 16:00–20:00) |
| `WA-NOTE <who> <what> [<date> <time>]` | A WhatsApp chat the AI handed to you → task + calendar block |
| several `WA-NOTE …` lines, or whole copied handover messages, in one reply | (14 Oct 2026, lesson d2604c05) One task (+ calendar block when timed) per WA-NOTE, confirmed in one table; UrBuddy keeps only the WA-NOTE part of a copied message; duplicates of open tasks skipped |
| `WA-NOTE none` | (14 Oct 2026, lesson d2604c05) Nothing handed over in WhatsApp today – no task, closes the reminder like `thank you` |
| `HELP wanote` | (14 Oct 2026) How to find the day's handovers in WhatsApp – the 5 steps in section 6a. Also offered in the daily 📱 WhatsApp line |
| `HELP campaignrun` | (15 Oct 2026, lesson caeb073a) How to send an offer email from the Campaigns collection – the steps in section 9a, plus the newest campaign's status |
| `WA <booking ref>` | Show that customer's WhatsApp/feedback message again |
| `PAUSE <agent>` / `RESUME <agent>` / `RUN <agent>` | Stop / restart / run an agent now |
| `MOVE <agent> <time>` | Change an agent's time (also `MOVE <n>` to accept a suggested slot for a clash) |
| `LEARN <agent> <rule>` | Teach an agent a standing rule (e.g. `LEARN whatsapp never mention prices`) |
| `LESSONS` / `FORGET <n>` | List lessons / drop lesson n |
| `REJECT L<n>` / `CORRECT L<n> <text>` | Drop / reword something an agent learned by itself (Saturday list) |
| `BRAIN` / `BRAIN ALL` | Newest WhatsApp update / the full live WhatsApp instructions |
| `EDITED <item> <text>` | You changed a WhatsApp item yourself – the copy follows |
| `STATUS` | Team health and what's waiting |
| `TRAFFIC` / `TRAFFIC <n>` (e.g. `TRAFFIC 30`, max 60) | urbook visits, visitors, contact clicks, paid bookings and conversion % from Wix – last 7 days (or n days; per day up to 14, per week above), plus the booking funnel and the newest "why visitors don't book" reasons. Read-only |
| `CONSOLE` (also `console export`, `search console`, `export steps`) | The 5 steps to export Search Console numbers to Drive for the Saturday SEO report, plus whether an export from the last 8 days is already in the SEO folder. Read-only |
| `ALL MAILS` | Counts for the 6 mailboxes in contact@ (contact@ + the 5 Gmail boxes): total · new in 7 days · unread · contact@ Inbox · hidden copies due for clean-up. Read-only |
| (in the ~21:00 funnel check) what a customer told you, e.g. `customer said price too high` | Logged as a learning every agent reads (no names stored) |
| (automatic, ~21:00) | 🗣️ What visitors told us ("What stopped you?" card, real visitors only, lesson 2e7179c9) · 📢 Google Ads (clicks + cost per campaign, what ad visitors did, search terms costing money + up to 3 suggestions for you to save) · 📬 Left their email (one reminder Gmail draft each for people who agreed; you press Send) |
| (automatic, ~21:00) 🌐 All channels | (16 Oct 2026, lessons 0a6b5e28 + 1288e427) Website by source, Google Ads, social (Metricool), chatbot, WhatsApp themes, email/Leads, help form, reviews, phone clicks + every question we ask customers – 🕳️ where we lost them and 🔧 how to hold them |
| (automatic, 07:30) 🤝 partners waiting | (16 Oct 2026, lesson c34166f5) How many researched partners wait for you in Admin Guide 9a; provider replies show in 'Needs you' (16:10 / 18:15) |
| (automatic, 07:30) 💷 Commission | (16 Oct 2026) The commission agent's night summary: applied / reverted / watch / hold; proposals to APPROVE or REJECT |
| (automatic, 07:30) 📧 campaigns | (15 Oct 2026, lesson caeb073a) A campaign test waiting in contact@ ('test sent' → check it, then set Status = approved), a campaign sent (count + failed), or a failed test |
| (automatic, 16:10 · 18:15) 📱 WhatsApp | (14 Oct 2026) 'Search WA-NOTE in WhatsApp Business, paste what you find here (whole messages are fine) or reply WA-NOTE none. How? Reply HELP wanote.' |
| (automatic, Mon–Sat 16:10) 📸 Instagram clean-up | (16 Oct 2026, lesson 1029cf3c, from Mon 19 Oct) '📸 Instagram clean-up (10 min): Following → Least interacted with → unfollow 50' (100 a day from 2 Nov if no warnings). Got 'restricted' again? Tell UrBuddy – the line pauses 3 days. Reply `DONE <task>` when following is under 500 |
| (automatic) 📱 customer messages | (12 Oct 2026) For every paid booking the website emails the customer a **reminder** (day before drop-off; 3 days before a holiday starts) and a **welcome-back** with thank-you code **URBACK5** (day after the trip / holiday ends). UrBuddy then sends you the matching WhatsApp text + a WhatsApp link that opens the chat with the text ready – tap, send, reply `DONE <booking ref>` |
| (automatic, Saturday 16:10) 📸 AXA calendar for next week | (12 Oct 2026, lesson dc6e25ad; times per lesson a7efff96) Asks for next week's AXA calendar until 'AXA ▸' blocks exist for next Mon–Fri. Reply with the screenshot – or `no AXA next week` / `DONE AXA` to stop the reminder |
| (automatic, 16:10 · 18:15) ⭐ New reviews | (13 Oct 2026, lesson 1eb863d5) New Trustpilot / Google reviews the `reviews` agent copied into the Reviews collection, and any 1–2★ review you may want to answer yourself |
| `FLIGHTS` · (automatic, Saturday) ✈️ Flights | (13 Oct 2026) UrBuddy sends the Travelpayouts link https://app.travelpayouts.com/programs?name=Aviasales – tap **Performance** on the Aviasales card for this week's searches, clicks and bookings on flights.urbook.co.uk (you sign in yourself; no agent can read Travelpayouts). Reply `FLIGHTS` any day for the same link |
| (automatic) 🔑 reconnect | (16 Oct 2026, lesson ef7e8188) If a connector needs signing in again: 'reconnect <service> on your phone: claude.ai → Settings → Connectors' |
| `HELP` / `HELP <topic>` | This catalog |
| (send a screenshot of your AXA calendar) | AXA meetings added as 'AXA ▸' blocks; clashes flagged |
| any question | Answered read-only (bookings, mail, agents, skills …) |
Agent names: `urbuddy`, `inbox`, `housekeeping`, `whatsapp`, `seo` (writer), `seoreport` (Sat 16:17), `trainer` (chatbot), `social`, `learn-social`, `learn-team`, `adscheck`, `reviews` (daily 11:47), `appwatch` (17:07, app store approvals incl. 1.0.1, pauses itself when done – it reads Gmail only, so it can't see Apple's App Review messages, which appear only in App Store Connect), `campaigns` (1st + 15th 16:47, campaign drafts, occasion ideas, reminder on the 15th), `research` (daily 06:52, verified partners into Potential Partners; never waits for approvals), `partners` (Sat 16:27, partnership pipeline), `commission` (nightly 02:07, temporary commission advice). LEARN also takes `ads` and `all`. Every agent learns each run and may add 💡 suggestions (lesson 6888a570).

## 3. Holidays (Claude chat)
| Type | What happens |
|---|---|
| `add holiday <destination>` + operator file | Duplicate check → today's USD→GBP rate + £100 pp → new provider + holiday rows (asks only real decisions). Commission 15% since 13 Oct 2026 (was 30%) |
| `update holiday <destination>` + file/answers | Updates existing rows (old rates kept in remarks) |
| `show holidays [<destination>]` | List live packages and prices |
| `deactivate holiday <package>` | Takes it off sale (never deleted) |
| `apply holiday commission <provider>` | (16 Oct 2026) Applies (or reverts) an approved holiday commission change together with the holiday prices |
| `change Everest flight price <£>` / `use an Everest photo` | (16 Oct 2026) The Nepal 'Add a scenic Everest mountain flight' tick box on the results page: price (one constant FLIGHT_ADDON in public/transferPricing.js – results, cards and checkout follow; £1,500 per person since 16 Oct) or its photo. Claude pushes the code; you Publish |

## 4. Calendar & day planning (Claude chat or UrBuddy)
| Type | What happens |
|---|---|
| `add my AXA calendar` + screenshot | 'AXA ▸' blocks for that week; AXA has priority; clashes listed |
| (automatic, Saturdays) | UrBuddy asks for next week's AXA calendar until you send it (`no AXA next week` / `DONE AXA` stops it) |
| `move <event> to <day> <time>` | Moves a block (meetings with people only after you agree with them) |
| `remove <event>` | Deletes that block |
| `add <what> <date> <time>` | New urbook block / task |
| Rule | (16 Oct 2026) urbook actions, calls and blocks only Mon–Sat 16:00–20:00 (after the last AXA meeting if later); Sunday none |

## 5. Mail & inbox
| Type | What happens |
|---|---|
| (UrBuddy 'Replies to send' list) | Drafts are already in contact@ Drafts – edit and send yourself, then `DONE <task>` |
| `LEARN inbox <rule>` | Change how mail is sorted or drafted |
| `customer messages for <booking ref>` (Claude chat) | (12 Oct 2026) Claude sets up the reminder + welcome-back by hand for one booking: two Gmail drafts in contact@ and two 📱 tasks so UrBuddy hands you the WhatsApp text on the right days. Needed only for bookings the automatic job can't cover (e.g. holidays booked before 12 Oct with no start date) |
| `refund email <booking ref>` (Claude chat) | (15 Oct 2026) After you refund a booking we couldn't fulfil, Claude drafts a kind retention email with URBACK5 (£5 off, any booking) – you check and send it |
| `check mail for <topic>` (Claude chat) | Read-only search of contact@ + forwarded boxes |
| `ALL MAILS` (UrBuddy) / `all mails` (Claude chat) | Per-mailbox counts in contact@ – contact@ itself + shanmugasr81@, shanmugasr@, shanmugasr05@, thenilgirisltd@, thenilgiris15@: total, new in 7 days, unread, Inbox, hidden copies due for clean-up |
| Gmail search in contact@: `deliveredto:<gmail address>` | See the hidden copies of one Gmail box (All Mail). Don't delete them yourself – housekeeping clears them (after 7 days) after your `APPROVE` |
| (automatic) | Mail to the 5 Gmail boxes skips contact@'s Inbox (filter, 10 Oct 2026) – read it in its own mailbox; the agent still drafts from contact@ with 'send FROM <address>' |

## 6. WhatsApp
| Type | Where | What happens |
|---|---|---|
| `new WhatsApp item <what>` / `change WhatsApp item <first words>` | Claude chat | Claude writes the paste text (≤1,000 chars) |
| `done` / `pasted` | Claude chat | Claude saves it into the WhatsApp copy (row whatsapp-agent) |
| `APPROVE` / `CHANGE <what>` / `EDITED <item> <text>` | WhatsApp keeper chat (Sat 16:37) or UrBuddy | Approve / fix the weekly update / record your own edit |
| `help wanote` / `HELP wanote` | Claude chat / UrBuddy | How to find the day's handovers – section 6a |
| search `WA-NOTE` | WhatsApp Business app (search bar above the chats) | (14 Oct 2026, tested by Shan) Lists every handover – the AI ends each one with a WA-NOTE line. The AI itself cannot list chats on request (it sees one chat at a time, and it would leak customer data) |
| `WA-NOTE <who> <what> [<date> <time>]` (one or several, or whole copied messages) / `WA-NOTE none` | UrBuddy | Hand-over chats → one task + calendar block each / nothing today – closes the reminder |
| `LEARN whatsapp <rule>` | UrBuddy | Standing rule for the WhatsApp keeper |
| (automatic, next weekly update) | WhatsApp keeper | (16 Oct 2026, lesson 1216416c) Tagged links (utm_source=whatsapp) to paste, so the funnel can count WhatsApp chats that turn into bookings |

### 6a. `wanote` – find your WhatsApp handovers (1 min) – show these steps word for word for `help wanote`
1. Open WhatsApp Business → Chats.
2. Pull the chat list down a little → tap the search bar.
3. Type WA-NOTE → under Messages you see every handover with its time (ignore older dates).
4. Tap one → press and hold the AI's message → Copy.
5. Paste it in the UrBuddy chat and send (several? paste them all in one reply). The whole message is fine – UrBuddy keeps only the WA-NOTE part.
Nothing found today? Reply `WA-NOTE none`.

## 7. Social media (since 15 Oct 2026: Wednesday + Saturday only, 07:48, auto-publishes – every post is a challenge post)
Wed = holidays & flights (Nepal → South India → Sri Lanka → partner trust; first Wednesday of the month = a sample itinerary). Sat = parking (even weeks) / transfers (odd weeks), from Sat 17 Oct. Every post: a natural, no-face photo background (no brand-colour backgrounds), the challenge question + £50 draw, an 'about urbook' line, music, URFIRST10 + URBACK5; links tagged with the network (lesson c1eb61ce). Since prompt v11 (16 Oct 2026, live once you paste it) a fitting Nepal post's videos open with a few seconds of your own clip. Since 17 Oct 2026 every post uses one of six hook types and says which in its message ('Hook type: SECRET | MONEY | POV | DARE | CHOICE | CALLING' – lesson d9b98d1b); the Saturday learner reports which type wins. The task is owner-created: set London time + 'Automatically approve' on claude.ai/code/routines.
**Since 17 Oct 2026:** the `learn-social` learner runs DAILY 06:10 – it studies urbook's results and the top travel posts (vidIQ) and leaves a 'Top posts elsewhere' note (3 ready angles for the next post, 'Media to add' free-licence photos/clips, 'Needs a real clip (for Shan)'); Saturday growth check says when to add a third posting day. The post task (block pasted 17 Oct) uses these and reports 'Learned from:', 'Reply prompt:' and 'Sound: <name> (seq n of N)'. Challenge cover = ONE short question, clues in the caption (lesson e46d9b09). Every post ends with an easy reply question such as 'Which one did we miss? 👇' (lesson df73f890). No AI-made people. Sound beds play in sequence from urbook-social `audio/index.json` (lesson 95ff4a1c).
| Type | Where | What happens |
|---|---|---|
| `APPROVE <n>` | UrBuddy – only when a post failed its checks and waits | Publishes it |
| `CHANGE <what>` | Claude chat | Claude prepares a new prompt file; you paste it on the Routines page |
| `different video` / `no video` | The social post's run chat | (16 Oct 2026, prompt v11) Re-make today's videos with the next fitting clip / without a clip (before publishing; a published post must be changed in each app) |
| `LEARN social <rule>` / `REJECT L<n>` | UrBuddy | Teach / correct the social agent |
| `consent form` | Claude chat | (17 Oct 2026) Opens the urbook Video Consent Form https://claude.ai/code/artifact/5cddd898-856e-43be-a723-d97fc5d64791 – print or export as PDF; everyone you film signs it BEFORE filming (under 18: parent/guardian); keep the signed original. Then `add to socials <country>` + the clip |
| `add sound <style>` | Claude chat | (17 Oct 2026) Claude makes a new original sound bed (e.g. lo-fi, acoustic, tabla fusion), gives it the next seq number and adds it to urbook-social `audio/` + `audio/index.json` – the social post picks it up in sequence |
| `DONE` (draw) | UrBuddy | Monthly £50 winner picked |
| `vidiq niche check` | Claude chat | (16 Oct 2026) Claude uses the vidIQ connector to find what is getting big views right now in UK travel / airport reels and Nepal / Sri Lanka / Kerala travel reels (outliers 5–1,000× their creator's usual views), and turns the patterns into the social agent's hook lesson. vidIQ is on the free plan – 150 credits a month (one check ≈ 15–25) |
| `instagram audit` | Claude chat | (16 Oct 2026) Claude checks @urbookuk – profile (name, bio, link, category, following vs followers) from vidIQ public data and every old caption from Metricool – and lists what to fix (e.g. '24/7', 'free cancellation', wrong codes). You make the edits in the app |
| `add to socials <country>` + photos / videos | Claude chat | (16 Oct 2026) Claude makes them social standard (photos JPEG, short side ≥1000 px – smaller ones enlarged as `-hd`; videos MP4 1080p 30 fps, sound removed), skips duplicates against everything in urbook-social, leaves out photos with recognisable faces, **blurs company names and logos** (e.g. helicopter operators) and anything personal (bag logos, faces of crew), uploads to `holiday/photos/<country>/` and `holiday/videos/<country>/` and lists them in `backgrounds/index.json` / `backgrounds/videos.json` so the social agent can use them. Never booking papers or anything with customer names (the repo is public) |
| `blur the video names` | Claude chat | (16 Oct 2026) The clip in `holiday/videos/<country>/hold/` gets its company names blurred (or is cut to the clean seconds) and moves out of hold. Clips in `hold/` are never posted |
| `enlarge all` | Claude chat | Claude first asks **where** – answer `github socials` → every photo under 1000 px (short side) in parking/, holiday/ and transfers/ (photos/ and videos/ subfolders) gets an enlarged copy named `<name>-hd.jpg` (clips: `<name>-hd.mp4`, 1080 px) next to it; originals never changed; pushed to GitHub; the social agent then uses the -hd copy |
| `add background photo <parking\|airport\|flight\|transfer>` + photo | Claude chat or GitHub | (15 Oct 2026) Put a real-looking photo with **no faces** in urbook-social `backgrounds/<category>/` (or attach it in chat) – Claude adds it to `backgrounds/index.json` so the social agent can use it. Photos rotate; none repeats within 28 days |
| (where to put media) | GitHub urbook-social | `parking/photos` · `parking/videos` · `holiday/photos` (+ `holiday/photos/nepal/`) · `holiday/videos` (+ `holiday/videos/nepal/`) · `transfers/photos` · `transfers/videos` – used on Wednesdays (holidays) and Saturdays (parking / transfers). Photos and videos only – never saved web pages or other files |

### 7a. `instagram` – keeping @urbookuk healthy (16 Oct 2026) – show for `help instagram`
- **Unfollow slowly:** max 50 a day (100 from 2 Nov if no warnings), never on Sunday – Following → 'Least interacted with'. Keep UK airports, travel brands, partners, customers and people who comment. On 16 Oct ~750 unfollows in one evening got the account 'temporarily restricted' (it also blocked connecting the Facebook Page) – then stop for 2–3 days. Goal: under 500 following.
- **Never automate** following, unfollowing, liking or DMs – no agent or tool does it (Instagram bans for it). vidIQ has NO Instagram account connected – it reads public data only; posting is Metricool only.
- **Fix old posts by editing the caption** (post → ⋯ → Edit), not deleting – deleting loses views and comments.
- **Profile:** name 'urbook | Heathrow Parking & Holidays', category Travel Company, link www.urbook.co.uk, Facebook link = the urbook Page (not a personal profile).

## 8. SEO, Google, traffic & booking funnel
| Type | Where | What happens |
|---|---|---|
| `CHANGE <what>` / `UNPUBLISH` / `APPROVE` / `REJECT` | SEO writer's message | Fix, remove or approve a new page |
| `CONSOLE` | UrBuddy | The 5 Search Console export steps + whether this week's export is already in Drive |
| `DONE` | seoreport chat (Sat 16:17) | You've uploaded the Search Console export |
| `change <live page> <what>` | Claude chat | Claude shows the exact change and waits for `APPROVE` |
| `ads report` / `check ads` | Claude chat | Google Ads numbers vs bookings (you save changes in Google Ads) |
| `TRAFFIC` / `TRAFFIC 30` | UrBuddy | Visits → booking funnel → paid bookings → conversion % (Wix numbers + FunnelEvents) |
| `traffic` / `traffic 30` | Claude chat | Claude pulls the same Wix numbers (Analytics Data API, last 62 days max) and explains them |
| `funnel review` | Claude chat (new chat: `Hi` → `funnel review`) | (15 Oct 2026, lesson bba91762) Every night after the ~21:00 funnel check: Claude reads today's journey steps, bookings and the dashboard, explains why visitors didn't book and ships fixes (you Publish) |
| `funnel` / `dashboard` | Claude chat | Claude opens the **urbook booking funnel** dashboard (also pinned in your Claude sidebar) and explains where visitors stop |
| (automatic, ~21:00 daily) | UrBuddy – daily funnel check | Arrivals by source, the funnel (arrived → searched → saw options → chose → checkout → pressed Pay → paid), biggest drop + reason, dashboard link, 🗣️ "What stopped you?" answers, 📢 Google Ads, 📞 opted-in members who didn't book, 📬 reminder drafts, and since 16 Oct 🌐 all channels + every customer question we ask + 🕳️ where we lost them + 🔧 how to hold them. Nothing is sent – you press Send. Real visitors only (no test-site, no bots) |
| (automatic, website) | Home 20 s · Results 30 s · Checkout 55 s · any other page 30 s | "What stopped you?" card (once per page per visit); Results also offers "Email me these prices" (consent tick); Checkout shows the email notice + "Don't send me offers or reminders". Answers go to the dashboard, the 21:00 check, the SEO writer and the Saturday report |
| (automatic) | UrBuddy 07:30 · seoreport Sat 16:17 | 📊 traffic line every morning (+ one funnel line); 📊 traffic → bookings + 🧩 "why visitors don't book" + the booking funnel every Saturday; site fixes arrive as "Ask Claude: …" tasks |

## 9. Website, code & data (Claude chat)
| Type | What happens |
|---|---|
| `fix <problem> on <page>` | Claude changes the code in GitHub; you click **Publish** in the Wix editor |
| `update parking rates <service>` + Excel | Urbook Premium = base, others + fixed £ (CMS only) |
| `add / change discount code <code>` | HIGH risk – Claude shows the impact first. Live codes: URFIRST10 (£10, first booking), WELCOMEUR (10%, first booking), **URBACK5** (£5, any booking – not first-time only; the thank-you / win-back code, 12 Oct 2026) |
| `show <collection>` | Read-only look at Wix data |
| (automatic, checkout) cheaper option | (13 Oct 2026) A customer who picks a car park or a transfer driver when a cheaper one of the same type is on the same results page sees 'Same service / journey for less: <name> at £X (save £Y) [Switch]'. Switch keeps dates, airport, discount, passengers and return. Not for Park Sleep & Fly or holidays |
| (automatic, everywhere we ask for a review) | (13 Oct 2026) Always both Trustpilot and Google, neutral wording, never for a reward: confirmation page, booking email, welcome-back email/WhatsApp, UrBuddy feedback, UrHelp chat, WhatsApp AI |
| `speed check` | (17 Oct 2026) Claude runs a full speed test – PageSpeed (mobile) plus phone, tablet and laptop views of Home, a landing page, Results and Checkout – finds what makes customers wait and ships the fixes (you Publish) |
| `fix 404 <address>` / `redirect <old> to <new>` | (17 Oct 2026) Claude adds a 301 in Wix → SEO & GEO → URL Redirect Manager and checks the old address opens the real page |
| `check ad paths` | (17 Oct 2026) Every Google Ads display path (e.g. urbook.co.uk/heathrow/long-stay) is opened on the live site; any 'page not found' gets a 301. The Saturday seoreport does this too (lesson aae3628f) |
| `apple listing` | (17 Oct 2026) Claude checks the App Store Connect text (description, promo text, reviewer notes) against urbook-app docs/app-store/LISTING.md – every feature must be documented (Apple 2.5.19) |
| open `https://www.urbook.co.uk/?rc=me` (once per phone / laptop / browser) | (12 Oct 2026) That browser is remembered as you testing: everything you do on it is marked as a test and left out of the funnel, the 21:00 check, the dashboard and the Saturday report. `?rc=notme` undoes it; open it again after clearing browser data or on a new browser. `?rc=test-site` still marks one page only |
| `help campaignrun` / `HELP campaignrun` | (15 Oct 2026) How to send an offer email from the **Campaigns** collection – the steps in section 9a |
| `new campaign <occasion>` | (15 Oct 2026) Claude drafts a Campaigns row (status draft, inactive) – subject, headline, content, code, send date – for you to check and send with the 9a steps |
| `campaign plan` | (16 Oct 2026) Claude shows the year's campaign calendar from the Campaigns collection (one or more offer emails a month, all drafts until you send them) |
| (automatic, 1st + 15th 16:47) 📧 urbook Campaigns | (16 Oct 2026) Agent `campaigns` checks the upcoming drafts (festival dates, wording), learns from sent campaigns (sent, failed, URBACK5 bookings, unsubscribes), adds up to 2 new occasion drafts, and **on the 15th tells you next month's mail to check and send** from the Admin Guide section 8. It never sends, tests or approves – you do. `PAUSE` / `RUN` / `LEARN campaigns <rule>` in UrBuddy |
| `build urbook app` | (11 Oct 2026) Claude builds the urbook app – Android (Google Play), iPhone (App Store), Windows (Microsoft Store) and an installable web app – from one code base (repo urbook-app). Plan = OpsTasks + 'urbook ▸ App n/6' calendar blocks; reply `DONE <task>` to UrBuddy after each of your steps |
| `build android` | (15 Oct 2026) Claude runs the GitHub Action android-build.yml – a new .aab (versionCode +1) on a GitHub release in urbook-app, ready for Play Console |
| `windows package` | (15 Oct 2026) Claude runs windows-package.yml (PWABuilder) – a new 'urbook Travel.msixbundle' for Partner Center. **Before any Microsoft upload switch the laptop to the phone hotspot** – the home Wi‑Fi blocks upload.xboxlive.com; Claude tells you before each upload |
| `continue the app from the bookmark` | (15 Oct 2026) Claude reads BOOKMARK.md in the urbook-app repo (Expo app, phone-only workflow) and carries on with the next stage. Test version: https://urbook.expo.app (updates itself ~2 min after each change) |

### 9a. `campaignrun` – send an offer email to customers (Wix CMS on your phone) – show these steps word for word for `help campaignrun`
**How to send one (Wix CMS on your phone → CMS → Campaigns):**
1. Add a row, or edit one, with **Status = draft**. Nothing is ever sent from a draft.
2. Tick **Active** and set **Status = test**. Within the hour, one test email goes to contact@urbook.co.uk only.
3. If you're happy with it, set **Status = approved**. It goes out on the **Send date**, then Status changes to **sent** with the counts.
4. To stop a campaign, untick **Active** or set **Status = cancelled**.

Good to know:
- **Who gets it:** only customers with *subscribed* ticked. Each customer gets a campaign once; every email has a one-click **Unsubscribe** link (it unticks *subscribed*).
- **Columns:** Campaign name · Occasion · Campaign year · Send date · Active · Status · Email subject · Preview line · Headline · Content · Discount code · Discount wording · Code valid until · Button text · Button link (filled in by the system: Test sent at · Sent at · Sent count · Failed count · Last result).
- **Writing the content:** a blank line starts a new paragraph; `**word**` = bold; placeholders `{firstName}` `{code}` `{discount}` `{validUntil}` work in the subject and the content.
- **Codes:** past customers can't use first-booking codes (URFIRST10, WELCOMEUR) – use **URBACK5** (£5, anyone) or ask Claude for a new campaign code (`add discount code <code>`).
- **Checking:** if Status says *test failed*, or Failed count > 0, read **Last result** and ask Claude. Every email is logged in EmailLog (kind `campaign` / `campaign-test`).
- The website job `runCampaigns` checks every hour at :20 (backend/campaigns.js, 15 Oct 2026). Halloween 2026 sends Thu 22 Oct. Since 16 Oct 2026 also: Black Friday · Christmas 1 Dec · New Year 2 Jan · Feb half-term 1 Feb · Mother's Day 22 Feb · Eid al-Fitr 1 Mar · Easter 10 Mar · Tamil/Sinhala/Nepali New Year 1 Apr · May half-term 10 May · Father's Day 10 Jun · Summer 1 Jul · August bank holiday 16 Aug · Nepal & Sri Lanka season 1 Sep · Diwali 2027 18 Oct (all URBACK5, all drafts; the campaigns agent may move dates or add occasions such as Winter Sun). The easiest route is the Admin Guide section 8 (template, photo, Preview, Send test, Send to all); **subscribed is the only rule**.

### 9b. `apps` – show for `help apps`
**17 Oct 2026 01:26:** App Store Connect description, promotional text and reviewer notes updated for Apple's guideline 2.5.19 (Flight search + Discount code documented; 'no hidden features'); 1.0 still Waiting for Review – type `apple listing` to re-check. **urbook Travel apps – status 16 Oct 2026 evening (all 3 in review, MANUAL release):** Apple 1.0 build 5 (App Store Connect app 6823064282) – Apple asked for more information (new developer account: screen recording + 6 answers), answered and resubmitted 16 Oct 20:46, 'Waiting for Review'; **Apple's messages appear only in App Store Connect, not in contact@ – check the App Store Connect app.** Microsoft 1.0.1 (Store ID 9N2WPN24QVSG, publishing hold) – certification flagged times shown 8 h late on a US PC, fixed (UK time on any device) and resubmitted 16 Oct. Google Play 1.0.0 versionCode 2 (app 4973823328554852667, package uk.co.urbook.app, managed publishing ON) – 'In review'. When a store approves, click Publish there (OpsTasks 4be1060e iPhone / 51ed6e3c Windows / 6ed99c23 Android); then the store badges go in the live footer (OpsTask 0d1264f2). Scheduled task `appwatch` (17:07 London) reads Gmail and tells you when Microsoft or Google approve. A long screen recording won't upload from the phone to App Store Connect – share it as an iCloud link (Photos → Share → Copy iCloud Link) in the reply and Notes.

### 9c. `partners` – grow urbook with new providers (Admin Guide section 9, 16 Oct 2026)
| Type / do | Where | What happens |
|---|---|---|
| Approve / Reject ticked | Admin Guide 9a | Researched partners (up to 5 a day, verified email + phone) move to Future Providers or are dropped (your note teaches the research agent) |
| Template → tick providers → Preview → Send test to me → Send to ticked | Admin Guide 9b | Partnership email to one or many (never twice in 7 days, max 3 without reply, 20 per send, reply "not now" stops them). Every email has an Unsubscribe link (16 Oct 2026) |
| Choose provider → stage, reply, meeting, outcome → Save | Admin Guide 9c | Tracks the pipeline: to contact → mailed → replied → meeting → documents → signed → onboarded |
| Log a contact → Save | Admin Guide 9c | (16 Oct 2026) After a call, WhatsApp, meeting or email you sent by hand: choose it in **Log a contact** and Save – adds 1 to **Times contacted** (emails sent from 9b count by themselves; it never resets) |
| Unsubscribed tick + reason → Save | Admin Guide 9c | (16 Oct 2026) A provider said stop (phone, reply 'not now'): no mails or calls for 3 months, then subscribed again automatically. Providers can also unsubscribe themselves from the link in every partnership email – the reason they give is saved. **Do not contact** = never again |
| `onboard provider <name>` | Claude chat | After they sign: Claude sets them up in Providers (or Hotels + weekly Park, Sleep & Fly rates) so they go live |
| `apply holiday commission <provider>` | Claude chat | Applies (or reverts) an approved holiday commission change together with the holiday prices |
| (automatic) | Sat 16:27 partners agent | Weekly pipeline table, replies (draft replies offering call times – you send), calls, outcomes, onboarding to start; since 16 Oct a **Times contacted** table (average contacts before a reply, reply / meeting / unsubscribe %, by type, email subject and contact type) + max 2 💡 ideas to improve our emails. Unsubscribed providers are never suggested for mails or calls |

### 9d. Apps over the air (16 Oct 2026)
| Type | What happens |
|---|---|
| `submit 1.0.1 <apple\|google>` | After 1.0 is published in that store: Claude checks the 1.0.1 build (over-the-air updates) and gives you the few taps to send it for review. From 1.0.1 every app screen change reaches phones automatically |
| `<apple\|google\|microsoft> app is live` | Claude marks the OpsTask Done and adds that store's badge to the website footer, the booking confirmation email and the campaign emails (you Publish the Wix site) |

## 10. Skills
| Type | What happens |
|---|---|
| `add skill <name>` / `update skill <name> <what>` / `remove skill <name>` | Claude changes both copies (Wix row + Claude card – tap **Save**); removing = marked inactive, never deleted |
| `show skills` | List of urbook skills and versions |

## Where this lives
Claude skill `urbook-commands` = Wix `UrbookSkills` row `urbook-commands` (v1.26.0, 17 Oct 2026 11:25, id 331b5682-ae78-4875-9ce7-e85d098b7390; the row's knownIssues hold v1.18.0–v1.26.0 in short form, this card holds the full tables). Change both together – straight away whenever a command is added or changed.

## Change log
- 9 Oct 2026 19:45 (v1.0.0): created at Shan's request – help / help all / help <topic>, UrBuddy HELP, one 💡 tip per reply, read at "hi", updated at "thank you bye".
- 10 Oct 2026 (v1.1.0–v1.6.0): TRAFFIC, ALL MAILS, enlarge all, review documents, daily funnel check, CONSOLE, "What stopped you?" card, Leads reminder drafts.
- 11–13 Oct 2026 (v1.7.0–v1.13.0): build urbook app, Google Ads in the funnel check, ?rc=me, customer messages + URBACK5, Saturday AXA reminder, reviews agent, FLIGHTS.
- 14–15 Oct 2026 (v1.14.0–v1.18.0): WA-NOTE none / several, wanote, campaignrun, new campaign, apps milestone, refund email, social Wed + Sat, funnel review, Luton parking is back.
- 16 Oct 2026 04:40 (v1.19.0): agent `campaigns`; `campaign plan`; the 2026–27 campaign calendar in 9a.
- 16 Oct 2026 06:10 (v1.20.0): action hours Mon–Sat 16:00–20:00, Sunday status only (UrBuddy midday now 16:10, Saturday reports 16:17–16:47); agents `research`, `partners`, `commission`; Admin Guide section 9 (help topic `partners`, 9c); `onboard provider <name>`, `apply holiday commission <provider>`; commission APPROVE/REJECT; 💡 `DO / SKIP / LATER S<n>` (help topic `options`); 🤝, 💷, 🌐, 🔑 automatic lines; `submit 1.0.1 <store>`, `<store> app is live` adds email badges (9d); `sync skills`.
- 16 Oct 2026 07:20 (v1.21.0): Admin Guide 9c 'Log a contact' (Times contacted, never resets) and 'Unsubscribed' tick + reason (3 months, automatic re-subscribe, provider unsubscribe link in every partnership email); Saturday partners report gains the Times contacted table + max 2 💡 ideas; research agent never waits for approvals. (Wix row v1.22.x: small fixes, card not changed.)
- 16 Oct 2026 14:05 (v1.23.0): `add to socials <country>` + photos/videos (social standard, duplicates skipped, faces left out, company names blurred, indexed in backgrounds/index.json + new backgrounds/videos.json); `blur the video names` (hold/ clips); social agent replies `different video` / `no video` (prompt v11 – video clip intro); `change Everest flight price <£>` / `use an Everest photo` (Nepal results add-on, £1,500 pp since 16 Oct).
- 16 Oct 2026 20:55 (v1.24.0): `vidiq niche check` and `instagram audit` (Claude chat, vidIQ connector – research only, free plan 150 credits a month); UrBuddy 📸 Instagram clean-up line Mon–Sat 16:10 from 19 Oct (lesson 1029cf3c); help topic `instagram` (section 7a: unfollow max 50 a day, never automate, edit captions don't delete, profile settings); social owner message 'Hook type:' line; 9b apps status 16 Oct evening (Apple messages only in App Store Connect; iCloud link for screen recordings).
- 17 Oct 2026 01:40 (v1.25.0): `speed check`, `fix 404 <address>` / `redirect <old> to <new>`, `check ad paths`, `apple listing` (section 9); 9b – App Store listing updated for Apple 2.5.19 (17 Oct 01:26). Bark lead mails stay ignored (Shan won't pay for leads).
- 17 Oct 2026 11:25 (v1.26.0): `consent form` and `add sound <style>` (section 7); social learner daily + ideas notes; short challenge cover; reply prompt every post; no AI people; sound beds in sequence from audio/index.json (6 new original tracks 05–10).
