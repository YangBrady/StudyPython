@echo off
echo "begin install python libs"

python -m pip install --upgrade pip
python -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
python -m pip install ./gdal/GDAL-3.0.4-cp37-cp37m-win_amd64.whl