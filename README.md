<div style="text-align:center"><img width="100px" src="doc/logo.png" /></div>

# DecisionSystem
A system of decision based in models predictions and master_policies with A/B test (DaC by Factory design pattern)


## Requirements:
- Unix System
- Python 3.9.6

## How to start
Clone the repository
```sh
git clone git@github.com:eduardoKatsurayama/DecisionSystem.git
```

Update the remote
```sh
git remote set-url origin git@github.com:eduardoKatsurayama/DecisionSystem.git
```

Create a branch homolog
```sh
git checkout -b "homolog"
```

Into a virtualenv install the dependencies:
```sh
pip install -r requirements/dev.txt
```

Create the .env based on .env.sample:
```sh
cp contrib/.env.sample .env
```

Run:
```sh
python -m src.main.py
```

External Run:
```sh
./run.sh
```