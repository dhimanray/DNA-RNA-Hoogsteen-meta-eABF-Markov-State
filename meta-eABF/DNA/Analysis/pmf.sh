#:/bin/bash

#first do:  split -d -l 7323 a6RNA-meta-eABF.abf1.hist.zcount count to generate the count00, count01 ... files
#do the same for gradient files
#then run this script

for i in {88..89}
do
	cp gradient$i gradient$i.grad
	cp count$i gradient$i.count
	/home/dhiman/NAMD_2.12_Linux-x86_64-multicore/lib/abf_integrate/abf_integrate gradient$i.grad
	a=$(( 2*i ))
	awk 'NF' gradient$i.grad.pmf > pmf_${a}_ns
done

for j in {9078..9111}
do
        i=$(( j-9000+90 ))
        cp gradient$j gradient$i.grad
        cp count$j gradient$i.count
	/home/dhiman/NAMD_2.12_Linux-x86_64-multicore/lib/abf_integrate/abf_integrate gradient$i.grad
        a=$(( 2*i ))
        awk 'NF' gradient$i.grad.pmf > pmf_${a}_ns
done
