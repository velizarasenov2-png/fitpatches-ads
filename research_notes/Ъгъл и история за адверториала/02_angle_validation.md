# Angle validation for the next FitPatches advertorial: is the "glucose dip" the strongest new cause, and what are the alternatives? (as of 3 Oct 2026)

Scope and method notes:
- This file builds on `research_notes/Успешни адверториали за отслабване/02_angles_mechanisms_psychology.md` (angle catalog, berberine evidence, GLP-1 era, hooks, risk tiers) and `03_case_studies_teardowns.md` (Kind Patches, Lemme, EU COD funnels). It does not repeat them. Compliance detail is in `04_compliance_policy.md`; only the parts that change the angle ranking are flagged here.
- Internal context checked: FitPatches has already produced advertorials on most candidate angles: 08 кръвна захар, 09 инсулин, 11 менопауза, 13 кортизол, 14 сън, 18 „глад в 15:00" (sugar crash), 20 вечерно хапване, 22 висцерална мазнина, 23 Оземпик, 24 микробиом, 25 жени 35+, the "winners" AD26–AD28 ("after 40" VOC hooks), and the current draft AD29 (glucose dip). Paths: `/home/user/fitpatches-ads/advertorial-*/index.html`, `/home/user/fitpatches-ads/winners_adv/`. The internal audit (06) found **no performance numbers** for any advertorial, so it is not known whether 08/18/20 (the glucose family) under- or over-performed.
- Google Trends data below was pulled directly from the Google Trends API on 3 Oct 2026. Window: weekly, 5 years (3 Oct 2021 – 3 Oct 2026). Values are relative (0–100) *within each comparison batch*. "First 12m" = Oct 2021–Sep 2022 average, "last 12m" = Oct 2025–Oct 2026 average. Explore links are given so the numbers can be re-checked; values drift slightly between pulls.

---

## 1. PREDICT / Wyatt 2021: exact findings, population, caveats, correction, and follow-up studies (2022–2026)

### Takeaway
The numbers in the AD29 draft (1,070 people; "big dippers" +9% hunger, +75 kcal in 3–4 h, +312 kcal/day) are reported correctly, but they are **observational quartile comparisons in healthy adults without diabetes**, with weak correlations (r = 0.16–0.27), a commercial sponsor (ZOE) directly involved in design and analysis, and a small US validation cohort in which the hunger and 24-h intake links were not significant after adjustment. A March 2026 independent study in JAMA Network Open (Singapore, 895 adults, 63% women, mean age 40) replicated the "dip → more hunger, eat sooner" link in real, free-choice meals, which makes it the fresher and stronger citation; one small 2024 trial found no link. Two details in the paper cut against common copy: dips were **only weakly related to the size of the preceding spike** and were *not* tied to age or BMI (men dipped slightly more), so "after 40 your sugar rollercoaster gets worse" is not supported by this study.

### Cited Findings
**Wyatt et al. 2021 (the study the draft cites)**
- Citation: Wyatt P, Berry SE, Finlayson G, … Spector TD, Franks PW, Wolf J, Blundell J, Valdes AM. "Postprandial glycaemic dips predict appetite and energy intake in healthy individuals." *Nature Metabolism* 2021;3(4):523–529, published online 12 Apr 2021, PMID 33846643 — [PubMed](https://pubmed.ncbi.nlm.nih.gov/33846643/); [Nature](https://www.nature.com/articles/s42255-021-00383-x); open author manuscript [PMC7610681](https://pmc.ncbi.nlm.nih.gov/articles/PMC7610681/)
- Population and design: PREDICT 1 enrolled 1,110 "healthy adults from the UK and US without diabetes" (UK n=1,010, from TwinsUK and online ads; US validation n=100, Massachusetts General Hospital); the analysed subset was 1,070 people, 8,624 standardised breakfasts and 71,715 ad-libitum meals over ~2 weeks at home with continuous glucose monitors (CGM). Participants fasted 3 h after the standardised breakfasts — [PMC7610681](https://pmc.ncbi.nlm.nih.gov/articles/PMC7610681/)
- The standardised breakfasts were muffins with equal calories but different carb/protein/fat/fibre mixes, plus an oral glucose drink (OGTT) — [NutritionInsight](https://www.nutritioninsight.com/news/big-dippers-overeating-caused-by-blood-sugar-drops-hours-after-eating-finds-zoe-backed-study.html); [PMC7610681](https://pmc.ncbi.nlm.nih.gov/articles/PMC7610681/)
- Who was in the cohort: the UK PREDICT 1 cohort (N=1,002) was 73% female, mean age 46.1 ± 11.9 years, mean BMI 25.6 (described in a separate 2023 PREDICT paper, not the Wyatt subset table) — [Bermingham et al., Eur J Nutr 2023](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10799113/). The Wyatt paper notes 97% of participants were white — [PMC7610681](https://pmc.ncbi.nlm.nih.gov/articles/PMC7610681/)
- Headline result (abstract): the average glucose dip 2–3 h after a meal, relative to baseline, predicted more hunger at 2–3 h (r = 0.16), shorter time to the next meal (r = −0.14), higher energy intake at 3–4 h (r = 0.19) and at 24 h (r = 0.27), all P < 0.001; dips predicted these better than the 0–2 h peak or the 0–2 h area under the curve; "results were directionally consistent in the US validation cohort" — [Europe PMC abstract](https://europepmc.org/article/MED/33846643)
- Exact quartile numbers (largest-dip quartile Q4 vs smallest Q1): hunger +9% (95% CI 5–13), alertness −2%, next meal 24 min sooner (95% CI 15–33), +75 kcal at 3–4 h (95% CI 47–103), +312 kcal over 24 h (95% CI 226–398) — [PMC7610681](https://pmc.ncbi.nlm.nih.gov/articles/PMC7610681/)
- The press release turned this into "big dippers" vs "little dippers": "9% increase in hunger … waited around half an hour less … 75 more calories … around 312 calories more over the whole day … even though they ate exactly the same meals" — [ScienceDaily / KCL release, 12 Apr 2021](https://www.sciencedaily.com/releases/2021/04/210412114802.htm); [KCL news](https://www.kcl.ac.uk/news/new-research-reveals-why-some-of-us-are-hungry-all-the-time). Trade press added that 312 kcal/day "could potentially turn into 20 lb of weight gain over a year" (an extrapolation, not a study result) — [NutritionInsight](https://www.nutritioninsight.com/news/big-dippers-overeating-caused-by-blood-sugar-drops-hours-after-eating-finds-zoe-backed-study.html)
- Weak validation in the US cohort, after adjusting for individual factors: hunger change r = −0.01 (P = 0.904), energy intake 3–4 h r = 0.23 (P = 0.055), energy intake 24 h r = 0.12 (P = 0.316); only time-to-next-meal stayed significant (r = −0.24, P = 0.038) — [PMC7610681](https://pmc.ncbi.nlm.nih.gov/articles/PMC7610681/)
- Within-person test (same person, same breakfast on two days): dips were "modestly but significantly" correlated with time to next meal (r = −0.06), intake 3–4 h (r = 0.08) and intake 24 h (r = 0.06); the hunger link was not significant (r = 0.04, P = 0.232); "none of the correlations in the smaller US validation cohort were significant" — [PMC7610681](https://pmc.ncbi.nlm.nih.gov/articles/PMC7610681/)
- Associations were strongest after the OGTT glucose drink, "which also preceded the largest dips"; for the high-carb muffin the dip was *not* associated with intake at 3–4 h (r = 0.04, P = 0.349) — [PMC7610681](https://pmc.ncbi.nlm.nih.gov/articles/PMC7610681/)
- Who dips: dips had "modest and non-significant correlations with … age, weight and BMI – except for sex, where males … had slightly larger dips"; bigger dips went with *lower* fasting insulin and C-peptide; dips correlated only weakly with the preceding glucose rise (r = 0.12) and not with the 0–2 h area under the curve (r = 0.05) — [PMC7610681](https://pmc.ncbi.nlm.nih.gov/articles/PMC7610681/)
- Authors' own limitations: no appetite hormones or clamp-measured insulin sensitivity; self-reported meal content; self-reported fasting compliance (109 meals excluded for early eating); could not see whether people compensated over weeks or months; 97% white; sleep and physical activity not included as confounders — [PMC7610681](https://pmc.ncbi.nlm.nih.gov/articles/PMC7610681/)
- Conflict of interest: funded by Zoe Global Ltd, Wellcome Trust and NIHR; "The sponsor, Zoe Global Ltd, was directly involved in study design, data collection and analysis"; five authors list Zoe Global affiliations — [PMC7610681](https://pmc.ncbi.nlm.nih.gov/articles/PMC7610681/)
- **Author correction** (Nat Metab 2021;3(7):1032, published 13 Jul 2021): "in the labels at the bottom of Fig. 2d,e, 'mins' should have read 'kcal'. In Supplementary Tables 1 and 3, mean and SD values were incorrectly transposed." Labelling and table errors only; no change to the numbers or conclusions — [Nature Metabolism correction](https://www.nature.com/articles/s42255-021-00436-1); [White Rose record](https://eprints.whiterose.ac.uk/183232/)
- An earlier conference abstract from the same data reported "1102 subjects" and the same direction of findings — [Current Developments in Nutrition, 2020](https://cdn.nutrition.org/article/S2475-2991(23)09629-4/fulltext)

**Follow-up studies, 2022–2026**
- **Yao J et al., JAMA Network Open, 2 Mar 2026** ("Postprandial Glucose Level Decreases and Appetite in Adults Without Diabetes", e263426, PMID 41885864). Independent cohort, Singapore, May 2021–Aug 2024; 895 adults without diabetes (mean age 40.1 ± 13.6; 561 [63%] female); 7,650 *free-choice* meals over 9 days; masked CGM plus smartphone hunger ratings (0–6 scale). 54% of meals were followed by a dip below baseline. Larger dips were associated with more hunger at 2–3 h (β = 0.05 per 10% decrease) and 3–4 h (β = 0.09), larger hunger increases, and eating sooner; a dip below baseline was associated with the next meal coming 27 minutes earlier (β = −27.3 min; median 380 vs 425 min). Energy intake was not measured. Authors: findings "should be interpreted with caution pending further confirmation". Funded by the Singapore Ministry of Health's NMRC, with no funder role in the analysis — [Europe PMC / PMC13022734](https://pmc.ncbi.nlm.nih.gov/articles/PMC13022734/)
- **Stutz B et al., Appetite, Jun 2024** (secondary analysis of a randomised crossover trial, 45 students: 22 early and 23 late chronotypes). Dips were smaller after medium-GI than high-GI meals. Hunger rose through the day, but "glucose dips were not related to the feeling of hunger at the meal following breakfast" (a null result in a small young sample) — [PubMed 38901765](https://pubmed.ncbi.nlm.nih.gov/38901765/); [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0195666324003726)
- ZOE PREDICT snacking paper (Bermingham 2023): 95% of the UK cohort snacked (2.28 snacks/day, 24% of daily calories); snacking after 9 pm (31% of participants) was associated with less favourable HbA1c, glucose and triglyceride responses than snacking at other times — [Eur J Nutr 2023, PMC10799113](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10799113/)
- Wider scepticism about the glucose-spike narrative in healthy people: post-meal rises of 2–3 mmol/L are normal; concern starts above ~11 mmol/L; CGMs "overestimate blood sugar levels in people without diabetes" and report a lot of variability (McGill Office for Science and Society, J. Jarry, 5 Sep 2025) — [McGill OSS](https://www.mcgill.ca/oss/article/health-and-nutrition-pseudoscience/he-sweet-embellishments-glucose-goddess)

**Does berberine act on the dip itself?**
- Berberine RCT meta-analysis (20 RCTs, n = 1,761; J Nutr 2023): fasting glucose −0.52 mmol/L, HbA1c −4.48 mmol/mol, fasting insulin −2.36 mU/L, HOMA-IR −0.85, **2-h post-meal glucose −1.81 mmol/L (4 studies, n = 501)**; reductions in fasting glucose and HOMA-IR possibly larger in women (4 women-only trials vs 1 men-only trial); larger effects in people with diabetes and in Asians; subgroup findings "remain to be replicated" — [Zhao et al., J Nutr 2023, PMID 37598753](https://jn.nutrition.org/article/S0022-3166(23)72544-3/fulltext)
- I found no trial that measured berberine's effect on the 2–3 h post-meal *dip*, on CGM glycaemic variability in people without diabetes, or on appetite as a primary outcome. The CGM search turned up only a prediabetes pilot (n = 34, 500 mg three times a day, standard glycaemic markers) — [HIMABERB pilot, PMC10483788](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10483788/). Harvard Health (2024) says there is "no rigorous scientific evidence" for appetite suppression (cited in file 02).

### Inferences
- What the copy can honestly say: "In a study of 1,070 healthy adults (King's College London and others, *Nature Metabolism* 2021), people whose blood sugar fell furthest below their starting level 2–3 hours after breakfast felt more hunger and ate *on average* about 75 kcal more in the next hours and about 312 kcal more that day — and a 2026 study of 895 adults in Singapore found the same pattern of earlier hunger." Use "were associated with" / „бяха свързани с", not "cause". Do not use the press-release extrapolation "20 lb a year".
- AD29's H2 "виновникът не е скокът. А [спадът]" is supported (dips predicted better than peaks). But the "rollercoaster" claim, that a big spike causes the crash, is only weakly supported (r = 0.12 between rise and dip). Frame the dip as its own signal, not as the spike's shadow.
- Do not link the dip to age, menopause or insulin resistance from this study. It found no age or BMI link, slightly *larger* dips in men, and dips going with *lower* fasting insulin. The "after 40" frame has to stand on other evidence (SWAN, file 02), not on PREDICT.
- The berberine bridge is an inference with a gap: berberine lowers post-meal glucose in oral trials (mostly in people with dysglycaemia), but nobody has shown it reduces dips, hunger or calorie intake. The copy should not say or imply "berberine/the patch stops the dip".
- The 2026 JAMA Network Open study is the better "news" hook: it is recent, independent, mostly women and mid-life, and based on real meals. Pair it with Wyatt rather than relying on the ZOE-sponsored paper alone.

### Gaps
- Wyatt Supplementary Table 1 (exact sex/age breakdown of the 1,070 subset) was not accessed; the 73% female / mean age 46 figures describe the UK PREDICT 1 cohort from a different paper.
- No study found on glucose dips and hunger specifically in peri- or postmenopausal women.
- No human data on transdermal berberine and glucose of any kind (same gap as file 02).

---

## 2. Are there newer, stronger or more recent "new cause" studies? Exact findings for each candidate

### Takeaway
On the science alone, the strongest causal evidence for overeating comes from ultra-processed food (Hall 2019 RCT: +508 kcal/day) and sleep (Tasali 2022 RCT: sleeping 1.2 h more → −270 kcal/day). These are randomised trials, unlike the observational dip data. But neither has any credible link to berberine or a patch. The evening-appetite evidence (circadian hunger peaks around 8 pm; late eating raises hunger) fits the avatar's "9 pm fridge" story and blends naturally with the dip. "Food noise" now has a formal definition and 2026 prevalence data showing women report it nearly twice as often as men. The cortisol/stress-eating evidence is old and small (Epel 2000/2001, 59 premenopausal women).

### Cited Findings
**Ultra-processed food (UPF)**
- Hall et al., *Cell Metabolism* 2019 (NIH inpatient RCT, crossover): 20 weight-stable adults (mean age 31, BMI 27), 2 weeks UPF vs 2 weeks unprocessed diet, matched for presented calories, energy density, macros, sugar, sodium and fibre, eaten ad libitum. Energy intake was +508 ± 106 kcal/day on UPF; participants gained 0.9 kg on UPF and lost 0.9 kg on the unprocessed diet — [PubMed 31105044 / PMC7946062](https://pmc.ncbi.nlm.nih.gov/articles/PMC7946062/)
- Dicken et al., *Nature Medicine*, 4 Aug 2025 (UPDATE trial, UK): 55 adults (BMI 25–40, habitual UPF ≥50% of kcal), two 8-week ad-libitum diets that both followed the UK Eatwell Guide; weight change −2.06% on minimally processed vs −1.05% on UPF (difference −1.01%, P = 0.024, ~1 kg); the minimally processed diet showed fewer food cravings — [Nature Medicine](https://www.nature.com/articles/s41591-025-03842-0); [UCL news](https://www.ucl.ac.uk/news/2025/aug/less-processed-diet-may-be-more-beneficial-weight-loss). Published critiques and a reply followed in *Nature Medicine* — [Concerns over conclusions](https://www.nature.com/articles/s41591-025-04087-7); [Reply](https://www.nature.com/articles/s41591-025-04089-5)

**Sleep**
- Spiegel et al., *Ann Intern Med* 2004: 12 healthy young men, 2 nights of restricted vs extended sleep: leptin −18%, ghrelin +28%, hunger +24%, appetite +23%, and appetite for calorie-dense, high-carb foods +33–45% — [PubMed 15583226](https://pubmed.ncbi.nlm.nih.gov/15583226/)
- Tasali et al., *JAMA Intern Med* 2022 (RCT, real-life setting): 80 adults aged 21–40, BMI 25–29.9, habitual sleep <6.5 h. Sleep counselling added ~1.2 h/night, and energy intake fell by ~270 kcal/day vs control (measured objectively by doubly labelled water) — [PubMed 35129580 / PMC8822469](https://pmc.ncbi.nlm.nih.gov/articles/PMC8822469/); [NIH Research Matters](https://www.nih.gov/news-events/nih-research-matters/getting-sufficient-sleep-reduces-calorie-intake)

**Evening appetite and meal timing**
- Scheer, Morris & Shea, *Obesity* 2013: 12 healthy adults on a 13-day protocol that spread meals and sleep evenly across the circadian cycle. Hunger has an internal circadian rhythm with its low point in the biological morning (~8 am) and its peak in the biological evening (~8 pm); peak-to-trough 17%; appetite for sweet, salty and starchy foods follows the same rhythm (14–25%) — [PMC3655529](https://pmc.ncbi.nlm.nih.gov/articles/PMC3655529/)
- Vujović et al., *Cell Metabolism* 2022 (randomised crossover, tightly controlled): 16 adults with overweight or obesity (5 women). The same meals shifted ~4 h later increased hunger (p < 0.0001), raised the waketime and 24-h ghrelin:leptin ratio, lowered waketime energy expenditure and 24-h core temperature, and shifted fat-tissue gene expression toward fat storage — [PubMed 36198293 / PMC10184753](https://pmc.ncbi.nlm.nih.gov/articles/PMC10184753/); [Harvard Gazette](https://news.harvard.edu/gazette/story/2022/10/study-looks-at-why-late-night-eating-increases-obesity-risk)
- ZOE PREDICT: snacking after 9 pm was associated with less favourable glycaemic and lipid markers (see §1) — [PMC10799113](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10799113/)

**"Food noise"**
- Formal definition (Dhurandhar, Allison et al., *Nutrition & Diabetes*, 8 Jul 2025): "persistent thoughts about food that are perceived by the individual as being unwanted and/or dysphoric and may cause harm … resembling rumination"; a measurement tool (RAID-FN Inventory) is under development — [Nature/N&D](https://www.nature.com/articles/s41387-025-00382-x)
- A 5-item Food Noise Questionnaire was validated (Obesity, 2025) — [Wiley](https://onlinelibrary.wiley.com/doi/full/10.1002/oby.24216)
- Prevalence (Hayashi & Masterson, *Obesity Science & Practice*, 29 Sep 2026; nationally representative survey of 1,000 US adults, May 2026): 50.9% experience food noise at least sometimes and 18% often/always. Often/always: **women 22.7% vs men 12.7%**; ages 18–29 26.5%, 45–59 15.6%, 60+ 13.5%; current GLP-1 users 25.8% vs non-users 16.3%. Loss of control over eating was the strongest correlate (~6× odds) — [News-Medical, 29 Sep 2026](https://www.news-medical.net/news/20260929/Cane28099t-stop-thinking-about-food-Youe28099re-far-from-alone.aspx)
- File 02 already covers the INFORM GLP-1 survey (constant food thoughts 62% → 16%).

**Cortisol / stress eating**
- Epel et al., *Psychosom Med* 2000: 59 healthy premenopausal women. Those with central fat (high waist-to-hip ratio) secreted more cortisol under lab stress, and lean women with central fat did not habituate to repeated stress. Cross-sectional — [PubMed 11020091](https://pubmed.ncbi.nlm.nih.gov/11020091/)
- Epel et al., *Psychoneuroendocrinology* 2001: 59 premenopausal women. High cortisol reactors ate more calories on the stress day (not on the control day) and ate more sweet food across days — [PubMed 11070333](https://pubmed.ncbi.nlm.nih.gov/11070333/)
- Expert pushback on "cortisol belly": [The Conversation, "The 'cortisol belly' myth"](https://theconversation.com/the-cortisol-belly-myth-when-diet-culture-is-rebranded-as-wellness-254362); [Healthgrades](https://resources.healthgrades.com/pro/cortisol-health-trends-misleading-patients); "Cortisol is an essential hormone, not a toxin that needs to be eliminated" (Dr A. Acquaviva) — [BakeryAndSnacks, 22 Jul 2026](https://www.bakeryandsnacks.com/Article/2026/07/22/cortisol-the-viral-trend-thats-rewriting-shopping-lists/)

**Protein leverage**
- Gosby et al., *PLoS One* 2011: 22 lean adults, three 4-day periods. Dropping protein from 15% to 10% of energy raised total energy intake by +12 ± 4.5%, mostly from savoury between-meal snacks; raising protein to 25% did not lower intake — [PMC3192127](https://pmc.ncbi.nlm.nih.gov/articles/PMC3192127/)

**Menopause / after 40**: SWAN body-composition data are already in file 02 (fat gain rate roughly doubles and lean mass declines from ~2 years before the final period). Not repeated here.

**Adherence and habit (the "mechanism of the solution" in the draft)**
- Dansinger et al., *JAMA* 2005 (RCT; 160 adults; Atkins vs Zone vs Weight Watchers vs Ornish for 1 year): weight loss was associated with self-reported adherence (r = 0.60, P < 0.001) but **not with diet type** (r = 0.07); completion rates were only 50–65% — [PubMed 15632335](https://pubmed.ncbi.nlm.nih.gov/15632335/)
- Lally et al., *Eur J Soc Psychol* 2010: median 66 days to reach maximum automaticity, range 18 to a predicted 254 days; for simple daily behaviours — [Univ. of Surrey Q&A with Dr Lally](https://www.surrey.ac.uk/news/does-it-really-take-66-days-form-habit-we-asked-expert-dr-pippa-lally); [BPS Research Digest](https://www.bps.org.uk/research-digest/how-form-habit); a 2026 explainer notes the 66 days is a median from a subset of participants — [The Behavioral Scientist](https://www.thebehavioralscientist.com/articles/how-long-to-form-a-habit)
- Newer and broader: Singh et al., *Healthcare* 2024 (systematic review and meta-analysis, 20 studies, 2,601 participants): median 59–66 days and mean 106–154 days to form a health habit, individual range 4–335 days; "morning practices and self-selected habits generally exhibit[ed] greater strength" — [PMC11641623](https://pmc.ncbi.nlm.nih.gov/articles/PMC11641623/)
- Patch vs pill adherence (closest real RCT): Audet et al., *JAMA* 2001, contraceptive patch vs pill, 1,417 women. Perfect compliance in 88.2% of cycles with the (weekly) patch vs 77.7% with the daily pill (P < .001); only 1.8% of patches fully detached; application-site reactions were more common with the patch — [PubMed 11343482](https://pubmed.ncbi.nlm.nih.gov/11343482/)
- The WHO's 2003 report *Adherence to long-term therapies* is the usual source for "~50% adherence in chronic disease in developed countries" (not re-fetched in this pass) — [WHO IRIS](https://iris.who.int/handle/10665/42682)

### Inferences
- Evidence strength for "a hidden cause of overeating" (my ranking): UPF (RCTs) ≈ sleep (RCTs) > evening circadian appetite / late eating (tight lab crossover, small n) > glucose dips (two large observational cohorts plus one small null) > food noise (definition and prevalence only; no mechanism) > cortisol (small 2000–2001 studies, contested trend) > protein leverage (small, short).
- Fit with a berberine patch runs almost the other way round: dips (berberine's strongest evidence is glucose) > evening/late eating (it can be folded into the dip story) > food noise (via cravings) > cortisol/sleep (no berberine link) > UPF/protein (none). The dip remains the best *bridge* to berberine even though it is not the strongest science.
- The adherence evidence is better than what the draft uses. Dansinger 2005 ("adherence, not diet type, predicted weight loss") is a stronger and more on-message citation than WHO's medication-adherence figure. Singh 2024's "morning habits form stronger" directly supports a morning patch ritual. Audet 2001 is the only RCT showing a patch beats a pill on adherence, but it was a *weekly* contraceptive patch, so use it as an analogy with that caveat.
- The 66-day figure should be quoted as "about two months on average, very different from person to person" (Singh 2024), not as a fixed rule.

### Gaps
- No RCT tests berberine (any route) on hunger, cravings, food noise or evening intake as a primary outcome.
- No study found on circadian evening hunger specifically in women aged 40–60.
- The full Vujović 2022 quantitative results (e.g., exact % change in hunger probability or leptin) could not be extracted; the PMC full text failed to load and the press coverage gave no numbers.

---

## 3. Which weight-loss angles are brands and advertorials using right now (2025–2026)? Saturated, rising, or burned, with search-trend data (BG and global)

### Takeaway
In Bulgaria, **кортизол** (×3.3 in five years, still at its 12-month high) and **берберин** (×13, peak Mar 2026) are the fastest-rising terms, and **инсулинова резистентност** hit a 5-year high in Mar 2026. **Кръвна захар** is the biggest and most stable term, while **менопауза** is flat and generic "отслабване", "хормони" and "метаболизъм" are falling. Globally, "food noise" is the clearest new term and "glucose goddess"-style spike content has plateaued or declined since 2023–2024. On Meta in the US, menopause is the single largest cluster of new health ads after the 22 Jul 2026 policy change, and "Endocrinologist reveals: cortisol is the reason you can't lose weight after 40" ads were live in late Sep 2026. Status: GLP-1/"natural Ozempic" = burned and red; menopause belly = saturated (US); cortisol = rising and peaking (US cooling, BG still climbing); glucose spikes = mature; glucose *dip* = under-used; food noise = rising but not yet Bulgarian; habit/adherence = used by the US patch leader but not as a new-cause story in BG.

### Cited Findings
**Google Trends, Bulgaria (5 years, weekly; pulled 3 Oct 2026)** — [Explore BG batch A](https://trends.google.com/trends/explore?date=today%205-y&geo=BG&q=%D0%BA%D1%80%D1%8A%D0%B2%D0%BD%D0%B0%20%D0%B7%D0%B0%D1%85%D0%B0%D1%80,%D0%BA%D0%BE%D1%80%D1%82%D0%B8%D0%B7%D0%BE%D0%BB,%D0%B1%D0%B5%D1%80%D0%B1%D0%B5%D1%80%D0%B8%D0%BD,%D0%B8%D0%BD%D1%81%D1%83%D0%BB%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%20%D1%80%D0%B5%D0%B7%D0%B8%D1%81%D1%82%D0%B5%D0%BD%D1%82%D0%BD%D0%BE%D1%81%D1%82,%D0%BC%D0%B5%D0%BD%D0%BE%D0%BF%D0%B0%D1%83%D0%B7%D0%B0)

| Term (batch A, same scale) | First 12m (2021–22) | Previous 12m | Last 12m (2025–26) | Last 3m | Peak week |
|---|---|---|---|---|---|
| кръвна захар | 70.9 | 65.7 | 66.9 | 65.6 | 100, Dec 2021 |
| кортизол | 13.1 | 28.6 | **43.7** | **49.2** | 75, 7–13 Jun 2026 |
| берберин | 3.3 | 33.1 | **42.9** | 40.8 | 71, 22–28 Mar 2026 |
| инсулинова резистентност | 25.8 | 40.1 | **45.7** | 47.5 | 69, 15–21 Mar 2026 |
| менопауза | 44.1 | 44.6 | 41.3 | 39.5 | 76, 1–7 Mar 2026 |

| Term (batch B, anchored on кръвна захар) | First 12m | Last 12m | Last 3m |
|---|---|---|---|
| хормони | 47.5 | 32.2 | 30.5 |
| апетит | 28.3 | 24.7 | 24.9 |
| метаболизъм | 7.0 | 1.5 | 2.5 |
| коремни мазнини | 0.3 | 0.0 | 0.1 |

| Term (batch C, on a different scale: отслабване dominates) | First 12m | Last 12m | Last 3m | Peak |
|---|---|---|---|---|
| отслабване | 75.7 | 48.9 | 44.7 | 100, Mar 2023 |
| кръвна захар | 21.2 | 20.1 | 19.8 | — |
| оземпик | 7.5 | 11.1 | 11.5 | 43, Aug 2022 |
| мунджаро | 0.0 | 10.9 | 11.9 | 16, Jul 2026 |
| глюкоза | 11.5 | 11.4 | 11.4 | — |

| Spike/dip phrasing (batch D, anchored on кръвна захар = 66.9, кортизол = 43.6 last 12m) | Last 12m |
|---|---|
| скок на кръвната захар | 0.0 |
| спад на кръвната захар | 0.2 |
| глад за сладко | 0.0 |

- BG related queries, last 12 months. **берберин**: top "берберин мнения", "берберин цена", "берберин комплекс", "берберин 500 мг", "беркол берберин" (rising +190%). **кортизол**: "висок кортизол", "изследване на кортизол", "кортизол цена", "висок кортизол симптоми". **инсулинова резистентност**: "…изследване", "…симптоми", "…диета", "хранене при…", "…лечение" — [Google Trends BG, related queries](https://trends.google.com/trends/explore?date=today%2012-m&geo=BG&q=%D0%B1%D0%B5%D1%80%D0%B1%D0%B5%D1%80%D0%B8%D0%BD)

**Google Trends, worldwide and US (5 years)**
- Worldwide (same batch): "berberine" 7.9 → 61.5 (peak 31 May–6 Jun 2026); "food noise" 1.0 → 19.6 (peak 53 in 3–9 May 2026; last 3m 11.4); "cortisol belly" 0.0 → 2.5; "menopause belly" 0.9 → 1.6; "glucose spike" 0.1 → 2.3, flat since its Feb 2024 peak — [Explore worldwide](https://trends.google.com/trends/explore?date=today%205-y&q=berberine,cortisol%20belly,menopause%20belly,food%20noise,glucose%20spike)
- US: "cortisol" 14.3 → 59.3 (peak 8–14 Mar 2026; last 3m 45.5, i.e., cooling from the peak); "berberine" 4.2 → 23.6 (peak Apr 2026); "glucose goddess" peaked Apr–May 2023 and fell from 0.7 (previous 12m) to 0.1 (last 12m); "berberine patch" and "GLP-1 patch" ≤0.5 — [Explore US](https://trends.google.com/trends/explore?date=today%205-y&geo=US&q=berberine,cortisol,glucose%20goddess,berberine%20patch,GLP-1%20patch)
- Other trend data: #cortisoldetox ~800 million TikTok views; #HowToReduceCortisol + #CortisolLevels >140 million — [BakeryAndSnacks, 22 Jul 2026](https://www.bakeryandsnacks.com/Article/2026/07/22/cortisol-the-viral-trend-thats-rewriting-shopping-lists/). Spate (Mar 2024–Feb 2025): "cortisol" searches +339.7% YoY (Google +87.4%, TikTok +422.6%); "cortisol mocktail" ~1.4M weekly TikTok views — [WWD via search summary](https://wwd.com/beauty-industry-news/wellness/cortisol-face-mocktail-supplement-tiktok-trend-1236774663/); Spate also reported PCOS searches +773% YoY — [NutraIngredients, May 2025](https://www.nutraingredients.com/Article/2025/05/05/top-supplement-trends-according-to-google-tiktok/)

**Ads running now (Meta and market)**
- Live Meta ads, 25–27 Sep 2026 (Health Insider advertorial publisher, selling a "Carnivore Cortisol Detox" programme aimed at people over 40): "Endocrinologist Reveals: Cortisol Is The Reason You Can't Lose Weight After 40"; "Endocrinologist: High Cortisol Makes You Fat — Here's How to Stop It"; "Most weight loss advice is not made for older women"; "What a Gynecologist and Neurologist Both Recommend to Older Women for Lasting Fat Loss". The same publisher runs "It's Not Anxiety, It's 'Dopamine Loop'" — [Atria ad library: Health Insider](https://www.tryatria.com/ads/meta/health-insider-ads)
- New US health ads after Meta's 22 Jul 2026 policy change (Adligator, 17 Aug 2026): menopause 134, GLP-1 77, collagen 76, weight loss 49, joint pain 15; one supplement brand launched 1,800 ads in 30 days; aggressive numeric advertorial claims ("3 weeks — 30 lbs") expected to draw claim-level strikes — [Adligator](https://adligator.com/blog/meta-health-wellness-ad-policy-update-2026)
- Women's-health supplement ad guide (29 Jul 2026): Meta consistently rejects symptom-specific claims, hormonal-intervention language ("balances hormones", "regulates estrogen") and medical framing ("clinically proven"); what runs is energy, sleep and **routine/ritual** ("My morning non-negotiable for six months now"); benefit-led creative is said to get 3–4× higher approval than symptom-led (agency claim) — [Landing Partners](https://www.landing.partners/blog/womens-health-supplement-marketing-hormonal-balance-perimenopause)
- Cortisol products: Zoyava (cortisol + myo-inositol) $7.0M of TikTok Shop sales in three months; Nello Supercalm >1M units; Veracity "Cortisol Calming" — [search summary of Glossy / WWD / Charm coverage](https://www.glossy.co/pop/glossy-pop-newsletter-wellness-brands-are-winning-on-tiktok-shop-for-now/); [Charm.io on Zoyava](https://info.charm.io/en/blog/zoyava-3-key-factors-driving-its-tiktok-supplement-sales-boom) (figures as reported in search results; pages not fetched)
- Supplement launches with menopause claims +17% globally (Apr 2021–Mar 2026); "GLP-1-friendly" positioning spreading — [NutritionInsight](https://www.nutritioninsight.com/trend-analysis/positionings/glp-1-weight-management-trends.html)
- Menopause programmes from big players: WeightWatchers menopause programme (Queen Latifah); Noom expanded into HRT — [search summary](https://www.emarketer.com/topics/category/menopause)
- Glucose Goddess backlash: the Anti-Spike supplement "has not been clinically tested"; its "40%" figure is extrapolated from single ingredients; criticism of "selling a supplement to healthy people" — [Abby Langer review](https://abbylangernutrition.com/glucose-goddess-anti-spike-review/); [TODAY](https://www.today.com/health/diet-fitness/glucose-goddess-jessie-inchauspe-blood-sugar-rcna138866)

**Bulgarian market signals**
- BG cortisol content is now mainstream and commercial: "Какво е кортизол и защо всички говорят за него през 2026 г." (Haya Labs supplement brand, 10 Jun 2026; mentions "cortisol face"/"cortisol belly", sells magnesium/ashwagandha/omega-3) — [Haya Labs](https://www.hayalabs.bg/bg/media/kakvo-e-kortizol-i-zashto-vsichki-govoryat-za-nego-prez-2026-g-id165.html); "Синдромът на „кортизоловото коремче": Защо диетите не работят, когато сте под стрес" (Nova Svetlina, 28 Apr 2026) — [Nova Svetlina](https://novasvetlina.com/blog/%D1%81%D0%B8%D0%BD%D0%B4%D1%80%D0%BE%D0%BC%D1%8A%D1%82-%D0%BD%D0%B0-%D0%BA%D0%BE%D1%80%D1%82%D0%B8%D0%B7%D0%BE%D0%BB%D0%BE%D0%B2%D0%BE%D1%82%D0%BE-%D0%BA%D0%BE%D1%80%D0%B5%D0%BC%D1%87%D0%B5/2026/04/28/); a sceptical counterpoint: "Кортизолът не е враг" — [Светът на здравето](https://svetatnazdraveto.bg/novini/kortizolat-ne-e-vrag-kakvo-sa-kortizolovija-korem-i-kortizolovoto-lice.html)
- BG berberine sellers already own the insulin-resistance and blood-sugar positioning: "Хранителна добавка за инсулинова резистентност с берберин Glucoguard-B" — [DR-D Longevity](https://dr-d.eu/bg/product/glucoguard-b-by-dr-d-longevity/); "Берберин – за кръвната захар" — [Vitagold](https://www.vitagold.bg/produkt/%D0%B1%D0%B5%D1%80%D0%B1%D0%B5%D1%80%D0%B8%D0%BD-%D0%B7%D0%B0-%D0%BA%D1%80%D1%8A%D0%B2%D0%BD%D0%B0%D1%82%D0%B0-%D0%B7%D0%B0%D1%85%D0%B0%D1%80-90-%D1%82%D0%B0%D0%B1%D0%BB%D0%B5%D1%82%D0%BA%D0%B8/); media framing "Берберин – чудодейната добавка срещу диабет и за отслабване!" — [Gotvach.bg](https://gotvach.bg/n5-85961-%D0%91%D0%B5%D1%80%D0%B1%D0%B5%D1%80%D0%B8%D0%BD_-_%D1%87%D1%83%D0%B4%D0%BE%D0%B4%D0%B5%D0%B9%D0%BD%D0%B0%D1%82%D0%B0_%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%BA%D0%B0_%D1%81%D1%80%D0%B5%D1%89%D1%83_%D0%B4%D0%B8%D0%B0%D0%B1%D0%B5%D1%82_%D0%B8_%D0%B7%D0%B0_%D0%BE%D1%82%D1%81%D0%BB%D0%B0%D0%B1%D0%B2%D0%B0%D0%BD%D0%B5!); and "Ozempic от природата" — [Spiritell](https://spiritell.com/ozempic-%D0%BE%D1%82-%D0%BF%D1%80%D0%B8%D1%80%D0%BE%D0%B4%D0%B0%D1%82%D0%B0-%D0%BC%D0%BE%D0%B3%D0%B0%D1%82-%D0%BB%D0%B8-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%BA%D0%B8%D1%82%D0%B5/)

### Inferences
Angle status board (my synthesis of the data above, plus files 02 and 03):

| Angle | Global status (2026) | Bulgaria status | Note for FitPatches |
|---|---|---|---|
| GLP-1 / "natural Ozempic" / GLP-1 patch | Burned, scam-coded, litigated | Мунджаро searches rising (0 → 10.9), Оземпик steady | Red; already used (AD23) |
| Menopause belly / "hormonal belly" | Saturated (largest new Meta health cluster in the US; hormone language rejected) | Searches flat (44 → 41) | Keep "after 40" as identification, not as the mechanism |
| Cortisol / stress belly | Rising → peaking (US peak Mar 2026, now cooling); expert backlash | **Still rising, 12-month high** (×3.3 vs 2021–22) | Hot, but weak berberine fit; already used (AD13) |
| Insulin resistance | Mature | **Rising, 5-year high (Mar 2026)**; BG berberine sellers already claim it | Familiar ground; disease-adjacent |
| Glucose spikes (Glucose Goddess) | Mature/plateau since 2023–24; critiques | Familiar to health-engaged readers (see §4) | Don't lead with "spikes" |
| **Glucose *dip* 2–3 h after eating** | Niche; ZOE's own content; new 2026 JAMA NO paper | Practically unsearched (spike/dip phrases ≈0) | Fresh twist on a familiar base |
| Food noise | Rising (world 1 → ~20), formal science 2025–26 | No Bulgarian term established | Use as language, test as hook |
| Evening cravings / late eating | Evergreen | "глад за сладко" ≈0 searches; it is a felt experience, not a search | Strong emotional hook (AD20, AD29) |
| Habit / adherence / "pills get skipped" | Used by Kind Patches; agencies push "ritual" creative | Not used as a "new cause" in BG (none found) | Best honest patch mechanism |
| Ultra-processed food | Big science news (2025) | Not a supplement angle | No product fit |
| "Slow metabolism" / metabolic age | Older ClickBank staple | "метаболизъм" searches collapsed (7.0 → 1.5) | Cold |

- The "it's not X, it's Y" + endocrinologist + "after 40" structure (Health Insider's cortisol ads) is exactly FitPatches' winning AD27 structure. The format still works in Sep 2026; the *mechanism slot* is where competitors differ (cortisol vs FitPatches' metabolism/glucose).
- The BG related queries show berberine searchers are *solution-aware shoppers* (opinions, price, dose, brand). The insulin-resistance searchers are in a *self-diagnosis/test* mindset (symptoms, testing, diet). An advertorial that explains a felt symptom (evening hunger) in plain words reaches the larger problem-aware audience these searches point to.

### Gaps
- Meta Ad Library could not be queried for Bulgaria (login/JS required; no API token). Current BG competitor advertorial angles were not verified directly; this is the most important gap for the saturation judgement.
- TikTok Creative Center data for Bulgaria was not accessible.
- Google Trends values for Bulgarian low-volume phrases ("скок/спад на кръвната захар", "глад за сладко") are at the noise floor; they show that the phrases are not search terms, not that the concepts are unknown.
- "Metabolic age" and gut/Akkermansia were not re-checked in Trends (gut is covered in file 02).

---

## 4. How familiar is "Glucose Goddess"-style glucose education in Bulgaria? Is the glucose angle fresh or familiar?

### Takeaway
Familiar, but not worn out. Inchauspé's book has been in Bulgarian since 2023 (Колибри paperback, Storytel audiobook, a public-library title). Bulgarian pharmacy, lab and clinic blogs explain the "пик–спад" cycle that drives hunger and cravings for sweets. "Кръвна захар" is a high, steady search term, and insulin resistance is at a 5-year search peak. But nobody searches the spike/dip phrasing, and no Bulgarian brand was found using the 2–3 h *dip* as a hunger cause. The base belief "blood sugar swings make you hungry" is pre-installed for health-engaged women, and the *dip* framing adds new information on top of it. In Schwartz terms, that is the ideal Stage-3/4 move: a new mechanism on a belief the reader already accepts.

### Cited Findings
- Bulgarian edition: "Глюкозната революция", Джеси Инчауспе, Колибри, 2023, paperback, 304 pp., translated by Константин Цанков — [Orange Center](https://www.orangecenter.bg/glyukoznata-revolyutsiya.html); [Ozone.bg](https://www.ozone.bg/product/glyukoznata-revolyutsiya/); [Hermes Books listing](https://hermesbooks.bg/glyukoznata-revolyutziya.html); also in a regional public library catalogue — [libdobrich](https://libdobrich.bg/glyukoznata-revolyutsia/)
- Audiobook on Storytel from 10 Aug 2023 (narrated by Кристина Ибришимова). The press said the book had first circulated in Bulgaria "from person to person" in English. The launch was paired with a Storytel podcast by Bulgarian trainer Инес Субашка ("Навикът да си здрав") — [Жената днес, 1 Aug 2023](https://www.jenatadnes.com/po-zdravi/glyukoznata-boginya-djesi-inchauspe-i-top-trenaorat-ines-subashka-razkrivat-tainite-na-dobrata-forma/); [Eva.bg, 10 Aug 2023](https://eva.bg/article/44838)
- A Bulgarian book blog reviewed it (Mar 2024) — [The Librarian's Granddaughter](https://thelibrariansgranddaughter.wordpress.com/2024/03/05/%D0%B3%D0%BB%D1%8E%D0%BA%D0%BE%D0%B7%D0%BD%D0%B0%D1%82%D0%B0-%D1%80%D0%B5%D0%B2%D0%BE%D0%BB%D1%8E%D1%86%D0%B8%D1%8F-%D0%BE%D1%82-%D0%B4%D0%B6%D0%B5%D1%81%D0%B8-%D0%B8%D0%BD%D1%87%D0%B0%D1%83%D1%81/); it also appears in a bg-mamma e-book request thread — [bg-mamma](https://www.bg-mamma.com/?topic=1562091.690)
- Bulgarian health-content language: "Цикълът „пик–спад" предизвиква усещане за умора, раздразнителност, глад и желание за още сладко" (search summary of BG pharmacy/lab blogs) — [Vitarama.bg](https://vitarama.bg/bg/kak-da-predotwratim-pikowete-na-kravnata-zahar-i-trigliceridite-sled-hranen/644/item/); [ProLab "10 неща, които карат кръвната захар да „играе""](https://prolabgd.com/blog/10-neshta-karashti-kruvnata-zahar-da-igrae/); [Apollo Hospitals BG](https://www.apollohospitals.com/bg/health-library/blood-sugar-after-eating)
- Search behaviour: "кръвна захар" is the largest stable term in the BG health batch, and "инсулинова резистентност" peaked in Mar 2026. Spike/dip phrases ≈0 (see §3 tables) — [Google Trends BG](https://trends.google.com/trends/explore?date=today%205-y&geo=BG&q=%D0%BA%D1%80%D1%8A%D0%B2%D0%BD%D0%B0%20%D0%B7%D0%B0%D1%85%D0%B0%D1%80)
- In the US, the "glucose goddess" brand peaked in 2023 and has declined since (see §3) — [Google Trends US](https://trends.google.com/trends/explore?date=today%205-y&geo=US&q=glucose%20goddess)

### Inferences
- The draft's VOC line „Ям като врабче, а в девет вечерта стоя пред хладилника" plus "the culprit isn't the spike, it's the *dip*" is a correct sophistication move. It acknowledges what the reader may already know ("you've heard about blood-sugar spikes…") and then gives her the piece she hasn't heard (the dip 2–3 hours later and its link to the next craving).
- Because FitPatches already ran 08 (кръвна захар), 18 („глад в 15:00") and 20 (вечерно хапване) to the same Meta audiences, the novelty has to come from the *new study* (2026) and the *dip* framing, not from "blood sugar" itself. Ask the owner for 08/18/20 results before scaling.
- For women 35–60 who are not health-engaged (the larger Meta audience), "кръвна захар" is familiar from GP check-ups and family diabetes. That gives the angle instant credibility but also pulls in medicated/diabetic readers. The team's own panel flagged them as wasted spend (file 06), and ANSES advises diabetics against berberine (file 04).

### Gaps
- No Bulgarian sales figure for "Глюкозната революция" and no data on Bulgarian Instagram/TikTok "glucose" creators was found.
- No Bulgarian survey on lay understanding of "кръвна захар скача/пада".

---

## 5. Ranked shortlist of angles for the next advertorial: problem mechanism, solution mechanism, strongest study, compliance, emotional pull

### Takeaway
Ranking: **(1) the sharpened "evening dip" angle**: identification with the 9 pm fridge raid, explained by the 2–3 h glucose dip plus the evening circadian appetite peak, with berberine as the studied ingredient and the morning patch as the routine. **(2) "The two-week cliff"**: adherence, not the method, is why everything failed; the safest and most patch-native angle, best run as a challenger. **(3) "Stress → evening hunger"**: cortisol as the hook only, with the mechanism routed back to the dip and routine; it rides the strongest rising BG trend but has weak berberine fit and expert backlash. **(4) "Food noise"**: as language and a test hook, not a full mechanism. **(5) "Sleep → next-day hunger"**: the best science but the weakest product fit; use as supporting proof. Scores are my judgement from the evidence above.

### Cited Findings (evidence per angle, condensed; full citations in §1–§4)
| # | Angle | Strongest real study | Science (1–5) | BG freshness (1–5) | Berberine-patch fit (1–5) | Compliance risk | Emotional pull, women 35–60 BG (1–5) |
|---|---|---|---|---|---|---|---|
| 1 | Evening dip ("вечерната въртележка") | Wyatt 2021 [PMC7610681](https://pmc.ncbi.nlm.nih.gov/articles/PMC7610681/) + Yao 2026 [PMC13022734](https://pmc.ncbi.nlm.nih.gov/articles/PMC13022734/) + Scheer 2013 [PMC3655529](https://pmc.ncbi.nlm.nih.gov/articles/PMC3655529/) + Zhao 2023 berberine PPG −1.81 mmol/L [J Nutr](https://jn.nutrition.org/article/S0022-3166(23)72544-3/fulltext) | 3 | 4 | 4 (glucose is berberine's best evidence; dip effect unproven) | **Amber** (glucose = physiological/medicinal-by-presentation risk for a patch in the EU; Meta OK if no diabetes and no "solely by wearable") | 5 |
| 2 | Two-week cliff (adherence) | Dansinger 2005 r = 0.60 adherence vs r = 0.07 diet type [PubMed](https://pubmed.ncbi.nlm.nih.gov/15632335/); Singh 2024 morning habits [PMC11641623](https://pmc.ncbi.nlm.nih.gov/articles/PMC11641623/); Audet 2001 patch 88.2% vs pill 77.7% [PubMed](https://pubmed.ncbi.nlm.nih.gov/11343482/) | 4 (for adherence) | 4 | 5 (the patch's honest mechanism) | **Green/low** (no physiological claim needed) | 4 ("Пробвала съм всичко", the AD28 winner) |
| 3 | Stress → evening hunger (cortisol as hook) | Epel 2001, 59 premenopausal women [PubMed](https://pubmed.ncbi.nlm.nih.gov/11070333/) | 2 | 4 now, likely 2 within 12 months (BG peak Jun 2026; US cooling) | 2 | Amber (hormone language often rejected; "detox" claims) | 5 |
| 4 | Food noise | Hayashi 2026 (women 22.7% vs men 12.7%) [News-Medical](https://www.news-medical.net/news/20260929/Cane28099t-stop-thinking-about-food-Youe28099re-far-from-alone.aspx); Dhurandhar 2025 [N&D](https://www.nature.com/articles/s41387-025-00382-x) | 2 (definition/prevalence only) | 5 (new in BG) but needs explaining | 3 (cravings via GLP-1 theory; no RCT) | Amber-low (satiety is the safer zone in the US; still physiological in the EU) | 4 |
| 5 | Sleep → next-day hunger | Tasali 2022, −270 kcal/day [PMC8822469](https://pmc.ncbi.nlm.nih.gov/articles/PMC8822469/); Spiegel 2004 [PubMed](https://pubmed.ncbi.nlm.nih.gov/15583226/) | 5 | 3 (AD14 already run) | 1 | Low | 4 (menopausal sleep problems) |
| — | Not recommended as the main angle: UPF (Hall 2019, +508 kcal/day [PMC7946062](https://pmc.ncbi.nlm.nih.gov/articles/PMC7946062/)): no product fit. Menopause-hormone mechanism: saturated, hormone language rejected [Landing Partners](https://www.landing.partners/blog/womens-health-supplement-marketing-hormonal-balance-perimenopause). GLP-1: red. Protein leverage (Gosby 2011 [PMC3192127](https://pmc.ncbi.nlm.nih.gov/articles/PMC3192127/)): no fit. | | | | | | |

### Inferences
**Angle 1: "Вечерната въртележка" (sharpened glucose dip). RECOMMENDED MAIN ANGLE**
- Mechanism of the problem: „Не е липса на воля. Учените откриха, че при много хора 2–3 часа след хранене кръвната захар пада *под* нивото отпреди храненето — и точно тогава гладът се връща по-рано и по-силно. Вечер биологичният часовник и без това усилва апетита за сладко и тестени, затова „пробивът" идва в 21:00, а не в 11:00." (*Not willpower: in many people blood sugar drops below its pre-meal level 2–3 h after eating, which was associated with earlier, stronger hunger; in the evening the body clock already raises appetite for sweet and starchy food, which is why the raid happens at 9 pm.*)
- Mechanism of the solution (honestly supportable): „Решението не е още по-малко храна, а по-равен ритъм: хранене, което не завършва с рязък спад (белтък и фибри първо, без сладки напитки сами по себе си), и всекидневна сутрешна рутина, която не зависи от силата на волята вечер. Берберинът е една от най-изследваните растителни съставки за метаболизма на глюкозата (в проучвания с капсули); лепенката е начинът да не пропуснете нито ден." (*An even eating rhythm plus a morning routine that doesn't depend on evening willpower; berberine is among the most-studied plant compounds for glucose metabolism (in capsule studies); the patch is how you don't skip a day.*)
- Why the solution side must stay this modest: the largest dips followed the pure glucose drink, and medium-GI meals produced smaller dips (Stutz 2024), so "what you pair your food with" is a defensible lever. There is **no evidence** that berberine or any patch prevents dips. Saying so would be an unsupported physiological claim and, per file 04, makes the patch a medicinal product "by presentation".
- Citation package: Wyatt 2021 (with "healthy adults, association" wording) → **Yao 2026 as the "new study"** → Scheer 2013 for "why 9 pm" → Zhao 2023 for berberine (oral, mostly dysglycaemic populations; never transferred to the patch).
- Emotional pull: very high. The evening fridge moment is private shame, so exonerating it ("it's a signal, not a character flaw") is the payoff. It fits the VOC hook format of the AD27/AD28 winners.
- Compliance (amber): no "контролира/регулира кръвната захар", no "за диабетици", no glucose-meter imagery or numbers attached to the product, no "results from the patch alone". Glucose science sits in the editorial, attributed to the studies; product claims are limited to routine and convenience. File 04's guidance ("Talk about routine and energy without mechanisms") applies to the product sentences.

**Angle 2: "Двуседмичната пропаст" (adherence as the new cause). RECOMMENDED CHALLENGER**
- Mechanism of the problem: „Не грешите метода — всички диети „работят", докато ги спазвате. Голямо проучване сравни четири популярни диети: резултатът зависеше от това колко дълго хората ги спазват, а не от вида на диетата. Повечето спират около втората седмица." (*Weight loss tracked adherence, r = 0.60, not diet type, r = 0.07; completion was only 50–65%.* The "second week" is a narrative device: no study gives a "week 2" drop-off number, so phrase it as experience, not data.)
- Mechanism of the solution: „Навикът се изгражда средно за около два месеца, а сутрешните навици се затвърждават най-лесно. Една лепенка сутрин е най-малкото възможно действие: не се гълта, не се помни три пъти на ден, не зависи от вечерното настроение." (*Singh 2024: ~59–66 days median, morning habits stronger; Audet 2001: the patch beat the pill on perfect adherence, 88.2% vs 77.7%, as an analogy with the weekly-patch caveat.*)
- Strength: the only angle where the patch itself is the honest mechanism. It needs no glucose or appetite claim, so compliance risk is lowest. It also directly answers the "tried everything" objection from AD28.
- Weakness: less "biological discovery" excitement, and the reader still needs a reason to believe berberine is the right "what". Borrow one paragraph of Angle 1 (berberine and glucose, oral studies).

**Angle 3: "Стресът, който яде вместо вас" (cortisol as the hook only)**
- Mechanism of the problem: „В стресиран ден жените, които реагират със силен кортизолов отговор, изяждат повече — и посягат към сладкото. Затова гладът вечер след тежък ден не е слабост." (Epel 2001)
- Mechanism of the solution: route back to Angle 1 and 2 (a steady eating rhythm and a morning routine "не зависят от това какъв ден сте имали"). **Do not claim that berberine or the patch lowers cortisol**: there is no human evidence, and "balances hormones" language is rejected on Meta.
- Use: as a Meta ad hook and headline variant feeding the Angle 1 advertorial, while BG interest is still climbing. The US pattern (peak Mar 2026, cooling by autumn) suggests the window in BG may be months, not years.

**Angle 4: "Шумът в главата за храна" (food noise)**
- Mechanism of the problem: „Почти всяка пета възрастна жена признава, че мисли за храна „често или постоянно" — учените вече имат име за това: „шум от храна"." (Hayashi 2026: 22.7% of US women report it often/always; a US statistic, so state the country.)
- Mechanism of the solution: same as Angle 1. Food noise is the *symptom vocabulary*, the dip is the *cause*.
- Use: as language inside Angle 1 and as one test hook. A Bulgarian equivalent is not established, so the term must be explained in one line.

**Angle 5: "Недоспиването прави утрешния ден по-гладен" (sleep)**
- Strongest RCT evidence (Tasali: +1.2 h sleep → −270 kcal/day), but nothing connects berberine or a patch to sleep. Use one paragraph of it as supporting proof that "hunger is biology, not character", not as the advertorial's mechanism.

### Gaps
- No A/B or performance data exists in the repo for any FitPatches angle (file 06), so these rankings are evidence- and market-based, not performance-based.
- No evidence on how Bulgarian women aged 35–60 react to cortisol vs blood-sugar language specifically; a cheap Meta hook test (same advertorial, three ad hooks: dip / two-week cliff / stress) would settle it.
- FitPatches' per-patch berberine dose and any lab/CoA data remain unknown (same gap as file 02).

---

## 6. Final verdict: keep, sharpen, or switch the "glucose dip" angle?

### Takeaway
**Keep it, but sharpen it.** No other candidate scores as well across novelty in Bulgaria, emotional pull for women 35–60 and fit with berberine at the same time. The other options are either stronger science with no product fit (sleep, UPF) or hotter trends with weak fit and fading credibility (cortisol). But the current draft over-relies on one ZOE-sponsored observational study, attaches an unsupported causal chain (dip → patch prevents it), and uses the weaker adherence citations. Sharpen it with six changes, and run Angle 2 (adherence) and a cortisol-hook variant as challengers.

### Cited Findings
- The draft's numbers match the paper (Q4 vs Q1: +9% hunger, +75 kcal at 3–4 h, +312 kcal over 24 h, 24 min sooner); the 2021 correction only fixed figure labels and supplementary tables — [PMC7610681](https://pmc.ncbi.nlm.nih.gov/articles/PMC7610681/); [Correction](https://www.nature.com/articles/s42255-021-00436-1)
- The associations are correlational and weak (r 0.16–0.27; within-person r 0.06–0.08), US validation hunger was not significant, and ZOE was directly involved in the analysis — [PMC7610681](https://pmc.ncbi.nlm.nih.gov/articles/PMC7610681/)
- The independent 2026 replication (895 adults, 63% women) supports the hunger and timing link but did not measure calories — [PMC13022734](https://pmc.ncbi.nlm.nih.gov/articles/PMC13022734/); one small null study — [PubMed 38901765](https://pubmed.ncbi.nlm.nih.gov/38901765/)
- Dips were not associated with age or BMI, were slightly larger in men, and were only weakly tied to the preceding spike — [PMC7610681](https://pmc.ncbi.nlm.nih.gov/articles/PMC7610681/)
- Berberine lowers 2-h post-meal glucose in oral RCTs (−1.81 mmol/L), with possibly larger effects in women; no data on dips or appetite — [J Nutr 2023](https://jn.nutrition.org/article/S0022-3166(23)72544-3/fulltext)
- BG: spike/dip phrasing is not searched, while "кръвна захар" and insulin resistance are big and rising; the Glucose Revolution book has been in BG since 2023 — §3–§4 sources
- Compliance: berberine has no authorised EU claim; a patch is not a food, and blood-sugar claims carry high EU risk; Meta bans diabetes cure claims and "results solely by wearable products" — `04_compliance_policy.md`; [Meta H&W policy](https://transparency.meta.com/policies/ad-standards/restricted-goods-services/health-wellness/)

### Inferences
Six sharpening changes for AD29 or its successor:
1. **Lead the science with the 2026 study, then 2021.** „Ново проучване от 2026 г. (JAMA Network Open) с 895 възрастни, повечето жени, потвърди наблюдение на учени от King's College London (Nature Metabolism, 2021) върху 1 070 души без диабет…" This adds recency, independence and the right demographic.
2. **Use associative verbs and correct scope.** „бяха свързани с", „средно", „здрави хора без диабет". Drop any yearly-kg extrapolation, and never imply the study tested berberine or patches.
3. **Decouple the dip from age and insulin resistance.** The study found no age link. Keep "after 40" as identification (SWAN, file 02) and the dip as the hunger mechanism, without claiming one causes the other.
4. **Add the "why 9 pm" proof.** Scheer 2013 (the body clock raises hunger and sweet/starchy appetite in the evening, ~8 pm peak) turns a vague dip story into the avatar's exact moment. Optionally add one Vujović line (late eating ↑ hunger hormones).
5. **Replace the solution chain with an honest one.** (a) Eating rhythm that blunts dips: protein and fibre first; avoid sugary drinks on their own, which produced the largest dips. (b) Berberine as "one of the most-studied plant compounds for glucose metabolism *in capsule studies*". (c) The patch as the consistency mechanism. Remove any "the patch stops the dip/stabilises blood sugar" wording (EU medicinal-by-presentation risk; zero evidence).
6. **Upgrade the adherence evidence.** Swap or add Dansinger 2005 (adherence, not diet type, predicted weight loss), Singh 2024 (≈2 months, morning habits stronger) and Audet 2001 (patch 88% vs pill 78% perfect adherence; contraceptive weekly patch, stated as an analogy). Keep WHO's ~50% figure only as context about medicines.

Test plan implication (an inference, not data): keep one advertorial body (Angle 1 with the Angle 2 solution section, as AD29 already partly does in „Четирите условия…" and „Защо капсулите … остават в чекмеджето"). Test three Meta hooks into it: (a) VOC evening fridge, (b) "Пробвала съм всичко → it's not the method, it's week two", (c) "Стрес → вечерен глад". Build the Angle 2 standalone advertorial next only if hook (b) wins.

Why not switch: cortisol has momentum in BG, but it would put FitPatches into the same mechanism slot as US "cortisol detox" funnels and BG adaptogen brands. Berberine has no credible cortisol story, and expert backlash is already mainstream. Sleep and UPF are better science but would make the product look bolted-on. Menopause-hormone and GLP-1 mechanisms are saturated, red, or both.

### Gaps
- Without AD08/AD18/AD20 performance data, it cannot be ruled out that the glucose family has already underperformed with this audience. Request those numbers from the owner before committing spend.
- EFSA's final berberine opinion (expected early 2027, file 04) could change every berberine-led angle; this is not angle-specific but affects all five.
- No direct test of Bulgarian readers' comprehension of the "dip below baseline" concept; one simple visual (a curve dipping below the starting line, as in AD29's SVG) is assumed, not verified, to carry it.
