# 06 Dropdown Time Tax

**Observation:** Alaska is second in every alphabetical list of US state names, so Alaskans barely scroll. Wyoming is last. What does your place in the alphabet cost you over a lifetime, and how does that compare with what your place on the map costs you?

**What it does:**
1. **The scroll tax.** Pick where you live in a real dropdown (US states with or without DC and territories, postal codes, or the 249-entry ISO 3166-1 country list). The page shows the extra time per pick against the first entry, the lifetime cost, and the cost summed over everyone who lives there, as a bar chart over every entry.
2. **The waiting tax.** Commute time by state from the Census Bureau's American Community Survey, as a proxy for the waiting that crowded places impose, plotted against population density with a log-density fit.
3. **Calibrate with your own hand.** Find 8 named entries as fast as you can; a straight-line fit gives your personal cost per row, which can replace the model.

**Findings:** Alaska vs Wyoming in a 51-entry state list is about 20 minutes per lifetime (range roughly 4 minutes to 2 hours), not hours. A US resident in a 249-row country list loses about 2 hours. Commute differences between states are over 1000× larger; commute vs log10 density gives r = 0.80.

**Model (documented in the page):** per-pick tax is a mix of mouse (scroll past hidden rows plus a Fitts'-law point), keyboard type-ahead (fewest letters to reach the entry), touch (distance-proportional picker) and autofill (zero). Only the position-dependent part counts. Every input is labelled DATA, EST, MODEL or YOU, with its source or reasoning.

**Flagged:** commute is a proxy for waiting, not a stopwatch on queues. Visible rows default to 20 (Chromium's popup limit); macOS native menus show more. Some commute figures came via a third-party transcription of the ACS table and are marked as such in the page.

**Source:** `source/` holds `template.html`, the data files and `build.py`. `python3 build.py 06 ../index.html` rebuilds the page.

---

Part of **Art Insights**, a series of interactive pieces by Hanji Xu. Open `index.html` in a current browser; it is a single self-contained file with no network access or libraries. See also [01 Stubble Field](https://github.com/Hanji-Xu/stubble-vector-field).
