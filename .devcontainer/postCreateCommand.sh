#!/bin/sh

echo ===================================================
git --version

python3 --version
python3 -c "import django; print('Django ' + django.get_version())"
pytest --version
echo ===================================================