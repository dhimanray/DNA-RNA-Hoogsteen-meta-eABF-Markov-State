set all [atomselect top "all"]
set sel [atomselect top "name C1'"]

$all set beta 0.0
$sel set beta 1.0

$all writepdb restraint.pdb 
