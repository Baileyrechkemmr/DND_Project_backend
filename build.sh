set -o errexit

pip3 install -r requierments.txt

python3 manage.py migrate