# 06 Dropdown Time Tax

**▶ Play it:** https://hanji-xu.github.io/dropdown-time-tax/

**Observation:** Alaska is second in every alphabetical list of US state names, so Alaskans barely scroll. Wyoming is last. What does your place in the alphabet cost you over a lifetime?

**What it does:** the page is dressed as a plain, dense government form (a fictional "Office of Dropdown Time Accounting"), because that is where long dropdowns live.
1. **Speed test.** Find 8 named items in a 250-entry dropdown of unfamiliar dishes and foreign words (same length as the country list, so knowing the list can't help). A straight-line fit of time against list position gives your personal seconds per row. People who type to select get a slope near zero, and the page says so.
2. **Address.** Chained dropdowns, the way address forms work, so only real combinations exist: country, then state / province / prefecture, then city, then district where that is the convention (China: province, prefecture-level city, district, e.g. Xinjiang, Ürümqi, Tianshan District). Japan's Tokyo list includes its wards (e.g. Shibuya-ku). Each field shows your position, extra time per selection vs the first entry, the lifetime cost, and your actual measured time.
3. **Statement of lifetime dropdown liability** totals the fields.

**Findings:** with the default 35 ms per row, a Wyoming resident pays about 20 minutes more over a lifetime than an Alaskan in the state dropdown, not hours. A typer pays almost nothing. Long country and city lists are where the minutes add up.

**Model (dense technical notes at the bottom of the page):** per-selection tax = slope × (position − 1); lifetime = tax × selections per year × 62 form-filling years, summed over fields. Selections per year (country 6, state 12, city 2, district 2) are estimates and editable on the page. Address data: Countries States Cities Database (dr5hn, ODbL 1.0), the open dataset behind many web form dropdowns. Life expectancy: CDC NCHS.

**Source:** `source/` holds `template.html`, `testwords.py` (speed-test list), `places.json` (built by `prep_places.py` from the Countries States Cities Database CSVs) and `build.py`. `python3 build.py 06 ../index.html` rebuilds the page. Address data © Countries States Cities Database contributors, ODbL 1.0.

---

Part of **Art Insights**, a series of interactive pieces by Hanji Xu. Open `index.html` in a current browser; it is a single self-contained file with no network access or libraries. See also [01 Stubble Field](https://github.com/Hanji-Xu/stubble-vector-field).
