import sys
import os
sys.path.append(os.path.basename(os.path.basename(__file__)))
from app import run_charts

run_charts.run_chart('bfx', 'btc', 9*60)
