#find . -name "*.jpg" -exec mogrify -format png {} \;
for file in ./test/*
do
  echo "processing: "
  echo $file
  convert $file -resize "200x200!" $file
done

for file in ./test/*
do
  echo "processing: "
  echo $file
  convert $file -virtual-pixel edge -fuzz 15% -monochrome $file
done

