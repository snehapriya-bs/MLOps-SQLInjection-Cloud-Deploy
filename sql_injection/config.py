app_config:
  package_name: "bikeshare_model"
  training_data_file: "train.csv"

model_config:
  target: "Label"
  query: "SELECT * FROM data_table"
  test_size: 0.2
  random_state: 42
  n_estimators: 100
  max_depth: 10
