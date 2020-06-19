from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='1uhr', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='6lth', atom_files='6lth.pdb')
aln.append(file='Q9VYG2.ali', align_codes='Q9VYG2')
aln.align2d()
aln.write(file='Q9VYG2-6lth.ali', alignment_format='PIR')
aln.write(file='Q9VYG2-6lth.pap', alignment_format='PAP')