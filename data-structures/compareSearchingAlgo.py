from searchingAlgo.binarySearch import binarySearch
from searchingAlgo.sequentialSearch import searchMethod1

import random
random.seed(0)
arr = [random.randint(1, 100) for _ in range(100)]
print("-----"*10)
print("data--")
print("-----"*10)
print(arr)
print("-----"*10)
print("-----"*10)
data = {"comparisions":{"binary":[], "sequential":[]},
        "steps":{"binary":[], "sequential":[]}}
for _ in range(5):
    random.seed(_+1)
    x = random.randint(1,150)
    binary = binarySearch(sorted(arr.copy()), x)
    sequential = searchMethod1(arr, x)
    print("binary - ", x, ' - ', binary)
    print("sequential - ", x, ' - ', sequential)
    data["comparisions"]['binary'].append(binary[-1]['comparisions'])
    data["comparisions"]['sequential'].append(sequential[-1]['comparisions'])
    data["steps"]['binary'].append(binary[-1]['steps'])
    data["steps"]['sequential'].append(sequential[-1]['steps'])

print("-----"*10)
print('Analysis')
print("-----"*10)
print("BinComp| SeqComp| BinSteps| SeqSteps")
for i in range(len(data['comparisions']['binary'])):
    print("   ", end="")
    print(data['comparisions']['binary'][i], end='\t')
    print("   ", end="")
    print(data['comparisions']['sequential'][i], end='\t')
    print("      ", end="")
    print(data['steps']['binary'][i], end='\t')
    print("      ", end="")
    print(data['steps']['sequential'][i])
print("-----"*10)
print("-----"*10)
