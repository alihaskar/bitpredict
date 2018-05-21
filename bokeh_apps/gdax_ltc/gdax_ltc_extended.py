import sys
import os
sys.path.append(os.path.basename(os.path.basename(__file__)))
from app import run_charts_extended

run_charts_extended.run_chart('gdax', 'ltc', 3*60*60)
