import dowhy
from dowhy.do_why import CausalModel
import dowhy.datasets

# Load some sample data
data=dowhy.datasets.linear_dataset(
        beta=10,
        num_common_causes=5,
        num_instruments = 2,
        num_samples=10000,
        treatment_is_binary=True)

data2 = dowhy.datasets.xy_dataset(
        num_samples=1000,
        effect= True)

print(data)
print(data2)