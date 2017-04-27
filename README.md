# vademecum-export
Web scraper to export drug data into CSV files.

This program scans the [Vademecum.es](http://vademecum.es) website to obtain a list of all the drugs.

If you don't want to run the program by yourself, you [can check the drug list file here](https://github.com/jvilaplana/vademecum-export/blob/master/results/vademecum.csv).

The resulting CSV file stores the drug name, the national code (Código Nacional) and the URL to access the drug data from vademecum.es.

Sample of the CSV file data:

| `National Code` | `Name` | `URL` |
| ------------- | ---- | --- |
| 614537 | A.A.S. Comp. 100 mg | http://vademecum.es/medicamento-a.a.s._ficha_1 |
| 686580 | A.A.S. Comp. 100 mg | http://vademecum.es/medicamento-a.a.s._ficha_1 |
| 614560 | A.A.S. Comp. 500 mg | http://vademecum.es/medicamento-a.a.s._ficha_2 |
| 672905 | A.A.S. Comp. 500 mg | http://vademecum.es/medicamento-a.a.s._ficha_2 |
| 712249 | ABACAVIR/LAMIVUDINA MYLAN Comp. recub. con película 600 mg/300 mg | http://vademecum.es/medicamento-abacavir%2Flamivudina+mylan_45299 |

## Requirements
To run this program the following software is required:
- git
- python 2.7
- pip
- virtualenv (recommended)

## Install
To install this program in your computer run the following commands in your terminal:
```
git clone https://github.com/jvilaplana/vademecum-export.git
cd vademecum-export
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
```
Now the program should be ready to be executed.

## Run
To execute the program run the following commands in your terminal:
```
source venv/bin/activate
python vademecum_export.py
```
If the executing is successful, you should see something like:
```
$ python vademecum_export.py

Going for letter a
	Getting drug 614537 (a-1)
	Getting drug 686580 (a-1)
	Getting drug 614560 (a-2)
	Getting drug 672905 (a-2)
	Getting drug 712249 (a-3)
  ...
```

## Analyze results
To check how many drugs were successfully retrieved run:
```
cd results/
find . -name 'vademecum-*' | xargs wc -l
```

To combine all the CSV files into a single one run:
```
cd results/
cat vademecum-* > vademecum.csv
```
