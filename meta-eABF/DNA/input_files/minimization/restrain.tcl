set all [atomselect top "all"]
set sel1 [atomselect top "not hydrogen and segname PROE or segname PROF or nucleic"]
set sel2 [atomselect top "protein and not segname PROE and not segname PROF"]

$all set beta 0.0
$sel1 set beta 1.0
#$sel2 set beta 0.5

$all writepdb restrain.pdb 
