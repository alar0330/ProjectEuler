import sys, os
import time
import glob
from importlib import import_module
import argparse as ap
import ruamel.yaml as yaml
sys.path.append('..')


def get_args():
    parser = ap.ArgumentParser()
    parser.add_argument('-a', '--answers',
                        default='answers.yaml',
                        help="YAML file with answers")
    parser.add_argument('-p', '--problem',
                        default='0',
                        type=int,
                        help="Problem number to test ('0' for all available)")
                         
    return parser.parse_args()
    

def get_answers(file):
    with open(file, 'r') as f:
        return yaml.safe_load(f)
    

def test(problem, input, answer):
        module = import_module('problems.p{:03d}.solution'.format(p))
        tic = time.time()
        output = module.solve(input)
        elapsed = time.time() - tic
        
        print("Problem #{:03d}: {} ms ({})".format(
            problem,
            int(round(elapsed * 1000)),
            'OK' if output == answer else '*** FAILED ***'))
            
        return elapsed
    
    
if __name__ == '__main__':

    args = get_args()
    answers = get_answers(args.answers)
    timer = 0.
        
    if args.problem:
        problems = [args.problem]
    else:
        all_solutions = sorted(glob.glob('../problems/p*/solution.py'))
        problems = [int(os.path.basename(os.path.dirname(m))[1:]) for m in all_solutions]
        
    for p in problems:
        inp = int(answers[p]['inp'])
        ans = int(answers[p]['ans'])
        timer += test(p, inp, ans)
    
    print("-" * 30)
    print("Total time: {:.3f} s".format(timer))

    