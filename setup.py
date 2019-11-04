from setuptools import setup

setup(
    name='streamlabswater_stream',
    version='0.2.1',
    packages=['streamlabswater'],
    keywords = ['streamlabs', 'streamlabswater', 'iot', 'water', 'sensor', 'smarthome', 'automation'],
    license='MIT',
    author='StreamLabs',
    author_email='support@streamlabswater.com',
    description='Python library for the StreamLabs Developer API',
    install_requires=['requests'],
    python_requires='>=3.6',
)
