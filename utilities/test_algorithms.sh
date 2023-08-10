# test_algorithms.sh 
#
# Execute algorithms unit tests and generate report
# @pre: Ran from the root of the repository

# Navigate to algorithms test directory
cd algorithms_module/tests

# Run pytest and tee output to file
touch "algorithms-test-output.txt"
echo "----- Algorithms Module Unit Testing -----" 2>&1 | tee -a algorithms-test-output.txt

now=`date`
echo "----- Execution Date: $now" 2>&1 | tee -a algorithms-test-output.txt

hash=`git log -1 --format="%H"`
echo "----- Commit Hash: $hash" 2>&1 | tee -a algorithms-test-output.txt
echo "" 2>&1 | tee -a algorithms-test-output.txt

pytest . -v 2>&1 | tee -a algorithms-test-output.txt

# Move file to docs/Reports
mv algorithms-test-output.txt ../../doc/Reports

