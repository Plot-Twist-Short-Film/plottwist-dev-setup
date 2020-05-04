if exist plottwist_dev del plottwist_dev
virtualenv plottwist_dev
cd plottwist_dev
cd Scripts
call activate
cd ..
cd ..
pip install -r dev_requirements.txt
pause