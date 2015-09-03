import os
import subprocess
import shutil

# Each library should be built separately for iOS and OS X and put in the right folders
for lib_name in ['libassert_lib.a', 'libdomain_registry_lib.a', 'libinit_registry_tables_lib.a']:

    lib_ios_path = os.path.join('ios', lib_name)
    lib_osx_path = os.path.join('osx', lib_name)
    lib_final_path = os.path.join('universal', lib_name)

    # Merge the iOS and OS X slices into one universal binary
    subprocess.call(['lipo', '-create', lib_ios_path, lib_osx_path, '-output', lib_final_path])