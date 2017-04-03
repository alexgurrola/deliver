import os
import sys

pid = str(os.getpid())
pid_file = "/tmp/halcyon.pid"

# verify
if os.path.isfile(pid_file):
    print(pid_file, "already exists, exiting")
    sys.exit()

# lock
with open(pid_file, 'w') as file:
    file.write(pid)

# run
try:
    input('press any key to continue...')
finally:
    os.unlink(pid_file)

# TODO: Check from CRON (this complains if the file doesn't exist, though)
# ps up `cat /tmp/halcyon.pid` > /dev/null && echo "Running" || echo "Not running"
