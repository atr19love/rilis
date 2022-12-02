install termux from F-Droid (NOT PLAYSTORE)
pkg install python -y
apt update && apt upgrade
pkg install git -y
git clone https://github.com/atr19love/rilis
cd rilis
pip install --upgrade pip
pip install -r req.txt
python topixsb.py
