from setuptools import setup

description = "Simplified tool for evaluating a DALL-e model"

setup(
    name="clip_score",
    version="0.1.0",
    author="Mehdi Cherti",
    description=description,
    license="MIT",
    url="https://github.com/mehdidc/DALLE_clip_score",
    zip_safe=False,  # the package can run out of an .egg file
    classifiers=['Intended Audience :: Science/Research',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved',
                 'Programming Language :: Python',
                 'Topic :: Software Development',
                 'Topic :: Scientific/Engineering',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX',
                 'Operating System :: Unix',
                 'Operating System :: MacOS'],
    platforms='any',
    scripts=['joblib'],
    include_package_data=True,
    install_requires=['joblib', 'clip@git+https://github.com/openai/CLIP'],
)

