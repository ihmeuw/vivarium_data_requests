import warnings
import shutil
import os
import subprocess

"""
Locations:
    all states in Indea, urban/rural
"""


locations = ['Uttar Pradesh', 'Kerala', 'Bihar']


def format_fname(fname: str):
    return fname.replace(' ', '_').replace(',', '_').lower()


def create_specs():
    """Generate model specifications for each location using the template."""
    for loc in locations:
        for type in ['Urban', 'Rural']:
            name = loc + type
            fname = format_fname(name)

            with open("template.yaml") as f:
                template_spec = f.read()

            template_spec = template_spec.format(name=name, fname=fname)

            with open(f"model_specs/{fname}.yaml", 'w') as f:
                f.write(template_spec)


def run(fname: str):
    """build the artifact defined by fname"""
    subprocess.call(["build_artifact", "-v", f"./model_specs/{fname}.yaml"])


def launch():
    import drmaa
    with drmaa.Session() as s:
        jt = s.createJobTemplate()
        jt.workingDirectory = os.getcwd()
        jt.remoteCommand = shutil.which('python')
        for loc in locations:
            for type in ['Urban', 'Rural']:
                name = loc + type
                fname = format_fname(name)
                jt.nativeSpecification = f'-V -w n -q all.q -l m_mem_free=20G -N {fname} -l fthread=1 -P proj_cost_effect'
                jt.args = ['run_all.py', 'run', fname]
                s.runJob(jt)
        s.deleteJobTemplate(jt)


if __name__ == "__main__":
    import sys
    cmd = sys.argv[1]
    commands = ['run', 'create_specs', 'launch']
    if cmd not in commands:
        raise ValueError(f"command should be one of {commands} ")

    if cmd == 'create_specs':
        create_specs()
    elif cmd == 'run':
        if len(sys.argv) < 3:
            raise ValueError("run requires a location")
        fname = sys.argv[2]
        run(fname)
    else:
        launch()
