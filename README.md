# Concurrent Python (Paweł Kmiecik)

## Preparation
Clone the repository and then
```
virtualenv -p python3 .venv
source .venv/bin/activate
```
next in the repo root directory:
```
pip install -r requirements.txt
```
## Workng with the demo

Make sure the venv is activated.
Then try below commands.
```
python -m io_bound.demo_sequential
python -m io_bound.demo_futures_threads
python -m io_bound.demo_asyncio
python -m cpu_bound.demo_process_pool
python -m cpu_bound.demo_sequential
``` 
