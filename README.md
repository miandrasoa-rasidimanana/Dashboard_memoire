# Résultats de l'enquête — Agilité asynchrone

Dashboard interactif présentant les résultats de l'enquête empirique réalisée dans le cadre d'un **Consulting Project (M2)** sur l'agilité asynchrone dans les équipes distantes.

**Accès en ligne :** [Voir le dashboard →](https://miandrasoa-rasidimanana.github.io/Dashboard_memoire/)

---

## Contenu

| Fichier | Description |
|---|---|
| `index.html` | Dashboard interactif auto-contenu (données embarquées, aucune dépendance serveur) |
| `data/survey_responses_16_06_2026.csv` | Export brut des réponses au formulaire Google Forms (n=48 répondants valides, bilingue FR/EN) |
| `data/parse_survey.py` | Script Python de parsing et calcul des scores composites (AAI, Bien-être, Performance, Inclusion, CC) |

---

## Hypothèses de recherche

| # | Énoncé | Verdict |
|---|---|---|
| **H1** | Les pratiques async (AAI ↑) sont positivement associées au bien-être (WB) et à la performance (Perf) | ✓ Partiellement confirmée — mécanisme : charge de réunions (r = −0,51, p < 0,001) |
| **H2** | Les pratiques async sont positivement associées à l'inclusion (Inc) et l'équité perçues | ✗ Non confirmée (r = 0,11, ns) |
| **H3** | Les équipes Hybrides diffèrent des Synchrone-first sur les scores composites | — Non testable (0 répondant async-first) |

---

## Données

- **N = 48** répondants valides (1 exclu : non éligible — test pilote)
- Enquête bilingue FR/EN distribuée en juin 2026
- Secteurs : Tech (63 %), Banque-Assurance (17 %), Conseil (13 %), autres
- Modes : Hybride (69 %), Synchrone-first (31 %), Asynchrone-first (0 %)

### Scores composites (échelle 1–5)

| Score | Signification | Items | Inversions |
|---|---|---|---|
| AAI | Adoption des pratiques asynchrones | 6 | aucune |
| Perf | Performance perçue | 5 | aucune |
| CC | Clarté & Collaboration | 4 | CC3 (6 − valeur) |
| WB | Bien-être au travail | 8 | WB1, WB2, WB7 (6 − valeur) |
| Inc | Inclusion perçue | 9 | aucune |

---

## Sections du dashboard

| Section | Contenu |
|---|---|
| 🎯 Synthèse | Verdicts H1/H2/H3, corrélations-clés, guide de navigation |
| 👥 Profil échantillon | Composition par mode, secteur, rôle, ancienneté (Figure 1) |
| 🗓️ Charge de réunions | Distribution, nuisibilité perçue, impact sur les scores |
| 📈 Distributions | Histogrammes des 5 scores par mode |
| 🔵 H1 — Async & Performance | Scatters AAI × WB/Perf, % réunions × WB/Perf (Figures 2 & 4) |
| 🔷 H2 — Async & Inclusion | AAI × Inclusion, scores par mode |
| 🟢 H3 — Comparaisons | Radar, scores par secteur/rôle/ancienneté |
| 🔗 Matrice corrélations | Heatmap Pearson, corrélations classées (Figure 3), nuages de points |
| 📋 Tableaux comparatifs | Moyennes par mode, rôle et secteur |

---

## Déploiement

Le dashboard est un fichier HTML statique auto-contenu. Il peut être ouvert directement dans un navigateur ou hébergé via **GitHub Pages** :

1. Aller dans **Settings → Pages** du repo GitHub
2. Source : `main` branch, dossier `/` (root)
3. Le dashboard sera accessible à `https://<username>.github.io/<repo-name>/`

---

## Contexte académique

- **Auteur :** Miandrasoa Fitiavana RASIDIMANANA
- **Titre visé :** RNCP 35284 — Expert en Management des Systèmes d'Information
- **Année universitaire :** 2025-2026
- **Problématique :** *Dans quelle mesure l'agilité asynchrone peut-elle améliorer la collaboration, la performance et le bien-être des équipes distantes tout en renforçant leur inclusivité et diversité ?*
