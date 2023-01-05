import ray

#Load Data.
dataset = ray.data.read_csv("s3://anonymous@air-example-data/breast_cancer.csv")

# dataset type : ray.data.dataset.Dataset
print("dataset type : ",type(dataset))
print(dataset)

# Split data into train and validation.
train_dataset, valid_dataset = dataset.train_test_split(test_size=0.3)

# Create a test dataset by dropping the target column.
test_dataset = valid_dataset.drop_columns(cols=["target"])

# Dataset에 target 컬럼 정보가 없어진것을 확인할 수 있다.
print(test_dataset)

# Preprocess your data with a Preprocessor.
# Create a preprocessor to scale some columns.
from ray.data.preprocessors import StandardScaler
preprocessor = StandardScaler(columns=["mean radius", "mean texture"])

#Scale out model trainning
# ray의 xgboost 모듈 설치
# pip install xgboost_ray


from ray.air.config import ScalingConfig
from ray.train.xgboost import XGBoostTrainer

trainer = XGBoostTrainer(
    scaling_config=ScalingConfig(
        num_workers=2,
        use_gpu=False,
    ),
    label_column="target",
    num_boost_round=20,
    params={
        # XGBoost specific params
        "objective":"binary:logistic",
        # "tree_method":"gpu_hist", # uncomment this to use GPUs.
        "eval_metric" : ["logloss", "error"],
    },
    datasets={"train" : train_dataset, "valid":valid_dataset},
    preprocessor=preprocessor,
)
result = trainer.fit()
print(result.metrics)