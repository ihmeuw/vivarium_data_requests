import shutil
import pathlib
import os
import subprocess

"""
Locations:
    India
    Ethiopia
    Sri Lanka

    Uttar Pradesh
    Kerala
    Bihar

    Sub-saharan Africa Super-region
    South Asia Region
    Low SDI
    Low-middle SDI
    Middle SDI
    High-middle SDI
    High SDI
"""

LOCATIONS = []
JOB_MEM = 20  # GB


def format_fname(fname: str):
    return fname.replace(' ', '_').replace(',', '').lower()


def get_output_path():
    path = pathlib.Path("/share/costeffectiveness/artifacts/vivarium_data_requests/jun_17_laura_lamberti/")
    path.mkdir(parents=True, exist_ok=True)
    return path


def create_specs():
    """Generate model specifications for each location using the template."""
    for loc in LOCATIONS:
        fname = format_fname(loc)

        with open("model_specs/template.yaml") as f:
            template_spec = f.read()

        template_spec = template_spec.format(name=loc, fname=fname)

        with open(f"model_specs/{fname}.yaml", 'w') as f:
            f.write(template_spec)


def run(fname: str):
    """build the artifact defined by fname"""
    output_path = get_output_path()
    subprocess.run(["build_artifact", "-v", "-o", str(output_path), f"./model_specs/{fname}.yaml"],
                   check=True,
                   stdout=subprocess.PIPE)
    print(f"Artifact written to {output_path}/{fname}.hdf")


def launch():
    import drmaa
    with drmaa.Session() as s:
        jt = s.createJobTemplate()
        jt.workingDirectory = os.getcwd()
        jt.remoteCommand = shutil.which('python')
        for loc in LOCATIONS:
            fname = format_fname(loc)
            jt.nativeSpecification = f'-V -w n -q all.q -l m_mem_free={JOB_MEM}G -N {fname} -l fthread=1 -P proj_cost_effect'
            jt.args = ['run_all.py', 'run', fname]
            s.runJob(jt)
            print(f"Submitted job for {loc}")
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