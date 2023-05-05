sudo dnf install postgresql
psql -U username -d disks-db -a -f init.sql
python DiscGolf-DataBase.py