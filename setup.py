"""Setup et installations
"""
import os
from setuptools import setup
from setuptools.command.install import install

# TODO


class Install(install):
    def run(self):
        install.run(self)
        os.system("echo 'message'")
        os.system("sudo sh ")


"""
python3 -m pip install spotipy  # spotify indetectable par les tests sinon

"""

"""TIME_WORK  3h """

setup(
    name="aicover",
    version="1.0.0",
    author="Antoine Rodriguez",
    author_email="rodriguezantoine@gmail.com",
    description="",  # noqa
    # license=,
    cmdclass={'install': Install}
    # keywords=,
    # url=,
    # packages=,
    # long_description=read('README')
)

if __name__ == '__main__':
    pass
