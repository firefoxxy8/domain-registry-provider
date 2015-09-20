import os
import subprocess
import shutil

# Each library should be built separately for iOS and OS X and put in the right folders
# In Xcode 7 we can no longer build a universal library as the linker rejects OS X builds
# when trying to run in the simulator
# https://github.com/google/j2objc/issues/611

# Make an iOS (iOS + Simulator) library
for lib_name in ['libassert_lib.a', 'libdomain_registry_lib.a', 'libinit_registry_tables_lib.a']:

    lib_ios_path = os.path.join('ios', lib_name)
    lib_osx_path = os.path.join('simulator', lib_name)
    lib_final_path = os.path.join('ios_universal', lib_name)

    # Merge the iOS and OS X slices into one universal binary
    subprocess.call(['lipo', '-create', lib_ios_path, lib_osx_path, '-output', lib_final_path])