# Lead Scoring Web Agent – Demo

This repository demonstrates a simple, reproducible pipeline for identifying and ranking high-intent leads for 3D in-vitro models in drug discovery and safety assessment.

## Objective
The goal is to convert identified professional profiles into a prioritized list of leads using a weighted propensity-to-buy scoring framework.

## Workflow
The demo follows three stages:
1. Identification – sample input profiles
2. Enrichment – contextual business and scientific signals
3. Ranking – weighted scoring and prioritization

## Scoring Logic
Each lead is scored on a scale of 0–100 using:
- Role Fit (Toxicology / Safety roles): +30
- Company Funding (Series A/B or Public): +20
- Scientific Intent (recent relevant publication): +40
- Location in Life Sciences Hub: +10

## Files
- sample_input.csv – sample lead data
- scoring.py – scoring logic
- output.csv – ranked lead output

This demo focuses on clarity and reproducibility rather than production-scale ingestion.
