
if [ "$#" -ne 1 ]; then
    echo "usage: $0 <file>"
    exit 1
fi

csv_file=$1

if [ ! -f "$csv_file" ]; then 
    echo "file : $csv_file doesn't exits"
    exit 1
fi

awk -F ',' '
BEGIN {
         printf "%-10s %-5s %-15s %-8s\n", "Name", "Age", "Dept", "Salary";
         printf "------------------------------\n";
}

NR > 1 {
        printf "%-10s %-5s %-15s %-8s\n", $1, $2, $3, $4;
        total_sum += $4;
}


END {
        printf "\n------------------------------\n";
        printf "Total Salary: %-10s\n", total_sum; 
} 
' $csv_file
