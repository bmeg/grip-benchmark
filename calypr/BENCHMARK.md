## Pebble

```
Benchmark Start  2025-06-19 15:14:54.953631
Loaded: META/DocumentReference.ndjson in 23.74 seconds
Loaded: META/Specimen.ndjson in 4.91 seconds
Loaded: META/Medication.ndjson in 0.27 seconds
Loaded: META/Observation.ndjson in 126.70 seconds
Loaded: META/ResearchStudy.ndjson in 0.78 seconds
Loaded: META/SubstanceDefinition.ndjson in 0.27 seconds
Loaded: META/Condition.ndjson in 18.97 seconds
Loaded: META/ResearchSubject.ndjson in 13.93 seconds
Loaded: META/Group.ndjson in 17.23 seconds
Loaded: META/MedicationAdministration.ndjson in 14.75 seconds
Loaded: META/Patient.ndjson in 0.34 seconds
Loaded: META/Substance.ndjson in 0.22 seconds
Loaded Test data in 222.10 seconds

query 0: #################################################################################
Successfully queried 427193 rows in 38.48 seconds
query 1: #################################################################################
Successfully queried 214841 rows in 38.07 seconds
query 2: #################################################################################
Successfully queried 85433 rows in 40.92 seconds
query 3: #################################################################################
Successfully queried 80 rows in 31.79 seconds
query 4: #################################################################################
Successfully queried 10000 rows in 7.81 seconds
query 5: #################################################################################
Successfully queried 12157 rows in 31.67 seconds
query 6: #################################################################################
Successfully queried 6789 rows in 41.22 seconds
query 7: #################################################################################
Successfully queried 10000 rows in 2.73 seconds
query 8: #################################################################################
Successfully queried 0 rows in 29.58 seconds
Total Benchmark Time:  484.36
```

## Grids -- Latest

```
Benchmark Start  2025-07-06 13:44:30.287741
Loaded: META/DocumentReference.ndjson in 24.18 seconds
Loaded: META/Specimen.ndjson in 2.97 seconds
Loaded: META/Medication.ndjson in 0.28 seconds
Loaded: META/Observation.ndjson in 122.66 seconds
Loaded: META/ResearchStudy.ndjson in 0.75 seconds
Loaded: META/SubstanceDefinition.ndjson in 0.26 seconds
Loaded: META/Condition.ndjson in 8.66 seconds
Loaded: META/ResearchSubject.ndjson in 6.04 seconds
Loaded: META/Group.ndjson in 12.35 seconds
Loaded: META/MedicationAdministration.ndjson in 6.61 seconds
Loaded: META/Patient.ndjson in 1.09 seconds
Loaded: META/Substance.ndjson in 0.31 seconds
Loaded Test data in 186.15 seconds
```

query 0: #################################################################################
Successfully queried 427193 rows in 1.46 seconds
query 1: #################################################################################
Successfully queried 214841 rows in 37.06 seconds
query 2: #################################################################################
Successfully queried 85433 rows in 43.47 seconds
query 3: #################################################################################
Successfully queried 80 rows in 27.68 seconds
query 4: #################################################################################
Successfully queried 10000 rows in 30.28 seconds
query 5: #################################################################################
Successfully queried 12157 rows in 33.79 seconds
query 6: #################################################################################
Successfully queried 6789 rows in 47.49 seconds
query 7: #################################################################################
Successfully queried 10000 rows in 183.67 seconds
query 8: #################################################################################
Successfully queried 0 rows in 31.17 seconds
Total Benchmark Time: 622.22 seconds

## Badger

```
Benchmark Start  2025-06-19 15:24:06.398163
Loaded: META/DocumentReference.ndjson in 21.45 seconds
Loaded: META/Specimen.ndjson in 0.87 seconds
Loaded: META/Medication.ndjson in 0.22 seconds
Loaded: META/Observation.ndjson in 103.68 seconds
Loaded: META/ResearchStudy.ndjson in 0.36 seconds
Loaded: META/SubstanceDefinition.ndjson in 0.23 seconds
Loaded: META/Condition.ndjson in 0.54 seconds
Loaded: META/ResearchSubject.ndjson in 0.36 seconds
Loaded: META/Group.ndjson in 2.62 seconds
Loaded: META/MedicationAdministration.ndjson in 0.31 seconds
Loaded: META/Patient.ndjson in 0.28 seconds
Loaded: META/Substance.ndjson in 0.26 seconds
Loaded Test data in 131.20 seconds

query 0: #################################################################################
Successfully queried 427193 rows in 35.08 seconds
query 1: #################################################################################
Successfully queried 214841 rows in 36.96 seconds
query 2: #################################################################################
Successfully queried 85433 rows in 35.69 seconds
query 3: #################################################################################
Successfully queried 80 rows in 29.49 seconds
query 4: #################################################################################
Successfully queried 10000 rows in 7.16 seconds
query 5: #################################################################################
Successfully queried 12157 rows in 29.60 seconds
query 6: #################################################################################
Successfully queried 6789 rows in 40.72 seconds
query 7: #################################################################################
Successfully queried 10000 rows in 1.66 seconds
query 8: #################################################################################
Successfully queried 0 rows in 29.49 seconds
Total Benchmark Time:  377.03
```

## Mongo

```
(venv) peterkor@RNB11238 calypr % python test.py
Benchmark Start  2025-06-19 15:33:06.529480



Loaded: META/DocumentReference.ndjson in 20.80 seconds
Loaded: META/Specimen.ndjson in 1.58 seconds
Loaded: META/Medication.ndjson in 0.29 seconds
Loaded: META/Observation.ndjson in 110.59 seconds
Loaded: META/ResearchStudy.ndjson in 0.48 seconds
Loaded: META/SubstanceDefinition.ndjson in 0.25 seconds
Loaded: META/Condition.ndjson in 0.63 seconds
Loaded: META/ResearchSubject.ndjson in 0.65 seconds
Loaded: META/Group.ndjson in 7.94 seconds
Loaded: META/MedicationAdministration.ndjson in 0.36 seconds
Loaded: META/Patient.ndjson in 0.34 seconds
Loaded: META/Substance.ndjson in 0.25 seconds
Loaded Test data in 144.16 seconds

query 0: #################################################################################
Successfully queried 427193 rows in 0.82 seconds
query 1: #################################################################################
Successfully queried 214841 rows in 41.50 seconds
query 2: #################################################################################
Successfully queried 85433 rows in 10.85 seconds
query 3: #################################################################################
Successfully queried 0 rows in 1.60 seconds
query 4: #################################################################################
Successfully queried 10000 rows in 4.42 seconds
query 5: #################################################################################

Interrupted Mongodb and got output result:   11347 rows in 3065.68 seconds
Docker container @ 100% cpu 2.46GB memory usage.
```

## grids -- No recent PRs -- 2 month old develop branch

```
(venv) peterkor@RNB11238 calypr % python test.py
Benchmark Start  2025-06-19 16:06:35.584024
Loaded: META/DocumentReference.ndjson in 23.19 seconds
Loaded: META/Specimen.ndjson in 3.39 seconds
Loaded: META/Medication.ndjson in 2.18 seconds
Loaded: META/Observation.ndjson in 112.92 seconds
Loaded: META/ResearchStudy.ndjson in 0.45 seconds
Loaded: META/SubstanceDefinition.ndjson in 0.27 seconds
Loaded: META/Condition.ndjson in 5.68 seconds
Loaded: META/ResearchSubject.ndjson in 5.88 seconds
Loaded: META/Group.ndjson in 12.80 seconds
Loaded: META/MedicationAdministration.ndjson in 4.95 seconds
Loaded: META/Patient.ndjson in 2.55 seconds
Loaded: META/Substance.ndjson in 0.33 seconds
Loaded Test data in 174.59 seconds

query 0: #################################################################################
Successfully queried 427193 rows in 12.71 seconds
query 1: #################################################################################
Successfully queried 213530 rows in 84.17 seconds
query 2: #################################################################################
Successfully queried 85433 rows in 58.80 seconds
query 3: #################################################################################
Successfully queried 80 rows in 77.66 seconds
query 4: #################################################################################
Successfully queried 10000 rows in 79.29 seconds
query 5: #################################################################################
Successfully queried 10000 rows in 77.11 seconds
query 6: #################################################################################
Successfully queried 0 rows in 72.24 seconds
query 7: #################################################################################
Successfully queried 0 rows in 169.77 seconds
query 8: #################################################################################
Successfully queried 0 rows in 71.55 seconds
Total Benchmark Time:  877.90

```

## Postgres

```
postgres:10.4 1 core ~2GB RAM

(venv) peterkor@RNB11238 calypr % python test.py
Benchmark Start  2025-06-20 08:15:09.377177
Loaded: META/DocumentReference.ndjson in 237.99 seconds
Loaded: META/Specimen.ndjson in 16.89 seconds
Loaded: META/Medication.ndjson in 0.34 seconds
Loaded: META/Observation.ndjson in 304.22 seconds
Loaded: META/ResearchStudy.ndjson in 0.69 seconds
Loaded: META/SubstanceDefinition.ndjson in 0.29 seconds
Loaded: META/Condition.ndjson in 4.11 seconds
Loaded: META/ResearchSubject.ndjson in 4.67 seconds
Loaded: META/Group.ndjson in 89.55 seconds
Loaded: META/MedicationAdministration.ndjson in 1.63 seconds
Loaded: META/Patient.ndjson in 1.50 seconds
Loaded: META/Substance.ndjson in 0.29 seconds
Loaded Test data in 662.17 seconds

query 0: #################################################################################
Successfully queried 427193 rows in 0.37 seconds
query 1: #################################################################################
Successfully queried 214841 rows in 37.77 seconds
query 2: #################################################################################
Successfully queried 85433 rows in 20.96 seconds
query 3: #################################################################################
Successfully queried 80 rows in 18.64 seconds
query 4: #################################################################################
Successfully queried 10000 rows in 5.23 seconds
query 5: #################################################################################
Successfully queried 12157 rows in 82.14 seconds
query 6: #################################################################################
Successfully queried 6789 rows in 34.33 seconds
query 7: #################################################################################
Successfully queried 10000 rows in 3.57 seconds
query 8: #################################################################################
Successfully queried 0 rows in 17.70 seconds
Total Benchmark Time:  882.89
```

## Sqlite

Gave it 20 minutes to get through the first write command, "Loaded: META/DocumentReference.ndjson in 237.99 seconds"
but it didn't finish in 20 minutes so I suspended the test
