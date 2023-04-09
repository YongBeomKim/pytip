folder_info='pytip.egg-info'

source /home/buffet/Coding/venv/Nlp/bin/activate
python setup.py bdist_wheel
python3.10 -m twine upload dist/*
mv ./dist/*.whl ./
rm -rf dist build "$folder_info"
deactivate
