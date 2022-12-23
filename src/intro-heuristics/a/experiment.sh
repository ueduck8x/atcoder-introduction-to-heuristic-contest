for i in {1..10}
do
  python3 tester/generator.py $i > test/sample-$i.in
  python3 main.py < test/sample-$i.in > test/sample-$i.out
  python3 tester/tester.py test/sample-$i.in test/sample-$i.out
done
