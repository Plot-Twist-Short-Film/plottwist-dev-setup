if exist clonerepos_venv del clonerepos_venv
virtualenv clonerepos_venv
cd clonerepos_venv
cd Scripts
call activate
cd ..
cd ..
pip install -r requirements.txt
python git_all_repos.py orgs Plot-Twist-Short-Film
del clonerepos_venv
