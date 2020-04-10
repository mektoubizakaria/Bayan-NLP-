pip3 install -r requirements.txt
pip freeze | xargs pip uninstall -y
pip freeze | grep seaborn
pip freeze >> requirements.txt
jupyter notebook
which python