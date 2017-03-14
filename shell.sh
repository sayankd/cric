echo "x=$2"
echo "y=$1"
echo "z=$3"
a=$2
b=$1
ab=$a$b
echo "$ab"
ntfy -t $3 send $1
ntfy -t $3 send $2
