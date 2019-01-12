from sys import argv
from collections import defaultdict as dd
from random import shuffle

if __name__=='__main__':
    filenames=argv[1:]

    for filename in filenames:
        analyses = dd(set)

        for line in open(filename, "r", encoding="utf-8"):
            line = line.strip()
            freq, apertium_analysis_output = line.split()

            wf = apertium_analysis_output.split("/")[0].lstrip("^")
            for apertium_analysis in apertium_analysis_output.split("/")[1:]:
                # todo: is the plus sign necessary?
                analyses[wf].add(" +<".join(apertium_analysis.rstrip("$").split("<")))

        pretty_filename = filename.replace("10000.txt","")
        src_train = open('%s-src-train.txt' % pretty_filename, 'w', encoding='utf-8')
        tgt_train = open('%s-tgt-train.txt' % pretty_filename, 'w', encoding='utf-8')

        src_val = open('%s-src-val.txt' % pretty_filename, 'w', encoding='utf-8')
        tgt_val = open('%s-tgt-val.txt' % pretty_filename, 'w', encoding='utf-8')

        src_val_all = open('%s-src-val.all.txt' % pretty_filename, 'w', encoding='utf-8')
        tgt_val_all = open('%s-tgt-val.all.txt' % pretty_filename, 'w', encoding='utf-8')

        src_test = open('%s-src-test.txt' % pretty_filename, 'w', encoding='utf-8')
        tgt_test = open('%s-tgt-test.all.txt' % pretty_filename, 'w', encoding='utf-8')
        
        analyses = list(analyses.items())
        shuffle(analyses)
        
        for i,wf_analysis in enumerate(analyses):
            wf, analysis = wf_analysis
            if i % 10 < 8:
                for a in analysis:
                    print(wf,file=src_train)
                    print(a,file=tgt_train)
            elif i % 10 == 8:
                for a in analysis:
                    print(wf,file=src_val)
                    print(a,file=tgt_val)
                    print(wf,file=src_val_all)
                    print('\t'.join(analysis),file=tgt_val_all)
                else:
                    print(wf,file=src_test)
                    print('\t'.join(analysis),file=tgt_test)
