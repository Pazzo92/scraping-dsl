"""
Created on 06.12.2015.

@author: xx
"""

import os

from dsl.execute import execute
from dsl.generate_spider import SpiderGenerator
from dsl.root import SRC_DIR

def main(location="", filename="", output="", debug=False):

    model_type = execute(os.path.join(SRC_DIR, "language"), 'type.tx', 'laptop.rbt', debug, debug)
    model = execute(os.path.join(SRC_DIR, "language"), 'products_mining.tx', 'laptop_program.rbt', debug, debug)
    
    generator = SpiderGenerator(model)
    generator.generate_application(output)


if __name__ == '__main__':
    main(False)
