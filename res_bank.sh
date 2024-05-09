python odoo_import_thread.py -c conf\connection.conf --file=res.bank.csv --model=res.bank --encoding=utf-8 --worker=2 --size=20 --groupby= --ignore= --sep=";" --context="{'tracking_disable': True}"
python odoo_import_thread.py -c conf\connection.conf --fail --file=res.bank.csv --model=res.bank --encoding=utf-8 --ignore= --sep=";" --context="{'tracking_disable': True}"
