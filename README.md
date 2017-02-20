This is the library I use in TrustKit to detect whether A is a subdomain of B.
I had to make minor changes so that it builds for OS X and iOS.

Build
=====

First install gyp:

    git clone https://chromium.googlesource.com/external/gyp
    cd gyp
    sudo ./setup.py install

Then use it to build the project:
    
    cd src
    build/run_gyp

Lastly, open build/all.xcodeproj to build the individual libraries; remember to use Xcode's Archive build operation so that the libraries are built for Release and with bitcode enabled.

To build a universal library (OS X & iOS), a script is available at ./create_universal_libraries.py.

In your project, you can then import the libraries as static dependencies and then add the domain_registry.h header.

For updating, see: https://github.com/pagespeed/mod_pagespeed/wiki/Updating-the-Public-Suffix-List
