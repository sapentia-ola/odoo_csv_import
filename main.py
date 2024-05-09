import os
import subprocess

def main():
    # Configuration options
    config_options = [
        "-c",
    "connection.conf",
   "--file=res.bank.csv",
    "--model=res.bank",
    "--encoding=utf-8",
    "--worker=2",
    "--size=4",
    "--groupby=",
    "--ignore=",
     "--sep=';'",
    "--context=\"{'tracking_disable': True}\""
    ]

    config_fail_options = [
        "-c",
        "connection.conf",
        "--fail",
        "--file=res.bank.csv",
        "--model=res.bank",
        "-encoding=utf-8",
        "--ignore=",
         "--sep=';'",
        "--context=\"{'tracking_disable': True}\""
    ]

    # Construct the command to run
    command = ["python", "odoo_import_thread.py"] + config_options
    command_fail = ["python", "odoo_import_thread.py"] + config_fail_options
    
    # Run the command
    subprocess.run(command)
    subprocess.run(command_fail)

if __name__ == "__main__":
    main()
