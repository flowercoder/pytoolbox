from setuptools import setup,find_packages
setup(name='pytoolboxes',
      version='22.5.27',
      description='private tool packages with python',
      classifiers=[
        'Programming Language :: Python',
        'Intended Audience :: Developers',
    ],
      url='https://github.com/flowercoder/pytoolboxes/',
      author='flowercoder',
      author_email='gas1015@gmail.com',
      license='NEU',
      install_requires=["fake_useragent","corpwechatbot"],
      packages=find_packages(),
      zip_safe=True,
     )
