import os
import psutil

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_PATH = os.path.join(SRC_DIR, "process.py")


def terminate_processes():
    termination_pids = []
    for p in psutil.process_iter():
        try:
            arguments = p.cmdline()
            if (len(arguments) > 0) and (arguments[-1] == SCRIPT_PATH):
                termination_pids.append(p.pid)
                p.terminate()
        except (psutil.AccessDenied, psutil.ZombieProcess, psutil.NoSuchProcess):
            pass
    return termination_pids


termination_pids = terminate_processes()
if len(termination_pids) == 0:
    print("No active process to be terminated")
else:
    print(
        f"Terminated {len(termination_pids)} background "
        + f"processes with PIDs {termination_pids}"
    )
