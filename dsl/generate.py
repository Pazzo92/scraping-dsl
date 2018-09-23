"""
Created on 06.12.2015.

@author: xx
"""

import os

from dsl.execute import execute
from dsl.generate_spider import SpiderGenerator
from dsl.root import SRC_DIR
from shutil import copyfile

def main(type,location="", filename="", output="", debug=False):
    
    model_main = execute(os.path.join(SRC_DIR, "language"), 'products_mining.tx', type+'_program.rbt', debug, debug)

    if type == 'movie' or type == 'poslanik':
        model = execute(os.path.join(SRC_DIR, "language"), 'type.tx', type+'_type.rbt', debug, debug )
        generator = SpiderGenerator(model, model_main)
    
    else:
        gigatron_model = execute(os.path.join(SRC_DIR, "language"), 'type.tx', type+'_type_gigatron.rbt', debug, debug )
        winwin_model = execute(os.path.join(SRC_DIR, "language"), 'type.tx', type+'_type_winwin.rbt', debug, debug )
        generator = SpiderGenerator(gigatron_model, model_main, winwin_model)
        
    generator.generate_application(type)
    
if __name__ == '__main__':
    
    # DEFINE THE TYPE OF THE SCRAPING ITEM
    type = "movie"
    main(type, False)
