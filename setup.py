from setuptools import setup

setup(name='ScrapingDSL',
      version='1.0',
      description='Generating Scrapy project using DSL',
      author='Filip Frank',
      author_email='frank.filip@hotmail.com',
      license='MIT',
      url='https://github.com/Pazzo92/scraping-dsl',
      packages=['dsl'],
      include_package_data=True,
      install_requires=["Arpeggio>=1.8.0", "textX>=1.7.0", "Scrapy>=1.5.0", "pymongo>=3.7.1", "Jinja2>=2.10", "pydot>=1.2.4"],
      keywords="meta-language meta-model language DSL scraping Scrapy",
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Scrapers',
        'Topic :: Software Development :: Compilers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        ]
     )

