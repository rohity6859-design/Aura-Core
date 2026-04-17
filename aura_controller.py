# Aura Main Controller
# Integrating Security and Growth Modules

from security_maze import security_maze
from opportunity_scout import scout_opportunities

def run_aura():
    print("--- Aura System Initializing ---")
    
    # 1. Security Check
    status = security_maze("user_access")
    print(f"Security Status: {status}")
    
    # 2. Scout for Growth
    opportunities = scout_opportunities()
    print(f"Growth Status: {opportunities}")
    
    print("--- Aura is ready to serve Yadav Sher ---")

if __name__ == "__main__":
    run_aura()
  
