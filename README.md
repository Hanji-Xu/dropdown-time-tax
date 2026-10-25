# 06 Dropdown Time Tax

**▶ Play it:** https://hanji-xu.github.io/dropdown-time-tax/

**Observation:** Alaska is second in every alphabetical list of US state names, so Alaskans barely scroll. Wyoming is last. What does your place in the alphabet cost you over a lifetime?

**What it does:** the page is dressed as a plain, dense government form (a fictional "Office of Dropdown Time Accounting"), because that is where long dropdowns live.
1. **Speed test.** Find 8 named countries in the real 249-entry country dropdown. A straight-line fit of time against list position gives your personal seconds per row. People who type to select get a slope near zero, and the page says so.
2. **U.S. state.** Pick your state (50 + DC). Shows your position, extra time per selection vs the first entry, the lifetime cost and the cost summed over everyone who lives there, next to Alaska and Wyoming.
3. **Country.** The same for the ISO 3166-1 list (249 entries), next to Afghanistan, the United States and Zimbabwe.
4. **Country and city.** Country plus city from every place of 15,000+ people in that country (GeoNames), e.g. 3,407 US cities.
5. **Statement of lifetime dropdown liability** totals the three.

Each real selection is also timed and compared with what your fitted line predicts.

**Findings:** with the default 35 ms per row, a Wyoming resident pays about 21 minutes more over a lifetime than an Alaskan in a state dropdown, not hours. A typer pays almost nothing. Long country and city lists are where the minutes add up.

**Model (dense technical notes at the bottom of the page):** per-selection tax = slope × (position − 1); lifetime = tax × selections per year × 62 form-filling years; population total = tax × selections per year × residents. Selections per year (12 state, 6 country, 2 country+city) are estimates and editable on the page. Data: 2020 Census state populations, ISO 3166-1 via pycountry, World Bank population (2025), GeoNames cities15000 (CC BY 4.0), CDC NCHS life expectancy.

**Source:** `source/` holds `template.html`, the data files (`dens.csv`, `countries.json`, `cities.json`) and `build.py`. `python3 build.py 06 ../index.html` rebuilds the page.

---

Part of **Art Insights**, a series of interactive pieces by Hanji Xu. Open `index.html` in a current browser; it is a single self-contained file with no network access or libraries. See also [01 Stubble Field](https://github.com/Hanji-Xu/stubble-vector-field).
