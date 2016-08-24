import os
import subprocess
import shutil

# Each library should be built separately for iOS and OS X and put in the right folders
# In Xcode 7 we can no longer build a universal library as the linker rejects OS X builds
# when trying to run in the simulator
# https://github.com/google/j2objc/issues/611

# Make an iOS (iOS + Simulator) library
for lib_name in ['libassert_lib.a', 'libdomain_registry_lib.a', 'libinit_registry_tables_lib.a']:
    for platform in ['ios', 'tvos']:
    
        lib_native_path = os.path.join(platform, lib_name)
        lib_simulator_path = os.path.join('{}_simulator'.format(platform), lib_name)
        lib_universal_path = os.path.join('{}_universal'.format(platform), lib_name)

        # Merge the native and simulator slices into one universal binary
        subprocess.call(['lipo', '-create', lib_native_path, lib_simulator_path, '-output', lib_universal_path])