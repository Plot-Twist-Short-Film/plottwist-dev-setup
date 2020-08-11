if exist plottwist_dev del plottwist_dev
"C:\Python38\Scripts\virtualenv.exe" plottwist_dev
cd plottwist_dev
cd Scripts
call activate
cd ..
cd ..
pip install -r dev_requirements.txt
pause