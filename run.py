import subprocess

program_list = ['wrack_combiner.py', 
                'coverage_combiner.py',
                'merger.py',
                'ph_filter.py',
                'ph_kelp.py',
                'kelp_ph_trimmer.py',
                'kelp_ph_updated.py',]

for program in program_list:
    subprocess.call(['python', program])
    print("Finished:" + program)