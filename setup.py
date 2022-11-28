import setuptools
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


setuptools.setup(
    name="YoutubeVideoTrimmer",
    version="0.0.5",
    author="Arunkumar Palani",
    author_email="arunkumarpas002@gmail.com",
    description="A compact solution for trimming YouTube videos You may get the desired output video clip by providing the YouTube video URL and required duration.",
    packages=setuptools.find_packages(),
    classifiers=[        
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python",
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        "Topic :: Internet",
        "Topic :: Multimedia :: Video",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Terminals",
        "Topic :: Utilities",
        "Natural Language :: English", 
        "Environment :: Console",
        "Environment :: Web Environment",
        
        ],
    long_description_content_type="text/markdown",
    long_description=long_description,
    zip_safe=True,
    url="https://www.karuwy.com/",
    include_package_data=True,
    install_requires=["pytube", "moviepy"],
    keywords=["youtube", "download", "video", "stream","trimmer","youtube video trimmer","youtube video downloader","youtube video downloader and trimmer"],
)