# -*- coding: utf-8 -"*-
"""
Simple loop, run the data pull to grab TorNet's dataset, which
is split by year and can be fetched using zenodo_get.
"""

import subprocess

ZENODO_INDICES = [
    ("2013", "12636522"),
    ("2014", "12637032"),
    ("2015", "12655151"),
    ("2016", "12655179"), 
    ("2017", "12655183"), 
    ("2018", "12655187"),
    ("2019", "12655716"),
    ("2020", "12655717"),
    ("2021", "12655718"),
    ("2022", "12655719")
    ]

def pull_data_from_zenodo(out_folder=""):
    subprocess.check_call("pip3 install zenodo_get", shell=True)
    for tup in ZENODO_INDICES:
        subprocess.check_call("zenodo_get {i}".format(i = tup[1]), shell=True, 
                              encoding="utf-8")
        untar_cmd = "tar -xvzf tornet_{year}.tar.gz".format(tup[0])
        if out_folder != "":
            untar_cmd += " -C {out_folder}".format(out_folder)
        subprocess.check_call(untar_cmd, shell=True, encoding="utf-8")
        subprocess.check_call("rm tornet_{year}.tar.gz".format(year=tup[0]),
                              shell=True, encoding="utf-8")
    
if __name__ == "__main__":
    pull_data_from_zenodo()

