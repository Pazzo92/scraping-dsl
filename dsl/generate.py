"""
Created on 06.12.2015.

@author: xx
"""

import os

from dsl.execute import execute
from dsl.generate_spider import SpiderGenerator
from dsl.root import SRC_DIR

def main(type,location="", filename="", output="", debug=False):

    model = execute(os.path.join(SRC_DIR, "language"), 'type.tx', 'types.rbt', debug, debug)


    model_main = execute(os.path.join(SRC_DIR, "language"), 'products_mining.tx', type+'_program.rbt', debug, debug)
    
    generator = SpiderGenerator(model, model_main)
    generator.generate_application(type)
    
if __name__ == '__main__':
    
    # DEFINE THE TYPE OF THE SCRAPING ITEM
    type = "movie"
    main(type, False)
