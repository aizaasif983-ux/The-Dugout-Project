# The Dugout — Deliverable 1

**Student:** Aiza (confirm full name before submitting)  
**Batch:** LiveX Nano Degree, Batch 3  
**Course:** Advanced Python for AI, Week 1

## Overview
This project loads 142 PSL 2026 players from CSV, models players and fantasy teams with Python classes, checks league rules, and ranks teams by credits. It completes Part A and the B1–B4 programming tasks.

## Run
Install Python 3, then from the repository root run:

```bash
python main.py
```

No third-party packages required.

## Example output
```
Player pool: 142 players
Summary: 2 legal, 6 illegal out of 8 teams
LEAGUE TABLE (cheapest first)
```

## Files
- `dugout/models.py`: Player, FantasyTeam, League
- `dugout/rules.py`: league limits, five original checks, duplicate check (B1)
- `dugout/loader.py`: CSV loaders
- `data/players.csv`: 142 player records
- `data/sample_teams.csv`: 6 class teams and 2 deliberately invalid teams (B2)
- `data/my_team.csv`: example XI for now; replace with the **exact XI from your submitted form** (B3)
- `main.py`: output, rule checks, and cheapest-first league table (B4)

## Important before submission
1. Replace `data/my_team.csv` with the XI you submitted on the class form. The current Aiza XI is a **provisional example**, not verified as your actual submission. Ensure your final XI is legal.
2. Confirm your name in this README and your team owner name.
3. Create a **public GitHub repository** and make at least **8 genuine commits over at least 2 different days** with meaningful messages. This ZIP does not and cannot establish that history.
4. Push, clone the public repo into a fresh folder, run `python main.py`, and submit the repository URL via LiveX by Friday, 20 November 2026 at 11:59 pm PKT.
5. Be ready to explain selected lines of code at the demonstration.
