folder_info='pytip.egg-info'

# source /home/buffet/Coding/venv/Py/bin/activate
# python setup.py bdist_wheel
# twine upload dist/*
# mv ./dist/*.whl ./
# rm -rf dist build "$folder_info"
# deactivate
# source /home/buffet/Coding/venv/Py/bin/activate
# python setup.py bdist_wheel
# python3.10 -m twine upload dist/*
pyv
python setup.py sdist bdist_wheel
twine upload dist/*
mv ./dist/*.whl ./
rm -rf dist build "$folder_info"
deactivate