"""
Created on 06.12.2015.

@author: xx
"""

import os

from dsl.execute import execute
from dsl.generate_spider import SpiderGenerator
from dsl.root import SRC_DIR
from dsl.root import EXAMPLES_PATH
from shutil import copyfile

def main(type,domain, location="", filename="", output="", debug=False):
    
    examples_folder = os.path.join(EXAMPLES_PATH, "examples")
    
    model_main = execute(os.path.join(SRC_DIR, "language"), 'products_mining.tx', examples_folder+"/"+domain+"/"+type+'_program.sdq', debug, debug)

    model = execute(os.path.join(SRC_DIR, "language"), 'type.tx', examples_folder+"/"+domain+"/types/"+type+'_type.sdt', debug, debug )
    generator = SpiderGenerator(model, model_main)
         
    generator.generate_application(type, domain)
    
if __name__ == '__main__':
    
    # DEFINE THE TYPE AND THE DOMAIN OF THE SCRAPING ITEM
    domain = "imdb"
    type = "movie"
    main(type, domain, False)
