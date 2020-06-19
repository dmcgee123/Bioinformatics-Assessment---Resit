from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='1uhr', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='1v31', atom_files='1v31.pdb')
aln.append(file='Q9VYG2.ali', align_codes='Q9VYG2')
aln.align2d()
aln.write(file='Q9VYG2-1v31.ali', alignment_format='PIR')
aln.write(file='Q9VYG2-1v31.pap', alignment_format='PAP')